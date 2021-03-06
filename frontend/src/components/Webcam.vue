<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6" v-if="show === true">
        <div class="border">
          <vue-web-cam
            ref="webcam"
            :device-id="deviceId"
            width="100%"
            @started="onStarted"
            @stopped="onStopped"
            @error="onError"
            @cameras="onCameras"
            @camera-change="onCameraChange"
          />
        </div>

        <div class="row">
          <div class="col-md-12">
            <button type="button" class="btn btn-primary" @click="onCapture">Capture Photo</button>
          </div>
        </div>
      </div>
      <div class="col-md-6" v-if="img !== null">
        <h2>Captured Image</h2>
        <figure class="figure">
          <img :src="img" class="img-responsive" />
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
import { WebCam } from "vue-web-cam";

export default {
  name: "Webcam",
  components: {
    "vue-web-cam": WebCam
  },
  data() {
    return {
      img: null,
      camera: null,
      deviceId: null,
      devices: [],
      show: true
    };
  },
  computed: {
    device: function() {
      return this.devices.find(n => n.deviceId === this.deviceId);
    }
  },
  watch: {
    camera: function(id) {
      this.deviceId = id;
    },
    devices: function() {
      // Once we have a list select the first one
      const [first, ...tail] = this.devices;
      if (first) {
        this.camera = first.deviceId;
        this.deviceId = first.deviceId;
      }
    }
  },
  methods: {
    onCapture() {
      this.img = this.$refs.webcam.capture();
      this.show = false;
      this.$emit("capture", this.img);
    },
    onStarted(stream) {
      console.log("On Started Event", stream);
    },
    onStopped(stream) {
      console.log("On Stopped Event", stream);
    },
    onStop() {
      this.show = false;
      this.$refs.webcam.stop();
    },
    onStart() {
      this.$refs.webcam.start();
      this.show = true;
    },
    onError(error) {
      console.log("On Error Event", error);
    },
    onCameras(cameras) {
      this.devices = cameras;
      console.log("On Cameras Event", cameras);
    },
    onCameraChange(deviceId) {
      this.deviceId = deviceId;
      this.camera = deviceId;
      console.log("On Camera Change Event", deviceId);
    }
  }
};
</script>
