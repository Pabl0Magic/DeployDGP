import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { SalaImportService } from 'src/app/services/sala-import/sala-import.service';

@Component({
  selector: 'app-sala-import',
  templateUrl: './sala-import.component.html',
  styleUrls: ['./sala-import.component.css']
})
export class SalaImportComponent implements OnInit {
  reportFile!: File;
  fileForm!: FormGroup;
  fileName: string = "";
  isSubmitting: boolean = false;

  constructor(
    private formBuilder: FormBuilder,
    private salaImportService: SalaImportService
  ) {}

  ngOnInit(): void {
    this.fileForm = this.formBuilder.group({
      file: ['', Validators.required]
    });
  }

  onFileChange(event: any) {
    this.reportFile = event.target.files[0];
    this.fileName = this.reportFile.name;
  }

  onSubmit(event: any) {
    if (this.fileForm.invalid) return;

    this.isSubmitting = true;

    const fileInput = event.target.elements.fileInput.files[0];

    this.salaImportService.uploadFile(fileInput).subscribe({
      next: () => {
        console.log("downloaded")
      },
      error: () => {
        alert("Datos duplicados")
      }
    });
  }
}
