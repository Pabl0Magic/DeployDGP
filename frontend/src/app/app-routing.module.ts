import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { NewSalaComponent } from './components/dashboard/new-sala/new-sala.component';
import { SalaImportComponent } from './components/dashboard/sala/sala-import/sala-import.component';
import { OverviewComponent } from './components/dashboard/sala/overview/overview.component';
import { ModifySalaComponent } from './components/dashboard/modify-sala/modify-sala.component';
import { SalaComponent } from './components/dashboard/sala/sala.component';
import { DevicesComponent } from './components/dashboard/sala/devices/devices.component';
import { NewDeviceComponent } from './components/dashboard/sala/devices/new-device/new-device.component';
import { DevicesChartComponent } from './components/dashboard/sala/devices/devices-chart/devices-chart.component';
import { ModifyDeviceComponent } from './components/dashboard/sala/devices/modify-device/modify-device.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { 
    path: 'dashboard', 
    component: DashboardComponent, 
    children: [
      {
        path: '',
        component: NewSalaComponent
      },
      {
        path: 'new-sala',
        component: NewSalaComponent
      },
      {
        path: 'sala-import',
        component: SalaImportComponent
      },
      {
        path: 'sala/:salaName',
        component: SalaComponent,
        children: [
          {
            path: 'overview',
            component: OverviewComponent,
          },
          {
            path: 'devices',
            component: DevicesComponent
          },
          {
            path: 'device-chart/:deviceType/:deviceId',
            component: DevicesChartComponent
          },
          {
            path: 'modify-sala',
            component: ModifySalaComponent
          },
          {
            path: 'new-device/:deviceType',
            component: NewDeviceComponent
          },
          {
            path: 'modify-device/:deviceType/:deviceId',
            component: ModifyDeviceComponent
          }
        ]
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
