import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { MatIcon } from '@angular/material/icon';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  hide = true;
  public userForm: FormGroup;
  constructor(private fb: FormBuilder, private _router:Router) {
    localStorage.clear();
    // Form element defined below
    this.userForm = this.fb.group({
      name: '',
      password:''


    }
    
    );
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
