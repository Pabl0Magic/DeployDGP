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
import { NewSalaComponent } from './components/dashboard/sala/new-sala/new-sala.component';
import { SalaComponent } from './components/dashboard/sala/sala.component';
import { SalaImportComponent } from './components/dashboard/sala/sala-import/sala-import.component';
import { OverviewComponent } from './components/dashboard/sala/overview/overview.component';
import { ModifySalaComponent } from './components/dashboard/sala/modify-sala/modify-sala.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    SidebarComponent,
    NewSalaComponent,
    SalaComponent,
    SalaImportComponent,
    OverviewComponent,
    ModifySalaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    NgChartsModule,
    /*RouterModule.forRoot([
      { path: 'collection/:collectionId', component: CollectionNavbarComponent, data: { reuse: true } }
    ])*/
  ],
  providers: [
    { provide: DatePipe, useValue: new DatePipe('en-US') },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
