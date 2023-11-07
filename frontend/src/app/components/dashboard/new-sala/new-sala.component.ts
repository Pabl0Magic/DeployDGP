import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NewSalaService } from 'src/app/services/new-sala/new-sala.service';

@Component({
  selector: 'app-new-sala',
  templateUrl: './new-sala.component.html',
  styleUrls: ['./new-sala.component.css']
})
export class NewSalaComponent implements OnInit {
  lightsSelected: boolean = true;
  ventilatorsSelected: boolean = true;
  salaForm!: FormGroup;
  isSubmitting: boolean = false;

  constructor(
    private formBuilder: FormBuilder,
    private newSalaService: NewSalaService
  ) {}

  ngOnInit() {
    this.salaForm = this.formBuilder.group({
      name: ['', Validators.required],
      size: ['', Validators.required],
    })
  }

  toggleLuces(lights: boolean) {
    this.lightsSelected = lights;
  }

  toggleAire(ac: boolean) {
    this.ventilatorsSelected = ac;
  }

  onSubmit(event: any) {
    if (this.salaForm.invalid) return;

    this.isSubmitting = true;

    this.newSalaService.createSala(this.salaForm.value).subscribe((data) => console.log(data));
  }
}
