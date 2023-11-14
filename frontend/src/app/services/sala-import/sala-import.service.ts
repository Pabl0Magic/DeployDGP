import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SalaImportService {
  private API_URL = "";

  constructor(private http: HttpClient) { }

  uploadFile(file: File) {
    console.log(file);
    const formData = new FormData();
    formData.append('file', file);


  }
}
