import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription, interval, switchMap } from 'rxjs';
import { DevicesService } from 'src/app/services/devices/devices.service';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})
export class OverviewComponent implements OnInit {
  dataType: string = "personas";
  salaName: string = "";
  personasSubscription!: Subscription;
  temperaturaSubscription!: Subscription;
  co2Subscription!: Subscription;
  enviando: boolean = false;

  showAlarm: boolean = false;

  constructor(private route: ActivatedRoute, 
              private salaInfoService: SalaInfoService,
              private devicesService: DevicesService) {}

  ngOnInit() {
    this.salaName = this.route.parent?.snapshot.params.salaName;
  }

  sendData() {
    this.enviando = true;

    this.personasSubscription = interval(3000).pipe(
      switchMap(() => this.salaInfoService.sendData('personas', this.salaName))
    ).subscribe()

    this.temperaturaSubscription = interval(3000).pipe(
      switchMap(() => this.salaInfoService.sendData('temperatura', this.salaName))
    ).subscribe()

    this.co2Subscription = interval(3000).pipe(
      switchMap(() => this.salaInfoService.sendData('co2', this.salaName))
    ).subscribe()
  }

  pararDatos() {
    this.enviando = false;

    if (this.personasSubscription) this.personasSubscription.unsubscribe();
    if (this.temperaturaSubscription) this.temperaturaSubscription.unsubscribe();
    if (this.co2Subscription) this.co2Subscription.unsubscribe();
  }

  changeDataType(dataType: string) {
    this.dataType = dataType;
  }

  ngOnDestroy() {
    if (this.personasSubscription) this.personasSubscription.unsubscribe();
    if (this.temperaturaSubscription) this.temperaturaSubscription.unsubscribe();
    if (this.co2Subscription) this.co2Subscription.unsubscribe();
  }

  handleShowAlarm(value: boolean) {
    this.showAlarm = value;

    this.salaName = this.route.parent?.snapshot.params.salaName;
    console.log(this.salaName)

    this.devicesService.getAllDoors(this.salaName).subscribe(
      (data: any) => {
        data.forEach((puerta: any) => {
          if (puerta.isOpen)
            this.devicesService.switchDevice("puerta", puerta.id, false, this.salaName).subscribe();
        });
      }
    );
  }

  handleSwitchLights(value: boolean) {
    if (value) {
      console.log(value)
      this.devicesService.getAllLights(this.salaName).subscribe(
        (data: any) => {
          data.forEach((luz: any) => {
            if (!luz.isOn)
              this.devicesService.switchDevice("luz", luz.id, true, this.salaName).subscribe();
          });
        }
      );
    } else {
      this.devicesService.getAllLights(this.salaName).subscribe(
        (data: any) => {
          data.forEach((luz: any) => {
            if (luz.isOn)
              this.devicesService.switchDevice("luz", luz.id, false, this.salaName).subscribe();
          });
        }
      );

      this.devicesService.getAllVentilators(this.salaName).subscribe(
        (data: any) => {
          data.forEach((ventilador: any) => {
            if (ventilador.isOn)
              this.devicesService.switchDevice("ventilador", ventilador.id, false, this.salaName).subscribe();
          });
        }
      );
    }
  }

  handleVentilate(value: boolean) {
    if (value) {
      this.devicesService.getAllWindows(this.salaName).subscribe(
        (data: any) => {
          data.forEach((ventana: any) => {
            if (!ventana.isOpen)
              this.devicesService.switchDevice("ventana", ventana.id, true, this.salaName).subscribe();
          });
        }
      );

      this.devicesService.getAllVentilators(this.salaName).subscribe(
        (data: any) => {
          data.forEach((ventilator: any) => {
            if (!ventilator.isOn)
              this.devicesService.switchDevice("ventilador", ventilator.id, true, this.salaName).subscribe();
          });
        }
      );
    }
  }
}
