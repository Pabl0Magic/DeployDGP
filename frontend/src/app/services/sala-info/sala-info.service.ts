import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SalaInfoService {
  private API_URL = "";

  constructor(private http: HttpClient) { }

  getPersonas() {}

  getTemperatura() {}

  getCO2() {}
}
