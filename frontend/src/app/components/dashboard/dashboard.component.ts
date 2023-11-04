import { Component, OnInit } from '@angular/core';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  elements: NodeListOf<HTMLElement> | null = null;

  constructor(private salaInfoService: SalaInfoService) {}

  ngOnInit() {
    this.salaInfoService.sendData('personas').subscribe((data) => console.log(data));
    this.salaInfoService.sendData('temperatura').subscribe((data) => console.log(data));
    this.salaInfoService.sendData('co2').subscribe((data) => console.log(data));
  }
}