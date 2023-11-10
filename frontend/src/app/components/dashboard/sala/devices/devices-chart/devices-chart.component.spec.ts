import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DevicesChartComponent } from './devices-chart.component';

describe('DevicesChartComponent', () => {
  let component: DevicesChartComponent;
  let fixture: ComponentFixture<DevicesChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DevicesChartComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DevicesChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
