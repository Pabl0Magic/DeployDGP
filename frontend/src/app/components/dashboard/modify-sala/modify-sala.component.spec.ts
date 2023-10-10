import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModifySalaComponent } from './modify-sala.component';

describe('ModifySalaComponent', () => {
  let component: ModifySalaComponent;
  let fixture: ComponentFixture<ModifySalaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ModifySalaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ModifySalaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
