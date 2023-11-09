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
  
  currentAction: string = "Abrir";

  constructor(private devicesService: DevicesService) {}

  ngOnInit() {
    this.currentAction = this.isOpen? "Cerrar": "Abrir";
  }

  switchDevice() {
    const newValue = !this.isOpen;
    this.devicesService.switchDevice(this.deviceType, this.id, newValue, this.salaName).subscribe(
      (data: any) => {
        this.isOpen = !this.isOpen;
        if (this.isOpen) this.currentAction = "Cerrar";
        else this.currentAction = "Abrir";
      }
    );
  }

  deleteDevice() {
    this.devicesService.deleteDevice(this.deviceType, this.id, this.salaName).subscribe(
      (data: any) => {
        console.log(data);
        this.deleted.emit({deviceId: this.id, deviceType: this.deviceType});
      }
    );
  }
}
