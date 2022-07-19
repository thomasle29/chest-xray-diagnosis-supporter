from ast import arg
from Infrastructure import util
import Config.reader as reader
import main
import json
import requests


class App:
    '''
    App class
    Manufacturing application function of this service
    '''
    reader = reader.Reader()
    config_MySQL = reader.get_config_MySQL()
    # config database
    def __init__(self) -> None:
        self.util   = util.Util(host = self.config_MySQL['MYSQL']['HOST'], 
                                user = self.config_MySQL['MYSQL']['USER'], 
                                password = self.config_MySQL['MYSQL']['PASSWORD'], 
                                database = self.config_MySQL['MYSQL']['DATABASE'])
        self.new_id = str()
        self.store_disease = []
    def pro_login(self, args):
        args = self.pre_json(args)
        sql = self.util
        return sql.pro_login(args)
    
    def pro_new_medical_record(self,args):
        args = self.pre_json(args)
        sql = self.util
        new_medical = sql.pro_new_medical_record(args) 
        if new_medical != "1":
            chest_result = self.chestDiagnosis(args[8]) # 8 is xray_image in arr
            chest_result = json.loads(chest_result)
            # chest_result = '''[{
            #                 "disease_name": "Edema",
            #                 "base64_image_diagnosis": "ABC",
            #                 "predictions": 0.70
            #                 },
            #                 {
            #                 "disease_name": "mass",
            #                 "base64_image_diagnosis": "XYZ",
            #                 "predictions": 0.75
            #                 }
            #                 ]'''
            chest_result = json.loads(chest_result)
            self.new_id = new_medical   
            dict_chest_result = {"ID": new_medical}
            disease = []
            for dis in chest_result:
                dis_id = sql.pro_disease_id([dis["disease_name"]])
                disease.append({"disease_id:": dis_id,
                                "disease_name": dis["disease_name"],
                                "base64_image_diagnosis":dis["base64_image_diagnosis"],
                                "predictions":dis["predictions"]})
                self.store_disease.append([ dis["disease_name"],
                                            dis_id,
                                            dis["base64_image_diagnosis"],
                                            dis["predictions"]])
            dict_chest_result["medical_record_disease"] = disease
            json_chest_result = json.dumps(dict_chest_result)
            return json_chest_result
        else:
            return new_medical

    def pro_diagnosis_report(self,args):
        sql = self.util
        return sql.pro_diagnosis_report(args)

    def submit_report(self,args):
        sql = self.util
        result = "0"
        for dis in self.store_disease:
            if args["disease_id_doctor_validation"] == dis[1]:
                valid = 1
            else:
                valid = 0
            result = self.pro_diagnosis_report( [args["medical_record_id"],   # medical_id
                                                dis[1],         # disease_id
                                                dis[2],         # base64_image_diagnosis
                                                dis[3],         # prediction
                                                valid         # doctor valid
                                                ])
        update_medial = sql.pro_report_medical( [args["medical_record_id"],
                                args["doctor_prediction_comment"],
                                args["disease_name_by_doctor"],
                                len(self.store_disease),
                                ])    #   id, comment, doctor's prediction, num of predict
        self.store_disease = []
        if update_medial == "0" and result == "0":
            return "0"
        return "1"

    def chestDiagnosis(self,args):
        dic_args = {"base64_image": args}
        j_args = json.dumps(dic_args)
        response = requests.post("http://127.0.0.1:8020/chest/diagnosis",data=j_args)
        result = response.text
        if result == "0":
            return "0"
        return str(response.text)

    def pre_json(self,j_str):
        j_arr = []
        for str in j_str:
            j_arr.append(j_str[str])
        return j_arr