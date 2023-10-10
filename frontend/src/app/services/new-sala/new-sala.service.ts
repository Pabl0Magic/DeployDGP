import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class NewSalaService {
  private API_URL = "";

  constructor(private http: HttpClient) { }

  createSala(data: any) {
    console.log(data);
    const formData = new FormData();
    for (let key in data) {
      formData.append(key, data[key]);
    }

    
  }
}
