import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})
export class OverviewComponent {
  constructor(
    private route: ActivatedRoute
  ) {}

  click() {
    const collectionId = this.route.snapshot.params.salaId;
    console.log(collectionId)
  }
}
