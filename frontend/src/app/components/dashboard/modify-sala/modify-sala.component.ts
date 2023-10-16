import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NewSalaService } from 'src/app/services/new-sala/new-sala.service';

@Component({
  selector: 'app-modify-sala',
  templateUrl: './modify-sala.component.html',
  styleUrls: ['./modify-sala.component.css']
})
export class ModifySalaComponent {
  lightsSelected: boolean = true;
  acSelected: boolean = true;
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
      doors: ['', Validators.required],
      windows: ['', Validators.required],
      lights: [true, Validators.required],
      ac: [true, Validators.required]
    })
  }

  toggleLuces(lights: boolean) {
    console.log("toggled")
    this.lightsSelected = lights;
  }

  toggleAire(ac: boolean) {
    console.log("toggled")
    this.acSelected = ac;
  }

  onSubmit(event: any) {
    if (this.salaForm.invalid) return;

    this.isSubmitting = true;

    this.salaForm.controls['lights'].setValue(this.lightsSelected);
    this.salaForm.controls['ac'].setValue(this.acSelected);

    this.newSalaService.createSala(this.salaForm.value);
  }
}
