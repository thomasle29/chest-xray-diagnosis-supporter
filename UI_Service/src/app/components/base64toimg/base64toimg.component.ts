import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-base64toimg',
  templateUrl: './base64toimg.component.html',
  styleUrls: ['./base64toimg.component.scss']
})
export class Base64toimgComponent implements OnInit {
  valueVariable: string='';
  constructor() { }

  ngOnInit(): void {
  }


changed():any{
  console.log(this.valueVariable);
  const el=document.getElementById('image');
  
  if(el!=null){
    el.setAttribute('src',this.valueVariable );
  }
    
  
}

}
