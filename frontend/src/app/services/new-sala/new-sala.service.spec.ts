import { TestBed } from '@angular/core/testing';

import { NewSalaService } from './new-sala.service';

describe('NewSalaService', () => {
  let service: NewSalaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(NewSalaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
