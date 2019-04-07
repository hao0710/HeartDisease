<template>
  <div>
    <hr>
    <hr>
    <b-jumbotron
      header="Heart Disease Analysis"
      lead="Predict heart disease using machine learning"
    ></b-jumbotron>
    <!--<p>{{ data }}</p>-->

    <!--Gender selector -->
    <div class="container">
      <h2>Please enter information below</h2>
      <hr>
      <h3 class="c-form-label" for="gender">Gender</h3>
      <br>
      <b-form-radio-group
        id="btn-radios-1"
        v-model="selected"
        :options="options_1"
        buttons
        name="radios-btn-default"
      ></b-form-radio-group>
      <p>
        Pressed State:
        <strong>{{selected}}</strong>
      </p>
      <!--Age--->

      <div role="group">
        <h3 for="input-live">Age:</h3>
        <b-form-input
          id="input-live"
          v-model="age"
          :state="ageState"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your age"
          trim
        ></b-form-input>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback id="input-live-feedback">Please enter an age beteen 35-74 years</b-form-invalid-feedback>

        <!-- This is a form text block (formerly known as help block) -->
        <!--<b-form-text id="input-live-help">Your age.</b-form-text>-->
        <p>
          Input Age:
          <strong>{{age}}</strong>
        </p>
      </div>

      <!--Chest Pain Type--->
      <h3 class="c-form-label" for="Chest pain type">Chest Pain Type</h3>
      <div>
        <b-form-radio-group
          id="radio-group-1"
          v-model="selected_pain"
          :options="options_2"
          name="radio-options"
        ></b-form-radio-group>

        <div class="mt-3">
          Selected:
          <strong>{{ selected_pain }}</strong>
        </div>
      </div>

      <!--Resting Blood Pressure--->

      <div role="group">
        <h3 for="input-live">Resting Blood Pressure:</h3>
        <b-form-input
          id="input-live"
          v-model="bloodpressure"
          :state="bloodpressureState"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your Resting Blood Pressure"
          trim
        ></b-form-input>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback
          id="input-live-feedback"
        >Please enter Resting Blood Pressure between 0-300</b-form-invalid-feedback>

        <!-- This is a form text block (formerly known as help block) -->
        <!--<b-form-text id="input-live-help">Your age.</b-form-text>-->
        <p>
          Input blood pressure:
          <strong>{{bloodpressure}}</strong>
        </p>
      </div>

      <!-- Serum Cholestoral in mg/dl -->
      <div role="group">
        <h3 for="input-live">Serum Cholestoral in mg/dl:</h3>
        <b-form-input
          id="input-live"
          v-model="cholestoral"
          :state="cholestoralState"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your Serum Cholestoral in mg/dl"
          trim
        ></b-form-input>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback id="input-live-feedback">Please enter Serum Cholestoral in mg/dl</b-form-invalid-feedback>

        <!-- This is a form text block (formerly known as help block) -->
        <!--<b-form-text id="input-live-help">Your age.</b-form-text>-->
        <p>
          Input cholestoral:
          <strong>{{cholestoral}}</strong>
        </p>
      </div>

      <!-- Fasting Blood Sugar > 120 mg/dl-->

      <h3 class="c-form-label" for="bloodsugar">Fasting Blood Sugar > 120 mg/dl</h3>
      <br>
      <b-form-radio-group
        id="btn-radios-1"
        v-model="selected_bloodsugar"
        :options="options_3"
        buttons
        name="radios-btn-default"
      ></b-form-radio-group>
      <p>
        bloodsugar State:
        <strong>{{selected_bloodsugar}}</strong>
      </p>

      <!--Resting Electrocardiographic Results-->

      <h3
        class="c-form-label"
        for="Resting Electrocardiographic Results"
      >Resting Electrocardiographic Results</h3>
      <div>
        <b-form-radio-group
          id="radio-group-2"
          v-model="selected_electrocardiographic"
          :options="options_4"
          name="radio-options1"
        ></b-form-radio-group>

        <div class="mt-3">
          Selected:
          <strong>{{ selected_electrocardiographic }}</strong>
        </div>
      </div>

      <!--Maximum Heart Rate Achieved-->
      <div role="group">
        <h3 for="input-live">Maximum Heart Rate Achieved:</h3>
        <b-form-input
          id="input-live"
          v-model="heart_rate"
          :state="heart_rateState"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your Maximum Heart Rate Achieved"
          trim
        ></b-form-input>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback id="input-live-feedback">Please enter Maximum Heart Rate Achieved</b-form-invalid-feedback>

        <!-- This is a form text block (formerly known as help block) -->
        <!--<b-form-text id="input-live-help">Your age.</b-form-text>-->
        <p>
          Input max heart rate:
          <strong>{{heart_rate}}</strong>
        </p>
      </div>

      <!-- Exercise Induced Angina -->
      <h3 class="c-form-label" for="angina">Exercise Induced Angina</h3>
      <br>
      <b-form-radio-group
        id="btn-radios-1"
        v-model="selected_angina"
        :options="options_5"
        buttons
        name="radios-btn-default"
      ></b-form-radio-group>
      <p>
        Exercise angina State:
        <strong>{{selected_angina}}</strong>
      </p>

      <!-- Old peak  ST depression induced by exercise relative to rest -->
      <div role="group">
        <h3 for="input-live">Old peak:ST depression induced by exercise relative to rest:</h3>
        <b-form-input
          id="input-live"
          v-model="oldpeak"
          :state="oldpeakState"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your Old peak:ST depression induced by exercise relative to rest"
          trim
        ></b-form-input>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback
          id="input-live-feedback"
        >Please enter Old peak:ST depression induced by exercise relative to rest</b-form-invalid-feedback>

        <!-- This is a form text block (formerly known as help block) -->
        <!--<b-form-text id="input-live-help">Your age.</b-form-text>-->
        <p>
          Input oldpeak:
          <strong>{{oldpeak}}</strong>
        </p>
      </div>
      <!-- The Slope of the Peak Exercise ST segment -->

      <h3 class="c-form-label" for="slope">The Slope of the Peak Exercise ST segment</h3>
      <br>
      <b-form-radio-group
        id="btn-radios-1"
        v-model="selected_slope"
        :options="options_6"
        buttons
        name="radios-btn-default"
      ></b-form-radio-group>
      <p>
        Slope of Peak State:
        <strong>{{selected_slope}}</strong>
      </p>

      <!-- ca: number of major vessels (0-3) colored by flourosopy  -->
      <h3 class="c-form-label" for="ca">Number of major vessels (0-3) colored by flourosopy</h3>
      <br>
      <b-form-radio-group
        id="btn-radios-1"
        v-model="selected_ca"
        :options="options_7"
        buttons
        name="radios-btn-default"
      ></b-form-radio-group>
      <p>
        Number of major vessels:
        <strong>{{selected_ca}}</strong>
      </p>
    </div>
    <br>
    <b-button @click="onSubmit" type="submit" variant="info">Submit</b-button>
    <br>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      selected: "1",
      age: "",
      bloodpressure: "",
      cholestoral: "",
      heart_rate: "",
      oldpeak: "",
      options_1: [{ text: "Male", value: "1" }, { text: "Female", value: "0" }],
      selected_pain: "1",
      options_2: [
        { text: "typical angin", value: "1" },
        { text: "atypical angina", value: "2" },
        { text: "non-anginal pain", value: "3" },
        { text: "asymptomatic", value: "4" }
      ],
      selected_bloodsugar: "1",
      options_3: [{ text: "Yes", value: "1" }, { text: "No", value: "0" }],
      selected_electrocardiographic: "0",
      options_4: [
        { text: "normal", value: "0" },
        { text: "having ST-T wave abnormality", value: "1" },
        {
          text:
            "showing probable or definite ventricular hypertrophy by Estes’ criteria",
          value: "2"
        }
      ],
      selected_angina: "1",
      options_5: [{ text: "Yes", value: "1" }, { text: "No", value: "0" }],
      selected_slope: "1",
      options_6: [
        { text: "Upsloping", value: "1" },
        { text: "Flat", value: "2" },
        { text: "Downsloping", value: "3" }
      ],
      selected_ca: "1",
      options_7: [
        { text: "0", value: "1" },
        { text: "1", value: "2" },
        { text: "2", value: "3" },
        { text: "3", value: "4" }
      ]
    };
  },
  methods: {
    addBook(payload) {
      const path = "http://localhost:5000/datasets/submit";
      axios
        .post(path, payload)
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        gender: this.selected,
        age: this.age,
        selected_pain: this.selected_pain,
        bloodpressure: this.bloodpressure,
        cholestoral: this.cholestoral,
        selected_bloodsugar: this.selected_bloodsugar,
        heart_rate: this.heart_rate,
        selected_slope: this.selected_slope,
        selected_angina: this.selected_angina,
        oldpeak: this.oldpeak,
        selected_ca: this.selected_ca,
        selected_electrocardiographic: this.selected_electrocardiographic
      };
      this.addBook(payload);
    }
  },

  computed: {
    ageState() {
      return this.age >= 35 && this.age <= 74 ? true : false;
    },
    bloodpressureState() {
      return this.bloodpressure > 0 && this.bloodpressure <= 300 ? true : false;
    },
    cholestoralState() {
      return this.cholestoral > 0 && this.cholestoral <= 300 ? true : false;
    },
    heart_rateState() {
      return this.heart_rate > 0 && this.heart_rate <= 300 ? true : false;
    },
    oldpeakState() {
      return this.oldpeak > 0 && this.oldpeak <= 10 ? true : false;
    }
  }
};
</script>

<style scoped>
</style>