import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JsonConvert } from 'json2typescript';
import { map } from 'rxjs/operators';
import { Response } from '../response.model';
import { MedicalDiseasePrediction } from './medical_record.model';
import { environment } from '../../../../environments/environment'
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class MedicalRecordService {
    private jsonConvert: JsonConvert = new JsonConvert();
    // static submitMedicalRecord: any;

    constructor(
      private http: HttpClient
    ) { }

    submitMedicalRecord(
        { 
            patientName, patientage, patientSex, patientJob, patientAddress, doctorID, patientSymptoms, doctorAdvice, xrayImage 
        }: { 
            patientName: string; patientage: number; patientSex: number; patientJob: string; patientAddress: string; doctorID: string; patientSymptoms: string; doctorAdvice: string; xrayImage: string; 
        }
        ): Observable<Response<MedicalDiseasePrediction[]>>{
            console.log("Run submitMedicalRecord")
        return this.http.post<Response<MedicalDiseasePrediction[]>>(
            `${environment.SERVER_URL}/chest/analysis`,
            {
                "patient_name": patientName,
                "patient_age": patientage,
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
            `${environment.SERVER_URL}/doctor/comment/submit`,
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