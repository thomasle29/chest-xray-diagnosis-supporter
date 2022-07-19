import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

import { FlexLayoutModule } from '@angular/flex-layout';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import {MatIconModule} from '@angular/material/icon';
import {MatToolbarModule} from '@angular/material/toolbar';

import { ConvertimgComponent } from './components/convertimg/convertimg.component';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { Base64toimgComponent } from 'src/app/components/base64toimg/base64toimg.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from 'src/app/components/footer/footer.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { SideMenuComponent } from './components/side-menu/side-menu.component';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatListModule} from '@angular/material/list';
import { UserHeaderComponent } from './components/user-header/user-header.component';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ConvertimgComponent,
    Base64toimgComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    SideMenuComponent,
    UserHeaderComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FlexLayoutModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule,
    MatIconModule,
    MatToolbarModule,
    //img
    FormsModule,
    ReactiveFormsModule,
    MatGridListModule,
    MatSidenavModule,
    MatListModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
