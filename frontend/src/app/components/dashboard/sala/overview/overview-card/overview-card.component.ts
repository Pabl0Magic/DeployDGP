import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
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

  constructor(private salaInfoService: SalaInfoService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.title = this.dataType[0].toUpperCase() + this.dataType.slice(1);
    
    this.salaName = this.route.parent?.snapshot.params.salaName;

    this.salaInfoService.getLatestData(this.salaName, this.dataType).subscribe((data) => {
      this.receivedData = data.data;
    });

    this.dataSubscription = this.salaInfoService.onDataMessage(this.dataType).subscribe((data) => {
      this.receivedData = data;
    });
  }

  ngOnDestroy() {
    this.dataSubscription.unsubscribe();
  }
}
