import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { DevicesService } from 'src/app/services/devices/devices.service';

@Component({
  selector: 'app-modify-device',
  templateUrl: './modify-device.component.html',
  styleUrls: ['./modify-device.component.css']
})
export class ModifyDeviceComponent {
  isSubmitting: boolean = false;
  deviceType: string = "";
  deviceId: number = -1;
  deviceForm!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private devicesService: DevicesService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    this.deviceType = this.route.snapshot.params.deviceType;
    this.deviceId = this.route.snapshot.params.deviceId;
    
    this.deviceForm = this.formBuilder.group({
      name: ['', Validators.required],
    })
  }

  onSubmit(event: any) {
    if (this.deviceForm.invalid) return;

    this.isSubmitting = true;

    const salaName = this.route.parent?.snapshot.params.salaName;

    return this.devicesService.modifyDevice(this.deviceType, this.deviceId, salaName, this.deviceForm.value).subscribe(
      (data) => console.log(data)
    );
  }
}
