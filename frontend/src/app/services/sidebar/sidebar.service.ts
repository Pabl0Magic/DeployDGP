import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SidebarService {
  private httpURL: string = "http://127.0.0.1:8000/project/room/";

  constructor(private http: HttpClient) { }

  getAllSalas() {
    return this.http.get(this.httpURL + "all/");
  }
}
