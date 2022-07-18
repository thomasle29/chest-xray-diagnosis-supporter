import { JsonObject, JsonProperty } from 'json2typescript';

@JsonObject('MedicalDiseasePrediction')
export class MedicalDiseasePrediction {
    @JsonProperty('disease_name', String)
    diseaseName: string = undefined;

    @JsonProperty('base64_image_diagnosis', String)
    base64ImageDiagnosis: string = undefined;

    @JsonProperty('predictions', String)
    predictions: string = undefined;
}