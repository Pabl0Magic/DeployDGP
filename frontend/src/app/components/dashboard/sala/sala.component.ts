import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { gsap } from 'gsap';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-sala',
  templateUrl: './sala.component.html',
  styleUrls: ['./sala.component.css']
})
export class SalaComponent {
  elements: NodeListOf<HTMLElement> | null = null;
  isReportsActive = true;
  name: string = "";
  size: number = 0;

  constructor(private route: ActivatedRoute, private salaInfoService: SalaInfoService) {}

  ngOnInit() {
    console.log("Sala reloaded")
    const salaName = this.route.snapshot.params.salaName;
    this.salaInfoService.getSala(salaName).subscribe((data: any) => {
      this.name = data.name;
      this.size = data.size;
    });
  }

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
