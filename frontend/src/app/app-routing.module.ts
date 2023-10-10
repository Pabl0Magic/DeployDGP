import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { NewSalaComponent } from './components/dashboard/sala/new-sala/new-sala.component';
import { SalaComponent } from './components/dashboard/sala/sala.component';
import { SalaImportComponent } from './components/dashboard/sala/sala-import/sala-import.component';
import { OverviewComponent } from './components/dashboard/sala/overview/overview.component';
import { ModifySalaComponent } from './components/dashboard/sala/modify-sala/modify-sala.component';

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
        path: ':salaId/modify-sala',
        component: ModifySalaComponent
      },
      {
        path: ':salaId/overview',
        component: OverviewComponent,
        children: [
          {
            path: 'modify-sala',
            component: ModifySalaComponent
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
