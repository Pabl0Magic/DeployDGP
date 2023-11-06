import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})
export class OverviewComponent implements OnInit {
  dataType: string = "personas";
  salaName: string = "";
  
  constructor(private route: ActivatedRoute, private salaInfoService: SalaInfoService) {}

  ngOnInit() {
    this.salaName = this.route.parent?.snapshot.params.salaName;

    this.salaInfoService.sendData('personas', this.salaName).subscribe();
    this.salaInfoService.sendData('temperatura', this.salaName).subscribe();
    this.salaInfoService.sendData('co2', this.salaName).subscribe();
  }

  changeDataType(dataType: string) {
    this.dataType = dataType;
  }
}
