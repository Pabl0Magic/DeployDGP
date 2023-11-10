import { Component, EventEmitter, Input, Output } from '@angular/core';
import { DevicesService } from 'src/app/services/devices/devices.service';

@Component({
  selector: 'app-device-card',
  templateUrl: './device-card.component.html',
  styleUrls: ['./device-card.component.css']
})
export class DeviceCardComponent {
  @Input() deviceType: string = "";
  @Input() id: number = 0;
  @Input() name: string = "";
  @Input() isOpen: boolean = false;
  @Input() bloqueada: boolean = false;
  @Input() salaName: string = "";
  @Output() deleted: EventEmitter<{ deviceId: number, deviceType: string }> = new EventEmitter<{ deviceId: number, deviceType: string }>();
  @Output() switched: EventEmitter<{ newIsOpen: boolean, deviceId: number, deviceType: string }> = new EventEmitter<{ newIsOpen: boolean, deviceId: number, deviceType: string }>();
  
  switching: boolean = false;

  currentAction: string = "Abrir";

  constructor(private devicesService: DevicesService) {}

  ngOnInit() {
    this.currentAction = this.isOpen? "Cerrar": "Abrir";
  }

  switchDevice() {
    this.switching = true;
    const newValue = !this.isOpen;
    this.devicesService.switchDevice(this.deviceType, this.id, newValue, this.salaName).subscribe(
      (data: any) => {
        this.isOpen = !this.isOpen;
        console.log("New isOpen = " + this.isOpen)
        if (this.isOpen) this.currentAction = "Cerrar";
        else this.currentAction = "Abrir";
        
        this.switched.emit({newIsOpen: this.isOpen, deviceId: this.id, deviceType: this.deviceType});
        this.switching = false;
      }
    );
  }

  deleteDevice() {
    this.devicesService.deleteDevice(this.deviceType, this.id, this.salaName).subscribe(
      (data: any) => {
        this.deleted.emit({deviceId: this.id, deviceType: this.deviceType});
      }
    );
  }

  isSwitching() {
    return this.isSwitching;
  }
}
