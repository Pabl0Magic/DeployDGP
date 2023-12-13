import { Component, EventEmitter, Input, OnDestroy, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DevicesService } from 'src/app/services/devices/devices.service';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-overview-card',
  templateUrl: './overview-card.component.html',
  styleUrls: ['./overview-card.component.css']
})
export class OverviewCardComponent implements OnInit, OnDestroy {
  @Input() dataType: string = "";
  @Input() salaName: string = "";
  @Input() unit: string = "";
  title: string = "";

  receivedData: any;
  private dataSubscription: any;

  @Output() showAlarm: EventEmitter<boolean> = new EventEmitter<boolean>(false);
  @Output() switchLights: EventEmitter<boolean> = new EventEmitter<boolean>(false);
  @Output() ventilate: EventEmitter<boolean> = new EventEmitter<boolean>(false);

  constructor(private salaInfoService: SalaInfoService, private route: ActivatedRoute, private devicesService: DevicesService) {}

  ngOnInit() {
    this.title = this.dataType[0].toUpperCase() + this.dataType.slice(1);

    this.salaName = this.route.parent?.snapshot.params.salaName;

    this.salaInfoService.getLatestData(this.salaName, this.dataType).subscribe((data) => {
      this.receivedData = data.data;
    });

    this.dataSubscription = this.salaInfoService.onDataMessage(this.dataType).subscribe((data) => {
      this.receivedData = data;

      if (this.dataType == 'temperatura' && data >= 70)
        this.showAlarm.emit(true);
      else
        this.showAlarm.emit(false);

      if (this.dataType == 'personas' && data == 0)
        this.switchLights.emit(false);
      else
        this.switchLights.emit(true);
      
      if (this.dataType == 'CO2' && data > 1000) {
        this.ventilate.emit(true);
        this.salaInfoService.changeColor('red');
      } else {
        this.ventilate.emit(false);
        
        if (data > 800)
          this.salaInfoService.changeColor('yellow');
        else
          this.salaInfoService.changeColor('green');
      }
    });
  }

  ngOnDestroy() {
    this.dataSubscription.unsubscribe();
  }
}
