<template>
  <div class="container">
    <h1>Latest Detection</h1>
    <hr>
    <p class="error" v-if="error">{{ error }}</p>
    <div class="detections-container">
      <div class="detections" 
      v-for="(detection, index) in detections"
      v-bind:item="detection"
      v-bind:index="index"
      v-bind:key="detection._id">
      {{ `${detection.createdAt.getDate()}.${detection.createdAt.getMonth()}.${detection.createdAt.getFullYear()}` }}
        <p class="text">{{ detection.text }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import detectionsService from '@/detectionsService';

export default {
  name: 'HelloWorld',
  data() {
    return {
      detections: [],
      error: '',
      text: ''
    }
  },
  async created() {
    try{
      this.detections = await detectionsService.getDetections();
      console.log(this.detections)
    } catch(err){
      this.error = err.message;
    }
  }
}
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
