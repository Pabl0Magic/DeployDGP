import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Subject, interval, switchMap } from 'rxjs';

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

  sendData(type: string) {
    if (type === 'personas') {
      return interval(3000).pipe(
        switchMap(() => {
          const formData = new FormData();
          const personas = Math.floor(Math.random() * 11);
          formData.append('people', String(personas));
          return this.http.post(this.httpURL + 'people/add/', formData)
        })
      );
    }
    if (type === 'temperatura') {
      return interval(3000).pipe(
        switchMap(() => {
          const formData = new FormData();
          const temperatura = Math.floor(Math.random() * 16) + 10;
          formData.append('temperature', String(temperatura));
          return this.http.post(this.httpURL + 'temperature/add/', formData)
        })
      );
    }
    else {
      return interval(3000).pipe(
        switchMap(() => {
          const formData = new FormData();
          const co2 = Math.floor(Math.random() * 201) + 600;
          formData.append('co2', String(co2));
          return this.http.post(this.httpURL + 'co2/add/', formData)
        })
      );
    }
  }
}
