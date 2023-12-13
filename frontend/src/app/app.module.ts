import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { SidebarComponent } from './components/dashboard/sidebar/sidebar.component';
import { DatePipe } from '@angular/common';
import { NgChartsModule } from 'ng2-charts';
import { NewSalaComponent } from './components/dashboard/new-sala/new-sala.component';
import { SalaComponent } from './components/dashboard/sala/sala.component';
import { SalaImportComponent } from './components/dashboard/sala/sala-import/sala-import.component';
import { OverviewComponent } from './components/dashboard/sala/overview/overview.component';
import { ModifySalaComponent } from './components/dashboard/modify-sala/modify-sala.component';
import { OverviewCardComponent } from './components/dashboard/sala/overview/overview-card/overview-card.component';
import { RouteReuseStrategy } from '@angular/router';
import { RoomRouteReuseStrategy } from './route-strategy/room-route-reuse-strategy';
import { OverviewChartComponent } from './components/dashboard/sala/overview/overview-chart/overview-chart.component';
import { DevicesComponent } from './components/dashboard/sala/devices/devices.component';
import { DeviceCardComponent } from './components/dashboard/sala/devices/device-card/device-card.component';
import { NewDeviceComponent } from './components/dashboard/sala/devices/new-device/new-device.component';
import { DevicesChartComponent } from './components/dashboard/sala/devices/devices-chart/devices-chart.component';
import { MatDialogModule } from '@angular/material/dialog';
import { ModifyDeviceComponent } from './components/dashboard/sala/devices/modify-device/modify-device.component';
import { AlarmaComponent } from './components/dashboard/sala/overview/alarma/alarma.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    SidebarComponent,
    NewSalaComponent,
    SalaComponent,
    SalaImportComponent,
    OverviewComponent,
    ModifySalaComponent,
    OverviewCardComponent,
    OverviewChartComponent,
    DevicesComponent,
    DeviceCardComponent,
    NewDeviceComponent,
    DevicesChartComponent,
    ModifyDeviceComponent,
    AlarmaComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    NgChartsModule,
    MatDialogModule
    /*RouterModule.forRoot([
      { path: 'collection/:collectionId', component: CollectionNavbarComponent, data: { reuse: true } }
    ])*/
  ],
  providers: [
    { provide: DatePipe, useValue: new DatePipe('en-US') },
    { provide: RouteReuseStrategy, useClass: RoomRouteReuseStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
