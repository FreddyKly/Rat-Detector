<template>
  <v-app>
    <!-- App-Bar on top -->
    <v-app-bar color="teal-darken-4" elevate-on-scroll>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-app-bar-title class="app_bar text-left">Rat-Detector</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
    </v-app-bar>

    <!-- Grid with Pictures -->
    <v-main>
      <v-container fluid>
        <v-navigation-drawer v-model="drawer">
          <v-list nav>
            <v-list-item prepend-icon="mdi-home" title="Home" value="home" @click="$router.push('/')"></v-list-item>
            <v-list-item prepend-icon="mdi-camera-wireless " title="Sensor-Node" value="sensor-node"
              @click="$router.push('/sensor-node')"></v-list-item>
            <v-list-item prepend-icon="mdi-message-alert" title="Notifications" value="notifications"
              @click="$router.push('/notifications')"></v-list-item>
            <v-list-item prepend-icon="mdi-chart-box" title="Statistics" value="statistics"
              @click="$router.push('/statistics')"></v-list-item>
            <v-list-item prepend-icon="mdi-account-supervisor-circle" title="Team" value="team"
              @click="$router.push('/team')"></v-list-item>
          </v-list>
        </v-navigation-drawer>
        <v-row>
          <v-col v-for="(detection, index) in detections.slice()" v-bind:item="detection" v-bind:index="index"
            v-bind:key="detection._id" cols="2">
            <v-hover>
              <template v-slot:default="{ isHovering, props }">
                <v-card height="250" width="250" :elevation="isHovering ? 15 : 1" v-bind="props">
                  <v-img :src="`data:image/jpg;base64,${detection.img}`" class="align-end" v-bind="props"
                    :gradient="isHovering ? 'to bottom, rgba(0,0,0,0), rgba(0,0,0,0), rgba(0,0,0,0.1), rgba(0,0,0,.45)' : 'to bottom, rgba(0,0,0,0), rgba(0,0,0,0), rgba(0,0,0,0.3), rgba(0,0,0,.5)'"
                    @click="detection.showDetails = !detection.showDetails">
                    <v-card-title class="text-white"> {{
                      detection.createdAt.getHours() + ":" +
                        detection.createdAt.getMinutes() + " " +
                        detection.createdAt.getDate() + "." +
                        (detection.createdAt.getMonth() + 1) + "." +
                        detection.createdAt.getFullYear()
                    }} </v-card-title>
                  </v-img>
                </v-card>
              </template>
            </v-hover>
            <v-expand-transition>
              <v-card v-show="detection.showDetails" elevation="10" width="250" transition="scroll-y-transition">
                <v-card-text>
                  Confidence: {{ detection.confidence }}
                </v-card-text>
                <v-card-text>
                  Number of Rats: {{ detection.numberOfRats }}
                </v-card-text>
              </v-card>
            </v-expand-transition>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import detectionsService from "@/detectionsService";

export default {
  name: "CardGrid",
  data() {
    return {
      drawer: false,
      detections: [],
      error: "",
      text: "",
    };
  },
  async created() {
    try {
      this.detections = await detectionsService.getDetections();
      console.log('First Element of Database', this.detections[0]);
    } catch (err) {
      console.log(err.message);
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card_descriptor {
  color: white;
  font-weight: bold;
  margin-right: 0;
  vertical-align: bottom;
}
</style>
