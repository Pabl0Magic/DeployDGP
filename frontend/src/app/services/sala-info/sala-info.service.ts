import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SalaInfoService {
  private httpURL = "http://127.0.0.1:8000/project/room/Sala12/";
  private websockets: { [key: string]: WebSocket } = {};
  private subjects: { [key: string]: Subject<any> } = {};

  constructor(private http: HttpClient) {
    this.websockets.wsPersonas = new WebSocket("ws://127.0.0.1:8000/ws/room/people/Sala12/");
    this.websockets.wsTemperatura = new WebSocket("ws://127.0.0.1:8000/ws/room/temperature/Sala12/");
    this.websockets.wsCO2 = new WebSocket("ws://127.0.0.1:8000/ws/room/co2/Sala12/");

    this.subjects.personasSubject = new Subject<any>();
    this.subjects.temperaturaSubject = new Subject<any>();
    this.subjects.co2Subject = new Subject<any>();

    this.websockets.wsPersonas.onmessage = (event) => this.subjects.personasSubject.next(event.data);
    this.websockets.wsTemperatura.onmessage = (event) => this.subjects.temperaturaSubject.next(event.data);
    this.websockets.wsCO2.onmessage = (event) => this.subjects.co2Subject.next(event.data);
  }

  onDataMessage(type: string) {
    if (type === 'personas') return this.subjects.personasSubject.asObservable();
    if (type === 'temperatura') return this.subjects.temperaturaSubject.asObservable();
    else return this.subjects.co2Subject.asObservable();
  }

  getLatestData(type: string) {
    if (type === 'personas') return this.http.get<any>(this.httpURL + 'people/');
    if (type === 'temperatura') return this.http.get<any>(this.httpURL + 'temperature/');
    else return this.http.get<any>(this.httpURL + 'co2/');
  }
}
