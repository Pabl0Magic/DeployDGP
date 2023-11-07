import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
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
    private newSalaService: NewSalaService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    this.salaForm = this.formBuilder.group({
      name: ['', Validators.required],
      size: ['', Validators.required]
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

  deleteSala() {
    const salaName = this.route.parent?.snapshot.params.salaName;
    this.newSalaService.deleteSala(salaName).subscribe((data) => data);
  }

  onSubmit(event: any) {
    if (this.salaForm.invalid) return;

    this.isSubmitting = true;

    const salaName = this.route.parent?.snapshot.params.salaName;

    this.newSalaService.modifySala(salaName, this.salaForm.value);
  }
}
