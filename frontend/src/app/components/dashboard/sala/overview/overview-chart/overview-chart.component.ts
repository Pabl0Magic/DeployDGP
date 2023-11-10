import { AfterViewInit, Component, ElementRef, Input, OnDestroy, OnInit, SimpleChanges, ViewChild } from '@angular/core';
import { Chart } from 'chart.js';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-overview-chart',
  templateUrl: './overview-chart.component.html',
  styleUrls: ['./overview-chart.component.css']
})
export class OverviewChartComponent implements AfterViewInit, OnInit, OnDestroy {
  @ViewChild('canvas') canvas!: ElementRef;
  @Input() dataType: string = 'personas';
  @Input() salaName: string = "";
  chart: any;
  data: number[] = [];
  labels: string[] = [];
  personasData: number[] = [];
  viewInitialized: boolean = false;

  private dataSubscription: any;

  constructor(private salaInfoService: SalaInfoService) {}

  createChart() {
    const gradient = this.canvas.nativeElement.getContext('2d').createLinearGradient(0, 0, 0, 300);
    gradient.addColorStop(0, this.hexToRGBA("#6d28d9", 0.7));
    gradient.addColorStop(1, '#FFFFFF');

    this.chart = new Chart("lineChart", {
      type: 'line',
      data: {
        labels: this.labels, 
	      datasets: [
          {
            label: "Score",
            data: this.data,
            fill: 'origin',
            tension: 0,
            borderColor: '#6d28d9',
            pointBackgroundColor: '#6d28d9',
            backgroundColor: gradient
          }  
        ]
      },
      options: {
        interaction: {
          intersect: false,
          mode: 'index',
        },
        responsive: true,
        aspectRatio: 5,
        plugins: {
          legend: {
            display: false,
          },
          tooltip: {
            backgroundColor: '#fafafa',
            borderColor: '#fafafa',
            borderWidth: 2,
            titleColor: 'black',
            displayColors: false,
            bodyColor: 'black',
            padding: 14,
            caretSize: 0,
            titleFont: {
              size: 17,
              family: 'Inter',
              weight: 'normal'
            },
            bodyFont: {
              size: 13,
              family: 'Inter',
            },
            yAlign: 'bottom'
          }
        },
        scales: {
          x: {
            border: {
              display: false
            },
            ticks: {
              display: true,
              font: {
                family: 'Inter'
              }
            },
            grid: {
              display: true
            },
            title: {
              display: false
            },
            
          },
          y: {
            type: 'linear',
            beginAtZero: true,
            ticks: {
              display: true,
              font: {
                family: 'Inter'
              }
            },
            grid: {
              display: true
            },
          }
        }
      }
    })
  }

  ngOnInit() {
    this.salaInfoService.getLast10Data(this.dataType, this.salaName).subscribe((data: any) => {
      data.data.reverse();
      const ts = data.data.map((entry: any) => {
        const date = new Date(entry.timestamp);
        const hours = date.getHours().toString().padStart(2, '0');
        const minutes = date.getMinutes().toString().padStart(2, '0');
        const seconds = date.getSeconds().toString().padStart(2, '0');
        const formattedTime = `${hours}:${minutes}:${seconds}`;
      
        return {
          value: entry.value,
          formattedTime: formattedTime,
        };
      });

      this.data = ts.map((entry: any) => entry.value) as number[];
      this.labels = ts.map((entry: any) => entry.formattedTime) as string[];

      this.createChart();
    });

    this.dataSubscription = this.salaInfoService.onDataMessage(this.dataType).subscribe((data) => {
      const currentDate = new Date();
      const hours = currentDate.getHours().toString().padStart(2, '0');
      const minutes = currentDate.getMinutes().toString().padStart(2, '0');
      const seconds = currentDate.getSeconds().toString().padStart(2, '0');
      
      this.chart.data.datasets[0].data.push(data);
      this.chart.data.labels.push(`${hours}:${minutes}:${seconds}`);
      console.log(this.salaName)

      this.chart.update();
    });
  }

  ngAfterViewInit() {
    console.log("After view")
    if (this.chart) {
      this.changeGradient();
      this.viewInitialized = true;
    }
  }

  changeGradient() {
    const ctx = this.chart.ctx;
    const gradient = ctx.createLinearGradient(0, 0, 0, 300);
    gradient.addColorStop(0, this.hexToRGBA("#6d28d9", 0.5));
    gradient.addColorStop(1, '#FFFFFF');
    this.chart.data.datasets[0].backgroundColor = gradient;
    this.chart.update();
  }

  hexToRGBA(hex: string, alpha: number): string {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return `rgba(${r}, ${g}, ${b}, ${alpha})`;
  };
  
  ngOnChanges(changes: SimpleChanges) {
    this.chart.destroy();
    this.data = [];
    this.labels = [];
    this.dataSubscription.unsubscribe();

    this.ngOnInit();
    this.changeGradient();
  }

  ngOnDestroy() {
    if (this.chart) this.chart.destroy();
  }
}
