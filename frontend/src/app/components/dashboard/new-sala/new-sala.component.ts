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
      doors: ['', Validators.required],
      windows: ['', Validators.required],
      luz: [true, Validators.required],
      ventilators: [true, Validators.required]
    })
  }

  toggleLuces(lights: boolean) {
    console.log("toggled")
    this.lightsSelected = lights;
  }

  toggleAire(ac: boolean) {
    console.log("toggled")
    this.ventilatorsSelected = ac;
  }

  onSubmit(event: any) {
    if (this.salaForm.invalid) return;

    this.isSubmitting = true;

    this.salaForm.controls['lights'].setValue(this.lightsSelected);
    this.salaForm.controls['ventilators'].setValue(this.ventilatorsSelected);

    this.newSalaService.createSala(this.salaForm.value);
  }
}
