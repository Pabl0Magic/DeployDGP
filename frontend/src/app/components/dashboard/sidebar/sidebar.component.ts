import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { gsap } from 'gsap';
import { SidebarService } from 'src/app/services/sidebar/sidebar.service';
import { SalaImportComponent } from '../sala/sala-import/sala-import.component';
import { SalaImportService } from 'src/app/services/sala-import/sala-import.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  elements: NodeListOf<HTMLElement> | null = null;
  salas: string[] = [];
  selectedSala: string = "";

  constructor(private sidebarService: SidebarService, private salaImportService: SalaImportService) {}

  ngOnInit() {
    this.sidebarService.getAllSalas().subscribe((data: any) => {
      this.salas = data.map((room: any) => room.name);
    });
  }

  animateClick() {    
    this.elements = document.querySelectorAll('.dashboard');

    gsap.fromTo(this.elements, {
      y: 0,
      opacity: 0
    }, {
      y: 0,
      opacity: 1,
      duration: 2,
      ease: 'power4.out',
    });
  }

  changeSalaSelected(salaName: string) {
    this.selectedSala = salaName;
  }

  export() {
    this.salaImportService.export();
  }
}
