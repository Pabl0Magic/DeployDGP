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
  @Input() salaName: string = "";
  chart: any;
  data: number[] = [];
  labels: string[] = [];
  personasData: number[] = [];
  viewInitialized: boolean = false;

  private dataSubscription: any;

  constructor(private salaInfoService: SalaInfoService) {}

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
      

      this.chart.update();
    });
  }

  ngAfterViewInit() {
    if (this.chart) {
      this.viewInitialized = true;
    }
  }
  
  ngOnChanges(changes: SimpleChanges) {
    console.log(changes.dataType + "-" + this.dataType)

    this.chart.destroy();
    this.data = [];
    this.labels = [];
    this.dataSubscription.unsubscribe();

    this.ngOnInit();
  }

  ngOnDestroy() {
    this.chart.destroy();
  }
}
