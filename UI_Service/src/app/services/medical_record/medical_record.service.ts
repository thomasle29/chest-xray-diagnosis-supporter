import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JsonConvert } from 'json2typescript';
import { map } from 'rxjs/operators';
import { Response } from '../response.model';
import { MedicalDiseasePrediction } from './medical_record.model';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class MedicalRecordService {
    private jsonConvert: JsonConvert = new JsonConvert();

    constructor(
      private http: HttpClient
    ) { }

    submitMedicalRecord(
        patientName: string, 
        patientBirthday: string, 
        patientSex: number,
        patientJob: string,
        patientAddress: string,
        doctorID: string,
        patientSymptoms: string,
        doctorAdvice: string,
        xrayImage: string
        ): Observable<Response<MedicalDiseasePrediction[]>>{
        return this.http.post<Response<MedicalDiseasePrediction[]>>(
            `${environment.BASE_URL}/analysis`,
            {
                "patient_name": patientName,
                "patient_birthday": patientBirthday,
                "patient_sex": patientSex,
                "patient_job": patientJob,
                "patient_address": patientAddress,
                "doctor_id": doctorID,
                "patient_symptoms"  : patientSymptoms,
                "doctor_advice"     : doctorAdvice,
                "xray_image": xrayImage
            }
            ).pipe(map(resp => {
                if (resp.returncode !== 1) {
                    return resp;
                }
                if (resp.data) {
                    resp.data = resp.data.map(item => this.jsonConvert.deserializeObject(item, MedicalDiseasePrediction));
                }
                return resp;
            }));
    }

    submitDoctorPredcitionComment(
        medicalRecordID: string, 
        doctorPredictionComment: string, 
        diseaseIDDoctorValidation: string,
        diseaseNameByDoctor: string,
        ): Observable<Response<String>>{
        return this.http.post<Response<String>>(
            `${environment.BASE_URL}/doctor/comment/submit`,
            {
                "medical_record_id": medicalRecordID,
                "doctor_prediction_comment": doctorPredictionComment,
                "disease_id_doctor_validation": diseaseIDDoctorValidation,
                "disease_name_by_doctor": diseaseNameByDoctor
            }
            ).pipe(map(resp => {
                if (resp.returncode !== 1) {
                    return resp;
                }
                return resp;
            }));
    }
}