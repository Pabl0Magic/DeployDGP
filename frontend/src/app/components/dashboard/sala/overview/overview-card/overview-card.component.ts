import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-overview-card',
  templateUrl: './overview-card.component.html',
  styleUrls: ['./overview-card.component.css']
})
export class OverviewCardComponent implements OnInit {
  @Input() dataType: string = "personas";
  title: string = "";
  value: number = 0;

  ngOnInit() {
    this.title = this.dataType[0].toUpperCase() + this.dataType.slice(1);
  }
}
