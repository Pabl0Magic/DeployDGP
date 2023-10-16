import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { gsap } from 'gsap';

@Component({
  selector: 'app-sala',
  templateUrl: './sala.component.html',
  styleUrls: ['./sala.component.css']
})
export class SalaComponent {
  elements: NodeListOf<HTMLElement> | null = null;
  isReportsActive = true;

  constructor(
    private route: ActivatedRoute
  ) {}

  click() {
    const collectionId = this.route.snapshot.params.salaId;
    console.log(collectionId)
    
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
