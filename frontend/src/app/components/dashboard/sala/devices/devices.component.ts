import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
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

  constructor(private devicesService: DevicesService, private route: ActivatedRoute, public dialog: MatDialog) {}

  ngOnInit() {
    this.salaName = this.route.parent?.snapshot.params.salaName;

    this.devicesService.getAllDoors(this.salaName).subscribe(
      (data: any) => {
        this.puertas = data;
      }
    );
    this.devicesService.getAllWindows(this.salaName).subscribe(
      (data: any) => {
        this.ventanas = data;
      }
    );
    this.devicesService.getAllLights(this.salaName).subscribe(
      (data: any) => {
        this.luces = data;
      }
    );
    this.devicesService.getAllVentilators(this.salaName).subscribe(
      (data: any) => {
        this.ventiladores = data;
      }
    );
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
      console.log("Looking for luz")
      let luz = this.luces.find(luz => luz.id === eventData.deviceId);
      console.log(luz.id)
      luz.isOn = eventData.newIsOpen;
    }

    else {
      let ventilador = this.ventiladores.find(ventilador => ventilador.id === eventData.deviceId);
      ventilador.isOn = eventData.newIsOpen;
    }
  }
}
