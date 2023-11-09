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
            path: 'modify-sala',
            component: ModifySalaComponent
          },
          {
            path: 'new-device/:deviceType',
            component: NewDeviceComponent
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
