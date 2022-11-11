<template>
  <v-app id="inspire">
    <v-app-bar app shrink-on-scroll>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Application</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <div class="container">
      <h1>Latest Detections</h1>
      <hr />
      <p class="error" v-if="error">{{ error }}</p>
    </div>
    <v-main>
      <v-container>
        <v-row>
          <v-col
            v-for="(detection, index) in detections"
            v-bind:item="detection"
            v-bind:index="index"
            v-bind:key="detection._id"
          >
            <v-card height="200">
              <v-card-text>
                {{
                  `${detection.createdAt.toUTCString()}`
                }}
                <p class="text">{{ detection.text }}</p></v-card-text
              >
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
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
