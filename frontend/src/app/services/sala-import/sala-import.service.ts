import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SalaImportService {
  private httpURL = "http://127.0.0.1:8000/project/room/";

  constructor(private http: HttpClient) { }

  uploadFile(file: File) {
    const formData = new FormData();
    formData.append('file', file);

    return this.http.post(this.httpURL + "import/", formData);
  }

  export() {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const options = { headers: headers, responseType: 'blob' as 'json' };

    this.http.get<Blob>(this.httpURL + "export/", options).subscribe((response: Blob) => {
      const blob = new Blob([response], { type: 'text/csv' }); // Set the appropriate file type
      const downloadLink = document.createElement('a');
      
      downloadLink.href = window.URL.createObjectURL(blob);
      downloadLink.download = 'room_data.csv'; // Set the filename here
      document.body.appendChild(downloadLink);
      downloadLink.click();
      document.body.removeChild(downloadLink);
    }, error => {
      console.error('File download error:', error);
    });
  }
}
