import { Component, OnInit } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';

@Component({
  selector: 'app-convertimg',
  templateUrl: './convertimg.component.html',
  styleUrls: ['./convertimg.component.scss']
})
export class ConvertimgComponent implements OnInit {
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

    this.convertToBase64(file);
  }

  convertToBase64(file: File) {
    const observable = new Observable((subscriber: Subscriber<any>) => {
      this.readFile(file, subscriber)
    })

    observable.subscribe((d)=>{
        console.log(d)
        this.myImage = d
        this.base64code = d
    })
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
