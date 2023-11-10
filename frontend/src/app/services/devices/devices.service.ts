import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  private httpURL = "http://127.0.0.1:8000/project/room/";

  constructor(private http: HttpClient) { }

  getAllDoors(salaName: string) {
    return this.http.get(this.httpURL + encodeURI(salaName) + "/door/all/");
  }

  getAllWindows(salaName: string) {
    return this.http.get(this.httpURL + encodeURI(salaName) + "/window/all/");
  }

  getAllLights(salaName: string) {
    return this.http.get(this.httpURL + encodeURI(salaName) + "/light/all/");
  }

  getAllVentilators(salaName: string) {
    return this.http.get(this.httpURL + encodeURI(salaName) + "/ventilator/all/");
  }

  getActivity(salaName: string, deviceType: string, deviceId: number) {
    if (deviceType === 'puerta') return this.http.get(this.httpURL + encodeURI(salaName) + "/door/" + deviceId + "/activity/");
    else return this.http.get(this.httpURL + encodeURI(salaName) + "/window/" + deviceId + "/activity/");
  }

  createDevice(deviceType: string, salaName: string, data: any) {
    const formData = new FormData();
    for (let key in data) formData.append(key, data[key]);
    if (deviceType === 'puerta') formData.append('rooms', salaName);
    else formData.append('room', salaName);

    if (deviceType === 'puerta') return this.http.post(this.httpURL + encodeURI(salaName) + '/door/create/', formData);
    if (deviceType === 'ventana') return this.http.post(this.httpURL + encodeURI(salaName) + '/window/create/', formData);
    if (deviceType === 'luz') return this.http.post(this.httpURL + encodeURI(salaName) + '/light/create/', formData);
    else return this.http.post(this.httpURL + encodeURI(salaName) + '/ventilator/create/', formData);
  }

  deleteDevice(deviceType: string, deviceId: number, salaName: string) {
    if (deviceType === 'puerta') return this.http.delete(this.httpURL + encodeURI(salaName) + '/door/' + deviceId + '/');
    if (deviceType === 'ventana') return this.http.delete(this.httpURL + encodeURI(salaName) + '/window/' + deviceId + '/');
    if (deviceType === 'luz') return this.http.delete(this.httpURL + encodeURI(salaName) + '/light/' + deviceId + '/');
    else return this.http.delete(this.httpURL + encodeURI(salaName) + '/ventilator/' + deviceId + '/');
  }

  switchDevice(deviceType: string, deviceId: number, newValue: boolean, salaName: string) {
    const isOpen = newValue? 'True': 'False';
    console.log("Data about to be sent: " + isOpen)
    const formData = new FormData();
    if (deviceType === 'puerta' || deviceType === 'ventana') formData.append('isOpen', isOpen);
    else formData.append('isOn', isOpen);
    console.log(formData.get('isOpen'))

    if (deviceType === 'puerta') return this.http.post(this.httpURL + encodeURI(salaName) + '/door/' + deviceId + '/addTs/', formData);
    if (deviceType === 'ventana') return this.http.post(this.httpURL + encodeURI(salaName) + '/window/' + deviceId + '/addTs/', formData);
    if (deviceType === 'luz') return this.http.post(this.httpURL + encodeURI(salaName) + '/light/' + deviceId + '/addTs/', formData);
    else return this.http.post(this.httpURL + encodeURI(salaName) + '/ventilator/' + deviceId + '/addTs/', formData);
  }
}
