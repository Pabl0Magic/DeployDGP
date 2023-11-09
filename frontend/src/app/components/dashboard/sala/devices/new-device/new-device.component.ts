import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { DevicesService } from 'src/app/services/devices/devices.service';

@Component({
  selector: 'app-new-device',
  templateUrl: './new-device.component.html',
  styleUrls: ['./new-device.component.css']
})
export class NewDeviceComponent {
  isSubmitting: boolean = false;
  deviceType: string = "";
  deviceForm!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private devicesService: DevicesService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    this.deviceType = this.route.snapshot.params.deviceType;
    
    this.deviceForm = this.formBuilder.group({
      name: ['', Validators.required],
    })
  }

  onSubmit(event: any) {
    if (this.deviceForm.invalid) return;

    this.isSubmitting = true;

    const salaName = this.route.parent?.snapshot.params.salaName;

    return this.devicesService.createDevice(this.deviceType, salaName, this.deviceForm.value).subscribe(
      (data) => console.log(data)
    );
  }
}
