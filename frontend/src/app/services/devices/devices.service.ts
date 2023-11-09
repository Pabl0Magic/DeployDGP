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
    const formData = new FormData();
    if (deviceType === 'puerta' || deviceType === 'ventana') formData.append('isOpen', String(newValue));
    else formData.append('isOn', String(newValue));

    if (deviceType === 'puerta') return this.http.patch(this.httpURL + encodeURI(salaName) + '/door/' + deviceId + '/', formData);
    if (deviceType === 'ventana') return this.http.patch(this.httpURL + encodeURI(salaName) + '/window/' + deviceId + '/', formData);
    if (deviceType === 'luz') return this.http.patch(this.httpURL + encodeURI(salaName) + '/light/' + deviceId + '/', formData);
    else return this.http.patch(this.httpURL + encodeURI(salaName) + '/ventilator/' + deviceId + '/', formData);
  }
}
