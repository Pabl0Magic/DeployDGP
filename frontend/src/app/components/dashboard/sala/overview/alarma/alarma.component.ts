import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-alarma',
  templateUrl: './alarma.component.html',
  styleUrls: ['./alarma.component.css']
})
export class AlarmaComponent {
  @Input() show: boolean = false;
}
