import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class NewSalaService {
  private API_URL = "http://127.0.0.1:8000/project/room/create";

  constructor(private http: HttpClient) { }

  createSala(data: any) {
    console.log(data);
    const formData = new FormData();
    for (let key in data) formData.append(key, data[key]);

    return this.http.post<any>(this.API_URL, formData);
  }
}
