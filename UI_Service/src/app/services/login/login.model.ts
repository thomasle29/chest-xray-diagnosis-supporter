import { JsonObject, JsonProperty } from 'json2typescript';

@JsonObject('LoginInfo')
export class LoginInfo {
    @JsonProperty('doctor_id', String)
    doctorID: string = undefined;
    
    @JsonProperty('doctor_name', String)
    doctorName: string = undefined;
}