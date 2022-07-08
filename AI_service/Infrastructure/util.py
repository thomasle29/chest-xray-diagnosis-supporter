# from turtle import pos
from pyexpat import model
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator
from keras.applications.densenet import DenseNet121
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras import backend as K
from keras.models import load_model

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
tf.compat.v1.disable_eager_execution()
import base64
from PIL import Image
import io

import random

import cv2
# from keras import backend as K
from keras.preprocessing import image
from sklearn.metrics import roc_auc_score, roc_curve
from tensorflow.compat.v1.logging import INFO, set_verbosity
import os
import base64

class Util:

    IMAGE_DIR = "./Models/images-small/"
    DF_DIR = "./Models/train-small.csv"

    LABELS = ['Cardiomegaly', 
            'Emphysema', 
            'Effusion', 
            'Hernia', 
            'Infiltration', 
            'Mass', 
            'Nodule', 
            'Atelectasis',
            'Pneumothorax',
            'Pleural_Thickening', 
            'Pneumonia', 
            'Fibrosis', 
            'Edema', 
            'Consolidation']
            
    LABELS_TO_SHOW = np.array([
        'Cardiomegaly', 'Edema', 'Mass', 'Pneumothorax'
    ])

    def __init__(self) -> None:
        random.seed(a=None, version=2)
        set_verbosity(INFO)
        self.train_df = pd.read_csv("./Models/train-small.csv")
        train_generator = self.get_train_generator(self.train_df, self.IMAGE_DIR, "Image", self.LABELS)
        freq_pos, freq_neg = self.compute_class_freqs(train_generator.labels)
        self.pos_weights = freq_neg
        self.neg_weights = freq_pos
        self.model = self.load_model(self.pos_weights, self.neg_weights)
        print("init done")
        
    def load_model(self, pos_weights, neg_weights):
        # create the base pre-trained model
        base_model = DenseNet121(weights='./Models/densenet.hdf5', include_top=False)

        x = base_model.output

        # add a global spatial average pooling layer
        x = GlobalAveragePooling2D()(x)

        # and a logistic layer
        predictions = Dense(len(self.LABELS), activation="sigmoid")(x)

        model = Model(inputs=base_model.input, outputs=predictions)
        model.compile(optimizer='adam', loss=self.get_weighted_loss(pos_weights, neg_weights))
        model.load_weights("./Models/pretrained_model.h5")
        # model._make_predict_function()
        return model

    def get_train_generator(self, df, image_dir, x_col, y_cols, shuffle=True, batch_size=8, seed=1, target_w = 320, target_h = 320):
        """
        Return generator for training set, normalizing using batch
        statistics.

        Args:
        train_df (dataframe): dataframe specifying training data.
        image_dir (str): directory where image files are held.
        x_col (str): name of column in df that holds filenames.
        y_cols (list): list of strings that hold y labels for images.
        batch_size (int): images per batch to be fed into model during training.
        seed (int): random seed.
        target_w (int): final width of input images.
        target_h (int): final height of input images.
        
        Returns:
            train_generator (DataFrameIterator): iterator over training set
        """        
        print("getting train generator...") 
        # normalize images
        image_generator = ImageDataGenerator(
            samplewise_center=True,
            samplewise_std_normalization= True)
        
        # flow from directory with specified batch size
        # and target image size
        generator = image_generator.flow_from_dataframe(
                dataframe=df,
                directory=image_dir,
                x_col=x_col,
                y_col=y_cols,
                class_mode="raw",
                batch_size=batch_size,
                shuffle=shuffle,
                seed=seed,
                target_size=(target_w,target_h))
        
        return generator

    def compute_class_freqs(self, labels):
        """
        Compute positive and negative frequences for each class.

        Args:
            labels (np.array): matrix of labels, size (num_examples, num_classes)
        Returns:
            positive_frequencies (np.array): array of positive frequences for each
                                            class, size (num_classes)
            negative_frequencies (np.array): array of negative frequences for each
                                            class, size (num_classes)
        """
        ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
        
        # total number of patients (rows)
        N = labels.shape[0]
        
        positive_frequencies = np.sum(labels, axis = 0) / N
        negative_frequencies = 1 - positive_frequencies

        ### END CODE HERE ###
        return positive_frequencies, negative_frequencies  
   
    def get_weighted_loss(self, pos_weights, neg_weights, epsilon=1e-7):
        """
        Return weighted loss function given negative weights and positive weights.

        Args:
        pos_weights (np.array): array of positive weights for each class, size (num_classes)
        neg_weights (np.array): array of negative weights for each class, size (num_classes)
        
        Returns:
        weighted_loss (function): weighted loss function
        """
        def weighted_loss(y_true, y_pred):
            """
            Return weighted loss value. 

            Args:
                y_true (Tensor): Tensor of true labels, size is (num_examples, num_classes)
                y_pred (Tensor): Tensor of predicted labels, size is (num_examples, num_classes)
            Returns:
                loss (float): overall scalar loss summed across all classes
            """
            # initialize loss to zero
            loss = 0.0
            
            ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###

            for i in range(len(pos_weights)):
                # for each class, add average weighted loss for that class 
                loss += K.mean(-(pos_weights[i] *y_true[:,i] * K.log(y_pred[:,i] + epsilon) 
                                + neg_weights[i]* (1 - y_true[:,i]) * K.log( 1 - y_pred[:,i] + epsilon))) #complete this line
            return loss
        
            ### END CODE HERE ###
        return weighted_loss   

    # Util Tool
    def get_mean_std_per_batch(self, image_dir = IMAGE_DIR, df_dir = DF_DIR, H=320, W=320):
        sample_data = []
        df = pd.read_csv(df_dir)
        for img in df.sample(100)["Image"].values:
            image_path = os.path.join(image_dir, img)
            sample_data.append(
                np.array(tf.keras.utils.load_img(image_path, target_size=(H, W))))

        mean = np.mean(sample_data, axis=(0, 1, 2, 3))
        std = np.std(sample_data, axis=(0, 1, 2, 3), ddof=1)
        return mean, std

    def image_preprocessing(self, base64_code, preprocess=True, H=320, W=320):
        """Load and preprocess image."""
        mean, std = self.get_mean_std_per_batch()
        # img_path = os.path.join(image_dir, img)
        # x = image.load_img(img_path, target_size=(H, W))
        image_decode = base64.b64decode(base64_code)
        img = Image.open(io.BytesIO(image_decode))
        x = np.array(img, dtype='float')
        # x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
        x = cv2.resize(x, (W, H), cv2.INTER_LINEAR)
        # print(len(x.shape))
        if len(x.shape) < 3:
            x = np.stack((x,)*3, axis=-1)
        if preprocess:
            x -= mean
            x /= std
            x = np.expand_dims(x, axis=0)
        return x


    def grad_cam(self, image, cls, layer_name = 'bn', H=320, W=320):
        """GradCAM method for visualizing input saliency."""
        y_c = self.model.output[0, cls]
        conv_output = self.model.get_layer(layer_name).output
        grads = K.gradients(y_c, conv_output)[0]

        gradient_function = K.function([self.model.input], [conv_output, grads])

        output, grads_val = gradient_function([image])
        output, grads_val = output[0, :], grads_val[0, :, :, :]

        weights = np.mean(grads_val, axis=(0, 1))
        cam = np.dot(output, weights)

        # Process CAM
        cam = cv2.resize(cam, (W, H), cv2.INTER_LINEAR)
        cam = np.maximum(cam, 0)
        cam = cam / cam.max()
        return cam


    def compute_gradcam(self, base64_code):
        image_x = self.image_preprocessing(base64_code, preprocess=True)
        predictions = self.model.predict(image_x)
        # gradcam = self.grad_cam(image_x)
        diagnosis_list = {}
        normal_image = self.image_preprocessing(base64_code, preprocess=False)
        normal_image = np.asarray(normal_image, np.float64)

        j = 1
        for i in range(len(self.LABELS)):
            if self.LABELS[i] in self.LABELS_TO_SHOW:
                # print(f"Generating gradcam for class {labels[i]}")
                gradcam = self.grad_cam(image_x, cls=i)
                if predictions[0][i] > 0.5:
                    mask = plt.imshow(gradcam, cmap='jet', alpha=min(0.5, predictions[0][i]))
                    mask, _, _, _ = mask.make_image("normalize", unsampled=True)
                    mask = mask[:, :, 0:3]
                    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

                    dst = cv2.addWeighted(normal_image,0.7,mask,0.5,0, dtype=cv2.CV_64F)
                    _, buffer = cv2.imencode(".jpg", dst)
                    jpg_as_text = base64.b64encode(buffer)

                    diagnosis = {}
                    diagnosis["base64_image_diagnosis"] = jpg_as_text.decode('utf-8')
                    diagnosis["predictions"] = predictions[0][i]

                    diagnosis_list[self.LABELS[i]] = diagnosis
                j += 1

        if len(diagnosis_list) > 0:
            return diagnosis_list

        return 0