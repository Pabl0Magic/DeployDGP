import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription, interval, switchMap } from 'rxjs';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})
export class OverviewComponent {
  dataType: string = "personas";
  salaName: string = "";
  personasSubscription!: Subscription;
  temperaturaSubscription!: Subscription;
  co2Subscription!: Subscription;
  
  constructor(private route: ActivatedRoute, private salaInfoService: SalaInfoService) {}

  ngOnInit() {
    this.salaName = this.route.parent?.snapshot.params.salaName;
  }

  sendData() {
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
}
