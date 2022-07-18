import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JsonConvert } from 'json2typescript';
import { map } from 'rxjs/operators';
import { Response } from '../response.model';
import { LoginInfo } from './login.model';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class LoginService {
    private jsonConvert: JsonConvert = new JsonConvert();

    constructor(
      private http: HttpClient
    ) { }

    login(
        userName: string, 
        passWord: string, 
        ): Observable<Response<LoginInfo[]>>{
        return this.http.post<Response<LoginInfo[]>>(
            `${environment.BASE_URL}/submit`,
            {
                "user_name": userName,
                "user_pass": passWord
            }
            ).pipe(map(resp => {
                if (resp.returncode !== 1) {
                    return resp;
                }
                if (resp.data) {
                    resp.data = resp.data.map(item => this.jsonConvert.deserializeObject(item, LoginInfo));
                }
                return resp;
            }));
    }
}