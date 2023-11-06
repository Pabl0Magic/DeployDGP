import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { gsap } from 'gsap';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-sala',
  templateUrl: './sala.component.html',
  styleUrls: ['./sala.component.css']
})
export class SalaComponent implements OnInit {
  elements: NodeListOf<HTMLElement> | null = null;
  isReportsActive = true;
  size: number = 0;

  constructor(private route: ActivatedRoute, private salaInfoService: SalaInfoService) {}

  ngOnInit() {
    const salaName = this.route.snapshot.params.salaName;
    this.salaInfoService.getSala(salaName).subscribe((data: any) => this.size = data.size);
  }

  click() {
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
