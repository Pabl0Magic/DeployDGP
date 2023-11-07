import { Component, OnInit } from '@angular/core';
import { gsap } from 'gsap';
import { SidebarService } from 'src/app/services/sidebar/sidebar.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {  
  elements: NodeListOf<HTMLElement> | null = null;
  salas: string[] = [];

  constructor(private sidebarService: SidebarService) {}

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
}
