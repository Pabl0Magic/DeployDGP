import { TestBed } from '@angular/core/testing';

import { SalaInfoService } from './sala-info/sala-info.service';

describe('SalaInfoService', () => {
  let service: SalaInfoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SalaInfoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
