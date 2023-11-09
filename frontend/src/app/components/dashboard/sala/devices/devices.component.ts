import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DevicesService } from 'src/app/services/devices/devices.service';

@Component({
  selector: 'app-devices',
  templateUrl: './devices.component.html',
  styleUrls: ['./devices.component.css']
})
export class DevicesComponent implements OnInit {
  salaName: string = "";
  puertas: any[] = [];
  ventanas: any[] = [];
  luces: any[] = [];
  ventiladores: any[] = [];

  constructor(private devicesService: DevicesService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.salaName = this.route.parent?.snapshot.params.salaName;

    this.devicesService.getAllDoors(this.salaName).subscribe(
      (data: any) => {
        console.log(data);
        this.puertas = data;
      }
    );
    this.devicesService.getAllWindows(this.salaName).subscribe(
      (data: any) => {
        console.log(data);
        this.ventanas = data;
      }
    );
    // Luces
    // Ventiladores
  }

  onDeviceDeleted(eventData: { deviceId: number, deviceType: string }) {
    if (eventData.deviceType === 'puerta') this.puertas = this.puertas.filter(puerta => puerta.id !== eventData.deviceId);
    else if (eventData.deviceType === 'ventana') this.ventanas = this.ventanas.filter(ventana => ventana.id !== eventData.deviceId);
    else if (eventData.deviceType === 'luz') this.luces = this.luces.filter(luz => luz.id !== eventData.deviceId);
    else this.ventiladores = this.ventiladores.filter(ventilador => ventilador.id !== eventData.deviceId);
  }

  onDeviceSwitched(eventData: { newIsOpen: boolean, deviceId: number, deviceType: string }) {
    if (eventData.deviceType === 'puerta') {
      let puerta = this.puertas.find(puerta => puerta.id === eventData.deviceId);
      puerta.isOpen = eventData.newIsOpen;
    }

    else if (eventData.deviceType === 'ventana') {
      let ventana = this.ventanas.find(ventana => ventana.id === eventData.deviceId);
      ventana.isOpen = eventData.newIsOpen;
    }

    else if (eventData.deviceType === 'luz') {
      let luz = this.luces.find(luz => luz.id === eventData.deviceId);
      luz.isOpen = eventData.newIsOpen;
    }

    else {
      let ventilador = this.ventiladores.find(ventilador => ventilador.id === eventData.deviceId);
      ventilador.isOpen = eventData.newIsOpen;
    }
  }
}
