import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-user-header',
  templateUrl: './user-header.component.html',
  styleUrls: ['./user-header.component.scss']
})
export class UserHeaderComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  onChange = ($event: Event) => {
    const target = $event.target as HTMLInputElement;

    const file: File = (target.files as FileList)[0];

    console.log(file);//in ra ten hinh anh da chon

    // this.convertToBase64(file);
  }
  handleCLick=()=>{
    this.onChange;
  }

}
