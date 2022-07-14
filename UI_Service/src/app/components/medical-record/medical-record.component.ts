import { Component, OnInit } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';

@Component({
  selector: 'app-medical-record',
  templateUrl: './medical-record.component.html',
  styleUrls: ['./medical-record.component.scss']
})
export class MedicalRecordComponent implements OnInit {

  url: any = "";
  constructor() { }

  ngOnInit(): void {
  }
  //lay file tu may tinh
  onFileSelected(e: any) {//a function
    if (e.target.files) {
      var reader = new FileReader();
      reader.readAsDataURL(e.target.files[0]);
      reader.onload = (event: any) => {
        this.url = event.target.result;
      }
    }
  }
  //lay file tu may tinh va chuyen thanh base64
  myImage!: Observable<any>;

  base64code!: any;
  //function khi click choose file
  onChange = ($event: Event) => {
    const target = $event.target as HTMLInputElement;

    const file: File = (target.files as FileList)[0];

    console.log(file);//in ra ten hinh anh da chon


  }

  readFile(file: File, subscriber: Subscriber<any>) {
    const filereader = new FileReader();//đặt biến toàn bộ là chữ thường

    filereader.readAsDataURL(file);

    filereader.onload = () => {
      subscriber.next(filereader.result);

      subscriber.complete();
    }

    filereader.onerror =() => {
      subscriber.error()
      subscriber.complete()
    }
  }
}
