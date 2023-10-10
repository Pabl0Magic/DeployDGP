import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SalaImportComponent } from './sala-import.component';

describe('SalaImportComponent', () => {
  let component: SalaImportComponent;
  let fixture: ComponentFixture<SalaImportComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SalaImportComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SalaImportComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
