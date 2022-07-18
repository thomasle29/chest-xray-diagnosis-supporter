import { JsonObject, JsonProperty } from 'json2typescript';

@JsonObject('MedicalDiseasePrediction')
export class MedicalDiseasePrediction {
    @JsonProperty('disease_id', String)
    diseaseID: string = undefined;
    
    @JsonProperty('disease_name', String)
    diseaseName: string = undefined;

    @JsonProperty('base64_image_diagnosis', String)
    base64ImageDiagnosis: string = undefined;

    @JsonProperty('predictions', String)
    predictions: String = undefined;
}

@JsonObject('MedicalPrediction')
export class MedicalDiseasePrediction {
    @JsonProperty('medical_record_id', String)
    medicalRecordID: string = undefined;

    @JsonProperty('medical_record_disease', [MedicalDiseasePrediction])
    medicalRecordDisease: MedicalDiseasePrediction[] = undefined;
}

