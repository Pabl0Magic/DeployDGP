import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';
import { SalaInfoService } from '../services/sala-info/sala-info.service';

@Injectable({
  providedIn: 'root'
})
export class OverviewResolver {
  constructor(private salaInfoService: SalaInfoService) {}

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<any> {
    const salaName = route.parent?.params.salaName;
    return this.salaInfoService.getSala(salaName);
  }
}
