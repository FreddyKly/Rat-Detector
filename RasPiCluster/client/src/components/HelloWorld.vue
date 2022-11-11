<template>
  <v-app>
    <!-- App-Bar on top -->
      <v-app-bar color="teal-darken-4">
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-app-bar-title class="app_bar">Rat-Detector</v-app-bar-title>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>

      </v-app-bar>

    <div class="container">
      <h1>Latest Detections</h1>
      <hr />
      <p class="error" v-if="error">{{ error }}</p>
    </div>

    <!-- Grid with Pictures -->
    <v-main>
      <v-container>
        <v-row>
          <v-col v-for="(detection, index) in detections" v-bind:item="detection" v-bind:index="index"
            v-bind:key="detection._id" cols="2">
            <v-card height="200">
              <v-card-text>
                {{ `${detection.createdAt.toUTCString()}` }}
                <p class="text">{{ detection.text }}</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import detectionsService from "@/detectionsService";

export default {
  name: "HelloWorld",
  data() {
    return {
      detections: [],
      error: "",
      text: "",
    };
  },
  async created() {
    try {
      this.detections = await detectionsService.getDetections();
      console.log(this.detections);
    } catch (err) {
      this.error = err.message;
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
