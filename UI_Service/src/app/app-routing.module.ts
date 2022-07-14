import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from 'src/app/components/login/login.component';
import { HomeComponent } from './components/home/home.component';

const routes: Routes = [
  // link component được đưa lên theo thứ tự
  //chỉ xuất hiện lên component đầu tiên
  //nếu không đưa component vào cái này, có thể để
  // thành tag đưa vào app.component.html
  // {path:'', component:LoginComponent},
  //  {path:'', component:ConvertimgComponent},
   {
    path:':user',
    component:HomeComponent
   },
   //mac dinh la trang LOGIN
   {
    path:'',
    component:LoginComponent
   },
   
   
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
