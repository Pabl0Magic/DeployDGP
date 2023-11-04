import { AfterViewInit, Component, Input, OnDestroy, OnInit, SimpleChanges } from '@angular/core';
import { Chart } from 'chart.js';
import { SalaInfoService } from 'src/app/services/sala-info/sala-info.service';

@Component({
  selector: 'app-overview-chart',
  templateUrl: './overview-chart.component.html',
  styleUrls: ['./overview-chart.component.css']
})
export class OverviewChartComponent implements AfterViewInit, OnInit, OnDestroy {
  @Input() dataType: string = 'personas';
  chart: any;
  labels: string[];
  data: number[];
  personasData: number[] = [];
  viewInitialized: boolean = false;

  private dataSubscription: any;

  constructor(private salaInfoService: SalaInfoService) {
    this.data = [7, 2, 5, 10, 3, 0, 8, 4, 9, 1];
    this.labels = Array.from({ length: 10 }, () => {
      const date = new Date();
      return `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
    });
  }

  createChart() {
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
            pointBackgroundColor: '#6d28d9'
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
    this.createChart();

    this.dataSubscription = this.salaInfoService.onDataMessage(this.dataType).subscribe((data) => {
      const currentDate = new Date();
      const hours = currentDate.getHours().toString().padStart(2, '0'); // Get hours and ensure 2-digit format
      const minutes = currentDate.getMinutes().toString().padStart(2, '0'); // Get minutes and ensure 2-digit format

      this.chart.data.datasets[0].data.push(data);
      this.chart.data.labels.push(`${hours}:${minutes}`);
      this.chart.update();
    });
  }

  ngAfterViewInit() {
    if (this.chart) {
      this.viewInitialized = true;
    }
  }
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes.dataType && this.viewInitialized) {
      this.chart.destroy();
      if (this.dataType == 'personas') {
        this.data = [7, 2, 5, 10, 3, 0, 8, 4, 9, 1];
        this.labels = Array.from({ length: 10 }, () => {
          const date = new Date();
          return `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
        });
      } else if (this.dataType == 'temperatura') {
        this.data = [15, 16, 16, 17, 17, 19, 20, 17, 20, 22];
        this.labels = Array.from({ length: 10 }, () => {
          const date = new Date();
          return `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
        });
      } else {
        this.data = [612, 743, 678, 721, 656, 799, 601, 703, 775, 689];
        this.labels = Array.from({ length: 10 }, () => {
          const date = new Date();
          return `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
        });
      }
      
      this.dataSubscription.unsubscribe();

      this.ngOnInit();
    }
  }

  ngOnDestroy() {
    this.chart.destroy();
  }
}
