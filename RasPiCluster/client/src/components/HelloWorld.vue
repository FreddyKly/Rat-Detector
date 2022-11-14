<template>
  <v-app>
    <!-- App-Bar on top -->
    <v-app-bar color="teal-darken-4">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-app-bar-title class="app_bar text-left">Rat-Detector</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
    </v-app-bar>

    <!-- Grid with Pictures -->
    <v-main>
      <v-container>
        <v-row>
          <v-col v-for="(detection, index) in detections" 
          v-bind:item="detection" 
          v-bind:index="index"
            v-bind:key="detection._id" 
            cols="2">
            <v-hover>
              <template 
              v-slot:default="{ isHovering, props }">
                <v-card 
                height="250" 
                width="250" 
                :elevation="isHovering ? 15 : 1" 
                v-bind="props">
                  <v-img :src="`data:image/jpg;base64,${detection.image}`" class="align-end" v-bind="props">
                    <v-card-title class="text-white"> {{ detection.createdAt }} </v-card-title>
                  </v-img>
                  <!-- <v-card-text>
                {{ `${detection.createdAt.toUTCString()}` }}
                <p class="text">{{ detection.text }}</p>
              </v-card-text> -->
                </v-card>
              </template>
            </v-hover>
          </v-col>
        </v-row>
      </v-container>
      <v-hover>
          <template v-slot:default="{ isHovering, props }">
            <v-card v-bind="props" :color="isHovering ? 'primary' : undefined" title="Hover over me" text="...">
            </v-card>
          </template>
        </v-hover>
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
.card_descriptor {
  color: white;
  font-weight: bold;
  margin-right: 0;
  vertical-align: bottom;
}
</style>
