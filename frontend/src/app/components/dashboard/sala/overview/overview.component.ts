import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})
export class OverviewComponent {
  dataType: string = "personas";
  
  constructor() {}

  changeDataType(dataType: string) {
    this.dataType = dataType;
  }
}
