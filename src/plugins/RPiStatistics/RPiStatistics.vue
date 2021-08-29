<style scoped>
.content {
	position: relative;
	min-height: 480px;
}
.content > canvas {
	position: absolute;
}
.v-progress-circular {
  margin: 1rem;
}

.margin-initial {
  margin: initial;
}
</style>

<template>
  <div>
    <v-container class="lighten-5 margin-initial">
      <v-row  class="justify-start" no-gutters>
        <v-col cols="3" sm="6" md="3" class="d-flex">
        <!-- <v-col cols="md-lg-4" class="d-flex"> -->
          <v-card class="mt-1 mr-2 flex-grow-1">
              <v-card-title class="justify-center"><b>SBC Info</b></v-card-title>
              <v-img
                width="255"
                src="https://upload.wikimedia.org/wikipedia/commons/d/d1/Raspberry_Pi_OS_Logo.png"
              ></v-img>
              <v-card-text>
                <p class="text-h7 text--primary">
                  <b>Model:</b> Raspberry Pi 4 B+ <br>
                  <b>SoC:</b> Broadcom BCM2711 <br>
                  <b>Architecture:</b> Cortex A72 a 1,5 GHz <br>
                  <b>RAM:</b> 4GB <br> 
                  <b>OS:</b> Raspberry Pi OS <br>
                  <b>Connectivity:</b> Bluetooth 5.0 Wifi
                </p>
              </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="3" sm="6" md="3" class="d-flex">
        <!-- <v-col cols="md-lg-4" class="d-flex"> -->
          <v-card class="mt-1 ml-2 mr-2 flex-grow-1">
              <v-card-title class="justify-center"><b>CPU Temperature</b></v-card-title>
              <v-progress-circular
                :rotate="90"
                :size="230"
                :width="35"
                :value="rpi_status.temperatures.cpu"
                color="primary"
              >
                {{ rpi_status.temperatures.cpu }} °C
              </v-progress-circular>
          </v-card>
        </v-col>
        <!-- <v-col cols="md-lg-4" class="d-flex"> -->
          <v-col cols="3" sm="6" md="3" class="d-flex">
          <v-card class="mt-1 ml-2 mr-2  flex-grow-1">
              <v-card-title class="justify-center"><b>CPU Load</b></v-card-title>
              <v-progress-circular
                :rotate="90"
                :size="230"
                :width="35"
                :value="rpi_status.cpu_usage.total_cpu_usage"
                color="primary"
              >
                {{ rpi_status.cpu_usage.total_cpu_usage }} %
              </v-progress-circular>
          </v-card>
        </v-col>
        <v-col cols="3" sm="6" md="3" class="d-flex">
          <v-card class="mt-1 ml-2 mr-2 flex-grow-1" max-width= "290px">
              <v-card-title class="justify-center"><b>CPU cores load</b></v-card-title>
              <apexchart 
              type="radialBar" 
              height="320"
              :options="optionsRadialBars" :series="rpi_status.cpu_usage.cpu_usage_per_core.slice(0, 4)"
              :labels="labels">
            </apexchart>  
          </v-card>
        </v-col>
        <!-- <v-col cols="auto" class="d-flex" style="flex-direction:column">
          <v-card class="mt-1 flex-grow-1">
            <v-card-title class="justify-center"><b>Core 0</b></v-card-title>
            <v-progress-circular
              :rotate="90"
              :size="90"
              :width="15"
              :value="rpi_status.cpu_usage.cpu_usage_per_core[0]"
              color="primary"
            >
              {{ rpi_status.cpu_usage.cpu_usage_per_core[0] }} %
            </v-progress-circular>
          </v-card>
          <v-card class="mt-1 flex-grow-1">
            <v-card-title class="justify-center"><b>Core 1</b></v-card-title>
            <v-progress-circular
              :rotate="90"
              :size="90"
              :width="15"
              :value="rpi_status.cpu_usage.cpu_usage_per_core[1]"
              color="primary"
            >
              {{ rpi_status.cpu_usage.cpu_usage_per_core[1] }} %
            </v-progress-circular>
          </v-card>
        </v-col>
        <v-col cols="auto" class="d-flex" style="flex-direction:column">
          <v-card class="mt-1 flex-grow-1">
            <v-card-title class="justify-center"><b>Core 2</b></v-card-title>
            <v-progress-circular
              :rotate="90"
              :size="90"
              :width="15"
              :value="rpi_status.cpu_usage.cpu_usage_per_core[2]"
              color="primary"
            >
              {{ rpi_status.cpu_usage.cpu_usage_per_core[2] }} %
            </v-progress-circular>
          </v-card>
          <v-card class="mt-1 flex-grow-1">
            <v-card-title class="justify-center"><b>Core 3</b></v-card-title>
            <v-progress-circular
              :rotate="90"
              :size="90"
              :width="15"
              :value="rpi_status.cpu_usage.cpu_usage_per_core[3]"
              color="primary"
            >
              {{ rpi_status.cpu_usage.cpu_usage_per_core[3] }} %
            </v-progress-circular>
          </v-card>
        </v-col> -->
      </v-row>
    </v-container>
    <v-container class="lighten-5 mb-6 margin-initial"> 
      <v-row class="justify-start">
        <v-col cols="4" sm="6" md="4" class="d-flex">
          <v-card class="mt-1 flex-grow-1">
              <v-card-title class="justify-center"><b>Disk Usage</b></v-card-title>
              <v-card-text>
                <div class="text--primary">
                  Disk size: {{rpi_status.disk.disk_total.toFixed(2)}} GB<br>
                  Memory used: {{rpi_status.disk.disk_used.toFixed(2)}} GB<br>
                  Memory available: {{rpi_status.disk.disk_free.toFixed(2)}} GB<br>
                </div>
              </v-card-text>
          <apexchart 
            type="donut" 
            :options="options" :series="[rpi_status.disk.disk_free, rpi_status.disk.disk_used]"
            :labels="labels">
          </apexchart>  
          </v-card>
        </v-col>
        <v-col cols="4" sm="6" md="4" class="d-flex">
          <v-card class="mt-1 flex-grow-1">
              <v-card-title class="justify-center"><b>RAM Usage</b></v-card-title>
              <v-card-text>
                <div class="text--primary">
                  RAM size: {{rpi_status.ram.ram_total.toFixed(2)}} MB<br>
                  RAM used: {{rpi_status.ram.ram_free.toFixed(2)}} MB<br>
                  RAM available: {{rpi_status.ram.ram_free.toFixed(2)}} MB<br>
                </div>
              </v-card-text>
            <apexchart 
              type="donut" 
              :options="options" :series="[rpi_status.ram.ram_total, rpi_status.ram.ram_free]"
              :labels="labels">
            </apexchart>  
          </v-card>
        </v-col>
        <v-col cols="4" sm="6" md="4" class="d-flex">
          <v-card class="flex-grow-1">
            <v-card-title class="justify-center"><b>Swap RAM Usage</b></v-card-title>
              <v-card-text >
                <div class="text--primary">
                  Swap size: {{rpi_status.swap_ram.swap_ram_total.toFixed(2)}} MB<br>
                  Swap used: {{rpi_status.swap_ram.swap_ram_used.toFixed(2)}} MB<br>
                  Swap available: {{rpi_status.swap_ram.swap_ram_free.toFixed(2)}} MB<br>
                </div>
              </v-card-text>
            <apexchart 
              type="donut" 
              :options="options" :series="[rpi_status.swap_ram.swap_ram_free, rpi_status.swap_ram.swap_ram_used]"
              :labels="labels">
            </apexchart>  
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    
  </div>
