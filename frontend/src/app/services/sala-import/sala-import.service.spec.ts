import { TestBed } from '@angular/core/testing';

import { SalaImportService } from './sala-import.service';

describe('SalaImportService', () => {
  let service: SalaImportService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SalaImportService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
