import { Component, Injectable, OnInit } from '@angular/core';
import { inject } from '@angular/core/testing';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { MatIcon } from '@angular/material/icon';
import { Router } from '@angular/router';
import { MedicalRecordService } from '../services/medical_record/medical_record.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})

@Injectable({providedIn: 'root'})

export class LoginComponent implements OnInit {
  hide = true;
  public userForm: FormGroup;

  constructor( 
    private fb: FormBuilder,
    private _router:Router,
    private medicalRecordService: MedicalRecordService
    ) {
    // this.medicalRecordService = inject(MedicalRecordService);
    localStorage.clear();
    // Form element defined below
    this.userForm = this.fb.group({
      name: '',
      password:''
    });
  }
  Login = new FormGroup({
    username: new FormControl("", Validators.required),
    password: new FormControl("", Validators.required),
  })
  ngOnInit(): void {
  }
  navigateToHome(){
    this._router.navigateByUrl('/user')
  }
  
  // submitAnalysisMedicalRecord(): void {
  //   const patientName = "Nguyễn Văn Tâm"
  //   const patientage = 30
  //   const patientSex = 1
  //   const patientJob = "Bác sĩ"
  //   const patientAddress = "290 An Dương Vương, Hồ Chí Minh"
  //   const doctorID = "DT1"
  //   const patientSymptoms = "Ho, sốt 38 độ, nổi sởi"
  //   const doctorAdvice = "Truyền 1l nước biển, tiêm 1 mũi hạ sốt"
  //   const xrayImage = "image"

  //   medicalRecordService: MedicalRecordService

  //   MedicalRecordService.submitMedicalRecord(
  //     patientName, patientage, patientSex,
  //     patientJob, patientAddress, doctorID,
  //     patientSymptoms, doctorAdvice, xrayImage
  //     ).subscribe(resp => {
  //     if (resp.returncode !== 1) {
  //       // this.errorMessage = 'Cannot get detail visitor' 
  //     }
  //     console.log(resp.data)
  //   }, () => {
  //     // this.snotify.error('Something went wrong, please try again!', { timeout: 3000, position: SnotifyPosition.rightTop, }) 
  //   }, () => {
  //   }) 
  // } 

  submitAnalysisMedicalRecord(): void {
    const patientName = "Nguyễn Văn Tâm"
    const patientage = 30
    const patientSex = 1
    const patientJob = "Bác sĩ"
    const patientAddress = "290 An Dương Vương, Hồ Chí Minh"
    const doctorID = "DT1"
    const patientSymptoms = "Ho, sốt 38 độ, nổi sởi"
    const doctorAdvice = "Truyền 1l nước biển, tiêm 1 mũi hạ sốt"
    const xrayImage = "image"

    console.log("Run submitAnalysisMedicalRecord")

    this.medicalRecordService.submitMedicalRecord(
      {patientName, patientage, patientSex,
      patientJob, patientAddress, doctorID,
      patientSymptoms, doctorAdvice, xrayImage}
      ).subscribe((resp) => {
      if (resp.returncode !== 1) {
        // this.errorMessage = 'Cannot get detail visitor' 
      }
      console.log(resp.data)
    }, () => {
      // this.snotify.error('Something went wrong, please try again!', { timeout: 3000, position: SnotifyPosition.rightTop, }) 
    }, () => {
    }) 

  }

  checkLogin() {
    const name = (<HTMLInputElement>document.getElementById("name")).value;
    const password = (<HTMLInputElement>document.getElementById("password")).value;
    // <a routerLink="/home">Home</a>
    console.log(name,password);
    if(name==="may" && password==="1"){
      this.navigateToHome();
    }else{
      alert("wrong pass or username")
    }
  }
  
}
