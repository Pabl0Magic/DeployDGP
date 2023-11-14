import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Chart } from 'chart.js';
import { DevicesService } from 'src/app/services/devices/devices.service';

interface Data {
  id: number,
  name: string,
  activities: any[]
}

@Component({
  selector: 'app-devices-chart',
  templateUrl: './devices-chart.component.html',
  styleUrls: ['./devices-chart.component.css']
})
export class DevicesChartComponent implements OnInit {
  salaName: string = "";
  deviceType: string = "";
  deviceId: number = -1;
  chart: any;
  chartId: string = "";
  data!: Data
  labels: string[] = [];
  stepChartData: string[] = [];

  constructor(private devicesService: DevicesService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.salaName = this.route.parent?.snapshot.params.salaName;
    this.deviceType = this.route.snapshot.params.deviceType;
    this.deviceId = this.route.snapshot.params.deviceId;

    this.devicesService.getActivity(this.salaName, this.deviceType, this.deviceId).subscribe((data: any) => this.getActivityCallback(data));
  }

  processData() {
    this.data.activities = this.data.activities.slice(-10);
    this.data.activities.forEach((activity: any) => {
      this.labels.push(activity.timestamp);
      this.stepChartData.push((activity.isOpen || activity.isOn) ? "Abierto" : "Cerrado");
    });
  }


  createChart() {
    this.chart = new Chart('timelineChart', {
      type: 'line',
      data: {
        labels: this.labels,
        datasets: [
          {
            label: 'Cronología',
            data: this.stepChartData,
            fill: 'origin',
            tension: 0,
            borderColor: '#6d28d9',
            pointBackgroundColor: '#6d28d9',
            backgroundColor: '#ffffff',
            stepped: true,
          },
        ],
      },
      options: {
        aspectRatio: 5,
        responsive: true,
        interaction: {
          intersect: false,
          axis: 'x'
        },
        scales: {
          y: {
            type: 'category',
            labels: ['Abierto', 'Cerrado'],
          },
        },
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
        }
      }
    });
  }

  getActivityCallback(data: any) {
    this.data = data;
    this.processData();
    this.labels = this.labels.map(ts => new Date(ts).toLocaleTimeString('en-US', {hour12: false}))
    this.createChart();
  }
}