</template>



<script>
import axios from 'axios'; 
import Vue from 'vue'
import VueApexCharts from 'vue-apexcharts'

Vue.component('apexchart', VueApexCharts)


export default {

  data: () => ({
    
      interval: {},
      rpi_status: {},

      options: {
        labels: ['Free', 'Used'],
        chart: {
          id: 'vuechart-example'
        },
        legend: {
          position: 'top'
        }
      },
      // series: [44, 55, 66, 77],

      optionsRadialBars : {
        plotOptions: {
          radialBar: {
            offsetY: 0,
            startAngle: 0,
            endAngle: 270,
            hollow: {
              margin: 5,
              size: '10%',
              background: 'transparent',
              image: undefined,
            },
            dataLabels: {
              name: {
                show: false,
              },
              value: {
                show: false,
              }
            }
          }
        },
        // colors: ['#1ab7ea', '#0084ff', '#39539E', '#0077B5'],
        labels: ['Core 1', 'Core 2', 'Core 3', 'Core 4'],
        legend: {
          show: true,
          floating: true,
          fontSize: '14px',
          position: 'left',
          offsetX: -15,
          offsetY: 15,
          labels: {
            useSeriesColors: true,
          },
          markers: {
            size: 0
          },
          formatter: function(seriesName, opts) {
            return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex] + '%'
          },
          itemMargin: {
            vertical: 3
          }
        },
        responsive: [{
          breakpoint: 350,
          options: {
            legend: {
                show: false
            }
          }
        }]
        }
  }),

  beforeDestroy() {
    clearInterval(this.interval);
  },


  mounted() {
    this.getRPiStatus();
    this.intervalFetchData();
  },

  methods : {

        getRPiStatus: function() {
          axios
                .get("http://localhost:5000/rpi_status")    
                .then(response => (
                  this.rpi_status = response.data)) 
                .catch(error => console.log(error))  
        },
        
        intervalFetchData: function () {
              setInterval(() => {    
                this.getRPiStatus();
                }, 2000);    
        }
  },
};
</script>
