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
    <v-container class="lighten-5 mb-6 margin-initial">
      <v-row  class="justify-start">
        <v-col cols="auto" class="d-flex">
          <v-card class="mt-1 flex-grow-1">
              <v-card-title class="justify-center"><b>SBC Info</b></v-card-title>
              <v-img
                width="255"
                src="https://upload.wikimedia.org/wikipedia/commons/d/d1/Raspberry_Pi_OS_Logo.png"
              ></v-img>
              <v-card-text>
                <p class="text-h6 text--primary">
                  Model: Raspberry Pi 4 B+<br>
                  Ram: 4GB <br>
                  OS: Raspberry Pi OS
                </p>
              </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="auto" class="d-flex">
          <v-card class="mt-1 flex-grow-1">
              <v-card-title class="justify-center"><b>CPU Temperature</b></v-card-title>
              <!-- <v-card-text>
                <div class="text--primary">
                  Raspberry Pi device should be <br>
                  below 85 °C for it to work properly. <br>
                  Throttling starts at 82 °C. 
                </div>
              </v-card-text> -->
              <v-progress-circular
                :rotate="90"
                :size="230"
                :width="30"
                :value="rpi_status.temperatures.cpu"
                color="primary"
              >
                {{ rpi_status.temperatures.cpu }} °C
              </v-progress-circular>
          </v-card>
        </v-col>
        <v-col cols="auto" class="d-flex">
          <v-card class="mt-1 flex-grow-1">
              <v-card-title class="justify-center"><b>CPU Load</b></v-card-title>
              <v-progress-circular
                :rotate="90"
                :size="230"
                :width="30"
                :value="rpi_status.cpu_usage.total_cpu_usage"
                color="primary"
              >
                {{ rpi_status.cpu_usage.total_cpu_usage }} %
              </v-progress-circular>
          </v-card>
        </v-col>
        <v-col cols="auto" class="d-flex" style="flex-direction:column">
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
        </v-col>
      </v-row>
    </v-container>
    <v-container class="lighten-5 mb-6 margin-initial"> 
      <v-row class="justify-start">
        <v-col cols="auto" class="d-flex">
          <v-card class="mt-1 flex-grow-1">
              <v-card-title class="justify-center"><b>Disk Usage</b></v-card-title>
              <v-card-text>
                <div class="text--primary">
                  Disk size: {{rpi_status.disk.disk_total.toFixed(2)}} GB<br>
                  Memory used: {{rpi_status.disk.disk_free.toFixed(2)}} GB<br>
                  Memory available: {{rpi_status.disk.disk_free.toFixed(2)}} GB<br>
                </div>
              </v-card-text>
              <v-progress-circular
                :rotate="90"
                :size="230"
                :width="30"
                :value="rpi_status.disk.disk_percent_used"
                color="primary"
              >
                {{ rpi_status.disk.disk_percent_used }} %
              </v-progress-circular>
          </v-card>
        </v-col>
        <v-col cols="auto" class="d-flex">
          <v-card class="mt-1 flex-grow-1">
              <v-card-title class="justify-center"><b>RAM Usage</b></v-card-title>
              <v-card-text>
                <div class="text--primary">
                  RAM size: {{rpi_status.ram.ram_total.toFixed(2)}} MB<br>
                  RAM used: {{rpi_status.ram.ram_free.toFixed(2)}} MB<br>
                  RAM available: {{rpi_status.ram.ram_free.toFixed(2)}} MB<br>
                </div>
              </v-card-text>
              <v-progress-circular
                :rotate="90"
                :size="230"
                :width="30"
                :value="rpi_status.ram.ram_percent_used"
                color="primary"
              >
                {{ rpi_status.ram.ram_percent_used }} %
              </v-progress-circular>
          </v-card>
        </v-col>
        <v-col cols="auto" class="d-flex">
          <v-card class="mt-1 flex-grow-1">
              <v-card-title class="justify-center"><b>Swap RAM Usage</b></v-card-title>
              <v-card-text>
                <div class="text--primary">
                  Swap size: {{rpi_status.swap_ram.swap_ram_total.toFixed(2)}} MB<br>
                  Swap used: {{rpi_status.swap_ram.swap_ram_free.toFixed(2)}} MB<br>
                  Swap available: {{rpi_status.swap_ram.swap_ram_free.toFixed(2)}} MB<br>
                </div>
              </v-card-text>
              <v-progress-circular
                :rotate="90"
                :size="230"
                :width="30"
                :value="rpi_status.swap_ram.swap_ram_percent_used"
                color="primary"
              >
                {{ rpi_status.swap_ram.swap_ram_percent_used }} %
              </v-progress-circular>
          </v-card>
        </v-col>
      </v-row>
    </v-container>





    <!-- <div>
    <apexchart 
      width="300" type="donut" 
      :options="options" :series="[rpi_status.ram.ram_total, rpi_status.ram.ram_free]"
      :labels="labels">
    </apexchart>  
    </div> -->


    
  </div>
</template>



<script>
import axios from 'axios'; 
// import Vue from 'vue'
// import VueApexCharts from 'vue-apexcharts'

// Vue.component('apexchart', VueApexCharts)


export default {

  data() {
    return {
      interval: {},
      temperature: 0,
      storage: 0,
      rpi_status: 'a',
    };
  },

  // data: () => ({
    
  //     interval: {},
  //     temperature: 0,
  //     storage: 0,
  //     rpi_status: 'a',

  //     options: {
  //       labels: ['Core 1', 'Core 2', 'Core 3', 'Core 4'],
  //     chart: {
  //       id: 'vuechart-example'
  //     },
  //     title: {
  //       text: 'Disk',
  //       align: 'center',
  //       style: {
  //         fontSize:  '20px',
  //       },
  //     },
  //     },
  //     series: [44, 55, 13, 43, 22],
      

  // }),

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
