<template>
  <div>
    <hr>
    <hr>
    <b-jumbotron
      header="Heart Disease Analysis"
      lead="Predict heart disease using machine learning"
    ></b-jumbotron>
    <!--<p>{{ data }}</p>-->
    <section class="o-section">
    <div class="o-grid o-grid--center">
        <div class="o-col o-col--5">
            <div class="o-col__inner">
                <p>Enter patient information below</p>
                <form class="c-form-stepper" selector=".js-calculator">
                    <div class="c-form-stepper__container">
                        <div>
                            <div class="c-form-stepper__frame">
                                <div class="c-form-stepper__inner">
                                    <ul class="c-form-stepper__fields">
                                        <li class="c-form-stepper__field"><label class="c-form-label"
                                                for="gender">Gender</label>
                                            <div>
                                                <div class="c-form-radio undefined"><input class="c-form-radio__input"
                                                        type="radio" name="gender" selector=".js-calculator"
                                                        id="gender-female" label="[object Object]" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="" shrinklabel="" value="Female"><label class="c-form-radio__label" for="gender-female"><span><svg
                                                                viewBox="0 0 500 500">
                                                                <path class="st0"
                                                                    d="M438.1 484.5H61.9v-17.9c.1-1.6 2.9-51.5 92.6-80.4 0 0 10.4-5.3 20.8-11.6 8.6-5.2 15.3-9.8 20.4-13.7 2.6 5.5 6.2 12.5 10.7 19.6 13.6 21.2 28.3 31.9 43.6 31.9s30.1-10.7 43.6-31.9c4.6-7.1 8.2-14.1 10.7-19.6 5.3 4.2 12.3 8.8 20.7 14 10.2 6.3 20.5 11.4 20.5 11.4 26.2 8.3 61.6 24 80.8 51.4 11 15.7 11.7 28.3 11.7 29v17.8zM206.2 327.1c13.6 5.3 28.3 7.9 43.8 7.9 15.5 0 30.2-2.7 43.8-7.9v19.4c-1.5 3.6-6.1 14.7-13.2 25.6-7.3 11.3-18.5 24.8-30.6 24.8-12.1 0-23.3-13.4-30.5-24.6-7.1-11-11.8-22.2-13.3-25.8v-19.4zm91.8-18.8c-14.4 7.5-30.5 11.3-48 11.3s-33.6-3.8-48-11.3c-17.5-9-32.1-23.4-42.2-41.7-10.1-18.3-15.5-40.1-15.5-63v-70.4c14.9-1.9 49.8-7.4 71.7-19.8h67.6c18.4 12.4 56 18 72.1 19.8v70.4c0 22.9-5.4 44.7-15.5 63-10.1 18.2-24.7 32.6-42.2 41.7zm-179.4-78.9v-97.9c0-64 52-116 116-116h30.9c64 0 116 52 116 116v97.9c0 33.1-3.6 60.6-10.8 81.8-8.5 25.1-22.1 41.4-40.5 48.6-9.4-5.8-16.6-11-20.8-15v-25c18.4-10.5 33.7-26.2 44.4-45.6 11.4-20.6 17.4-45 17.4-70.5v-84.4l-7-.6c-15.4-1.4-58.5-7.5-73.3-19l-2.1-1.6h-77l-1.8 1.1c-24.3 14.8-73.5 19.5-74 19.5l-7 .7v84.4c0 25.5 6 49.9 17.4 70.5 10.8 19.4 26 35.1 44.4 45.6V345c-4 3.8-10.9 8.8-20.4 14.7-24.4-10-51.8-40.8-51.8-130.3zm232.3 142.3c-.8-.4-2.5-1.3-4.8-2.6 33.7-19.6 50.8-66.5 50.8-139.8v-97.9C396.9 59 337.9 0 265.5 0h-30.9c-72.5 0-131.4 59-131.4 131.4v97.9c0 71.7 17.7 119.4 51.3 139.4-2.5 1.4-4.5 2.4-5.4 2.9-100.5 32.7-102.7 92.2-102.7 94.8V500h407.2v-33.5c0-2.6-1.5-62.5-102.7-94.8z">
                                                                </path>
                                                                <path class="st0"
                                                                    d="M257.7 193.3h-15.5v41.2c0 4.3 3.5 7.7 7.7 7.7h20.6v-15.5h-12.9v-33.4z">
                                                                </path>
                                                            </svg>Female</span></label></div>
                                                <div class="c-form-radio undefined"><input class="c-form-radio__input"
                                                        type="radio" name="gender" selector=".js-calculator"
                                                        id="gender-male" label="[object Object]" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="" shrinklabel="" value="Male"><label class="c-form-radio__label" for="gender-male"><span><svg
                                                                viewBox="0 0 500 500">
                                                                <path class="st0"
                                                                    d="M438.1 484.5H61.9v-17.9c0-.9.9-13.3 11.9-28.9 19.4-27.4 54.5-43.1 80.6-51.5 0 0 29.3-15.3 43.8-27.4 6.8 6.4 19.2 16.1 35.3 20.4L193 419.8l10.9 10.9 46.1-46.1 46.1 46.1 10.9-10.9-40.6-40.6c16.2-4.3 28.6-14.1 35.3-20.4 14.4 12.1 43.8 27.4 43.8 27.4 26.2 8.3 61.6 24 80.8 51.4 11 15.7 11.7 28.3 11.7 29l.1 17.9zM145.6 222.8c-.8-6-1.3-12.4-1.3-19.2v-50c16.9-2.8 61-12.1 95.7-38.4 16.5 11 71.3 45.5 115.6 49.3v39c0 6.8-.4 13.3-1.3 19.3-5.3 38.5-25.9 69.6-56.4 85.4-14.4 7.5-30.5 11.3-48 11.3s-33.6-3.8-48-11.3c-30.4-15.7-51-46.8-56.3-85.4zm-32.2-29.5c0-3.3 1.7-10.5 15.5-12.4 0 0 .1 29 .3 32-9-4.7-15.8-13.3-15.8-19.6zm56.5-146.7c23.2-20.7 50.2-31.2 80.1-31.2s56.9 10.5 80.1 31.2c14.4 12.8 22.9 25.8 25.5 30.2V149c-45.8-4.6-107.3-46.8-111.3-49.6-2.1-1.7-21.8-18.1-34.6-34.7l-12.2 9.5c9.5 12.3 22 24 29.9 31-29.6 21-66.6 29.6-83.1 32.6v-61c2.7-4.4 11.2-17.4 25.6-30.2zm216.7 146.7c0 6.3-6.8 14.9-15.7 19.7.2-3.1.3-32 .3-32 13.7 1.8 15.4 9 15.4 12.3zM246.9 365.9c-20.1-1.4-35.7-15.7-40.7-20.9v-17.8c13.6 5.3 28.3 7.9 43.8 7.9 15.5 0 30.2-2.7 43.8-7.9V345c-5 5.3-20.5 19.5-40.7 20.9h-6.2zm104 5.8c-9.2-4.9-31.9-17.7-41.6-26.9v-25.1c31.3-17.9 52.7-50 59.6-89.4 17.7-5.1 33.2-21.7 33.2-37.1 0-15.5-11.7-25.8-30.9-27.9V72.8l-.9-1.7c-.4-.7-9.9-18.1-29.4-35.6C315 12.3 283.5 0 250 0s-65 12.3-90.9 35.5c-19.5 17.5-29 34.9-29.4 35.6l-.9 1.7v92.6c-19.3 2.1-30.9 12.4-30.9 27.9 0 15.3 15.4 32 33.2 37.1 6.9 39.3 28.3 71.5 59.6 89.4v25.1c-9.8 9.2-32.5 22.1-41.7 26.9-100.4 32.5-102.6 92-102.6 94.6V500h407.2v-33.5c0-2.6-1.5-62.5-102.7-94.8z">
                                                                </path>
                                                                <path class="st0"
                                                                    d="M239.7 417.5h20.6V433h-20.6zm0 31h20.6V464h-20.6zM250 242.3h20.6v-15.5h-12.9v-33.5h-15.5v41.2c.1 4.3 3.5 7.8 7.8 7.8z">
                                                                </path>
                                                            </svg>Male</span></label></div>
                                            </div>
                                        </li>
                                        <li class="c-form-stepper__field"><label class="c-form-label"
                                                for="age">Age</label>
                                            <div class="c-form-text"><input id="age" step="" type="number"
                                                    selector=".js-calculator" name="age" label="Age"
                                                    placeholder="Between 35 - 74" info="" value=""><label
                                                    class="c-form-text__suffix" for="age">years</label></div>
                                        </li>
                                        <li class="c-form-stepper__field"><label class="c-form-label"
                                                for="bloodPressure">Systolic Blood Pressure</label>
                                            <div class="c-form-text"><input id="bloodPressure" step="" type="number"
                                                    selector=".js-calculator" name="bloodPressure"
                                                    label="Systolic Blood Pressure" placeholder="75 or more" info=""
                                                    value=""><label class="c-form-text__suffix"
                                                    for="bloodPressure">mmHg</label></div>
                                        </li>
                                        <div class="u-spacing-top-medium"></div>
                                        <li class="c-form-stepper__field"><label class="c-form-label"
                                                for="smoker">Smoking Status</label>
                                            <p class="c-form-info">Smoker is defined as currently smoking or quit within
                                                last year</p>
                                            <div>
                                                <div class="c-form-radio undefined"><input class="c-form-radio__input"
                                                        type="radio" name="smoker" selector=".js-calculator"
                                                        id="smoker-yes" label="Yes" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="Smoker is defined as currently smoking or quit within last year" shrinklabel="" value="Yes"><label
                                                        class="c-form-radio__label" for="smoker-yes">Yes</label></div>
                                                <div class="c-form-radio undefined"><input class="c-form-radio__input"
                                                        type="radio" name="smoker" selector=".js-calculator"
                                                        id="smoker-no" label="No" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="Smoker is defined as currently smoking or quit within last year" shrinklabel="" value="No"><label
                                                        class="c-form-radio__label" for="smoker-no">No</label></div>
                                            </div>
                                        </li>
                                        <li class="c-form-stepper__field"><label class="c-form-label"
                                                for="cholesterol">Total cholesterol</label>
                                            <div class="c-form-text"><input id="cholesterol" step="any" type="number"
                                                    selector=".js-calculator" name="cholesterol"
                                                    label="Total cholesterol" placeholder="2 or more" info=""
                                                    value=""><label class="c-form-text__suffix"
                                                    for="cholesterol">mmol/L</label></div>
                                        </li>
                                        <li class="c-form-stepper__field"><label class="c-form-label"
                                                for="hdlCholesterol">HDL cholesterol</label>
                                            <div class="c-form-text"><input id="hdlCholesterol" step="any" type="number"
                                                    selector=".js-calculator" name="hdlCholesterol"
                                                    label="HDL cholesterol" placeholder="Between 0.2 - 5" info=""
                                                    value=""><label class="c-form-text__suffix"
                                                    for="hdlCholesterol">mmol/L</label></div>
                                        </li>
                                        <li class="c-form-stepper__field"><label class="c-form-label"
                                                for="diabetes">Diabetes</label>
                                            <div>
                                                <div class="c-form-radio undefined"><input class="c-form-radio__input"
                                                        type="radio" name="diabetes" selector=".js-calculator"
                                                        id="diabetes-yes" label="Yes" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="" shrinklabel="" value="Yes"><label class="c-form-radio__label" for="diabetes-yes">Yes</label></div>
                                                <div class="c-form-radio undefined"><input class="c-form-radio__input"
                                                        type="radio" name="diabetes" selector=".js-calculator"
                                                        id="diabetes-no" label="No" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="" shrinklabel="" value="No"><label class="c-form-radio__label" for="diabetes-no">No</label></div>
                                            </div>
                                        </li>
                                        <li class="c-form-stepper__field"><label class="c-form-label" for="ecgLvh">ECG
                                                LVH</label>
                                            <div>
                                                <div class="c-form-radio c-form-radio--third"><input
                                                        class="c-form-radio__input" type="radio" name="ecgLvh"
                                                        selector=".js-calculator" id="ecgLvh-yes" label="Yes" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="" shrinklabel="" extraclass="c-form-radio--third" value="Yes"><label class="c-form-radio__label"
                                                        for="ecgLvh-yes">Yes</label></div>
                                                <div class="c-form-radio c-form-radio--third"><input
                                                        class="c-form-radio__input" type="radio" name="ecgLvh"
                                                        selector=".js-calculator" id="ecgLvh-no" label="No" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="" shrinklabel="" extraclass="c-form-radio--third" value="No"><label class="c-form-radio__label"
                                                        for="ecgLvh-no">No</label></div>
                                                <div class="c-form-radio c-form-radio--third"><input
                                                        class="c-form-radio__input" type="radio" name="ecgLvh"
                                                        selector=".js-calculator" id="unknown" label="Unknown" validate="function isRequired(value) {
    return value ? undefined : 'This field is required';
  }" info="" shrinklabel="" extraclass="c-form-radio--third" value="unknown"><label class="c-form-radio__label"
                                                        for="unknown">Unknown</label></div>
                                            </div>
                                        </li>
                                    </ul>
                                    <div class="c-form-stepper__actions"><button class="c-button" type="submit"
                                            disabled="">Calculate</button></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </form><button class="c-button c-button--secondary u-spacing-top-small">Reset</button>
                <div class="u-spacing-top-medium">
                    <div class="c-panel false false"><button class="c-panel__header" type="button"><span
                                class="c-panel__header-inner">Disclaimer</span><span class="c-arrow"></span></button>
                        <div class="c-panel__content">
                            <p>This Australian Absolute cardiovascular disease risk calculator has been produced by the
                                National Vascular Disease Prevention Alliance for the information of health
                                professionals. The statements and recommendations it contains are, unless labelled as
                                'expert opinion', based on independent review of the available evidence. Interpretation
                                of the results of this calculator by those without appropriate medical and/or clinical
                                training is not recommended, other than at the request of, or in consultation with, a
                                relevant health professional.</p>
                            <p>While care has been taken in preparing the content of this material, the National
                                Vascular Disease Prevention Alliance and their employees cannot accept any liability,
                                including for any loss or damage, resulting from the reliance on the content, or for its
                                accuracy, currency and completeness. This material may be found in third parties'
                                programs or materials. This does not imply an endorsement or recommendation by the
                                National Vascular Disease Prevention Alliance for such third parties' organisations,
                                products or services, including these parties' materials or information. Any use of
                                National Vascular Disease Prevention Alliance material by another person or organisation
                                is done so at the user's own risk. The entire contents of this material are subject to
                                copyright protection.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

    <br>

    <br>
    <label class="c-form-label" for="bloodPressure">Systolic Blood Pressure</label>
  </div>
</template>

<script>
export default {
  data() {
    return {
      Male: true,
      Female:true
    };
  },
  computed: {
    btnStates() {
      return this.buttons.map(btn => btn.state);
    }
  }
};

// import axios from "axios";
// export default {
//   data() {
//     return {
//       data: []
//     };
//   },
//   methods: {
//     getMessage() {
//       const path = "http://localhost:5000/datasets/blood";
//       axios
//         .get(path)
//         .then(res => {
//           this.data = res.data.datasets;
//         })
//         .catch(error => {
//           // eslint-disable-next-line
//           console.error(error);
//         });
//     }
//   },
//   created() {
//     this.getMessage();
//   }
// };
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Montserrat:400,700,800); .clearfix {
    zoom:1}

.clearfix:after,.clearfix:before {
    content: "";
    display: table
}

.clearfix:after {
    clear: both
}

.s-example {
    display: block;
    content: "";
    background-position: 0 0;
    width: 32px;
    height: 32px
}

.svg-arrow-left,.svg-arrow-right,.svg-chevron-down,.svg-chevron-left,.svg-chevron-right,.svg-chevron-up,.svg-google-plus,.svg-instagram,.svg-pinterest,.svg-search,.svg-share,.svg-tick,.svg-twitter,.svg-vimeo,.svg-youtube {
    display: inline-block;
    height: 100px;
    width: 100px
}

/*! normalize.css v3.0.2 | MIT License | git.io/normalize */
html {
    font-family: sans-serif;
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%
}

body {
    margin: 0
}

article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary {
    display: block
}

audio,canvas,progress,video {
    display: inline-block;
    vertical-align: baseline
}

audio:not([controls]) {
    display: none;
    height: 0
}

[hidden],template {
    display: none
}

a {
    background-color: transparent
}

a:active,a:hover {
    outline: 0
}

abbr[title] {
    border-bottom: 1px dotted
}

b,strong {
    font-weight: 700
}

dfn {
    font-style: italic
}

h1 {
    font-size: 2em;
    margin: .67em 0
}

mark {
    background: #ff0;
    color: #000
}

small {
    font-size: 80%
}

sub,sup {
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline
}

sup {
    top: -.5em
}

sub {
    bottom: -.25em
}

img {
    border: 0
}

svg:not(:root) {
    overflow: hidden
}

figure {
    margin: 1em 40px
}

hr {
    box-sizing: content-box;
    height: 0
}

pre {
    overflow: auto
}

code,kbd,pre,samp {
    font-family: monospace,monospace;
    font-size: 1em
}

button,input,optgroup,select,textarea {
    color: inherit;
    font: inherit;
    margin: 0
}

button {
    overflow: visible
}

button,select {
    text-transform: none
}

button,html input[type=button],input[type=reset],input[type=submit] {
    -webkit-appearance: button;
    cursor: pointer
}

button[disabled],html input[disabled] {
    cursor: default
}

button::-moz-focus-inner,input::-moz-focus-inner {
    border: 0;
    padding: 0
}

input {
    line-height: normal
}

input[type=checkbox],input[type=radio] {
    box-sizing: border-box;
    padding: 0
}

input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button {
    height: auto
}

input[type=search] {
    -webkit-appearance: textfield;
    box-sizing: content-box
}

input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration {
    -webkit-appearance: none
}

fieldset {
    border: 1px solid silver;
    margin: 0 2px;
    padding: .35em .625em .75em
}

legend {
    border: 0;
    padding: 0
}

textarea {
    overflow: auto
}

optgroup {
    font-weight: 700
}

table {
    border-collapse: collapse;
    border-spacing: 0
}

td,th {
    padding: 0
}

*,:after,:before {
    box-sizing: border-box
}

:focus {
    outline: 1px dotted #f1f1f1
}

::selection {
    color: #fff;
    background: #37383c
}

::-moz-selection {
    color: #fff;
    background: #37383c
}

body,html {
    -moz-osx-font-smoothing: auto;
    -moz-osx-font-smoothing: grayscale;
    -webkit-backface-visibility: hidden;
    -webkit-font-smoothing: antialiased!important;
    color: #37383c;
    font-family: Montserrat,sans-serif;
    font-size: 16px;
    font-weight: 400;
    line-height: 1.6;
    min-width: 320px;
    position: relative;
    text-rendering: optimizeLegibility!important;
    width: 100%;
    z-index: 0
}

body {
    font-size: 16px;
    font-size: 1rem
}

a[href*="mailto:"] {
    word-wrap: break-word
}

button {
    background-color: transparent;
    outline: none
}

h1,h2,h3,h4,h5,h6 {
    margin-top: 0
}

ol,ul {
    list-style: none;
    margin: 0;
    padding: 0
}

a {
    text-decoration: none;
    color: #5470e0
}

a:hover {
    text-decoration: underline
}

p {
    margin-top: 0;
    margin-bottom: 20px;
    margin-bottom: 1.25rem
}

p b,p strong {
    font-weight: 600
}

p em,p i {
    font-style: italic
}

[class^=c-btn],a,button,input[type=text],textarea {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429;
    transition-duration: .5s;
    transition-property: background-color,color,opacity,border,border-color,background-position,outline,box-shadow,border-bottom,text-decoration,left,top,transform;
    transition-timing-function: cubic-bezier(.5,0,.5,1);
    transform-origin: center center
}

@media (min-width: 900px) {
    [class^=c-btn],a,button,input[type=text],textarea {
        font-size:1rem;
        line-height: 1.375
    }
}

form fieldset {
    border: none;
    padding: 0
}

form ol {
    zoom:1}

form ol:after,form ol:before {
    content: "";
    display: table
}

form ol:after {
    clear: both
}

form ol li {
    zoom:1;margin-bottom: 20px;
    margin-bottom: 1.25rem
}

form ol li:after,form ol li:before {
    content: "";
    display: table
}

form ol li:after {
    clear: both
}

button {
    background: none;
    border: none;
    padding: 0
}

img {
    display: block;
    height: auto;
    max-width: 100%
}

figure {
    margin: 0
}

@media print {
    * {
        background: transparent!important;
        color: #000!important;
        box-shadow: none!important;
        text-shadow: none!important
    }

    a,a:visited {
        text-decoration: underline
    }

    a[href]:after {
        content: " (" attr(href) ")"
    }

    abbr[title]:after {
        content: " (" attr(title) ")"
    }

    .ir a:after,a[href^="#"]:after,a[href^="javascript:"]:after {
        content: ""
    }

    blockquote,pre {
        border: 1px solid #999;
        page-break-inside: avoid
    }

    thead {
        display: table-header-group
    }

    img,tr {
        page-break-inside: avoid
    }

    img {
        max-width: 100%!important
    }

    @page {
        margin: .5cm
    }

    h2,h3,p {
        orphans: 3;
        widows: 3
    }

    h2,h3 {
        page-break-after: avoid
    }
}

.o-col {
    display: inline-block;
    width: 100%
}

@media (min-width: 900px) {
    .o-col {
        -ms-flex:0 0 8.33333%;
        flex: 0 0 8.33333%;
        width: 8.33333%
    }
}

.o-col__inner {
    padding: 0 0 20px
}

@media (min-width: 900px) {
    .o-col__inner {
        padding:0 10px 20px
    }
}

.o-col--1 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--1 {
        -ms-flex:0 0 8.33333%;
        flex: 0 0 8.33333%;
        width: 8.33333%
    }
}

.o-col--2 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--2 {
        -ms-flex:0 0 16.66667%;
        flex: 0 0 16.66667%;
        width: 16.66667%
    }
}

.o-col--3 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--3 {
        -ms-flex:0 0 25%;
        flex: 0 0 25%;
        width: 25%
    }
}

.o-col--4 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--4 {
        -ms-flex:0 0 33.33333%;
        flex: 0 0 33.33333%;
        width: 33.33333%
    }
}

.o-col--5 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--5 {
        -ms-flex:0 0 41.66667%;
        flex: 0 0 41.66667%;
        width: 41.66667%
    }
}

.o-col--6 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--6 {
        -ms-flex:0 0 50%;
        flex: 0 0 50%;
        width: 50%
    }
}

.o-col--7 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--7 {
        -ms-flex:0 0 58.33333%;
        flex: 0 0 58.33333%;
        width: 58.33333%
    }
}

.o-col--8 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--8 {
        -ms-flex:0 0 66.66667%;
        flex: 0 0 66.66667%;
        width: 66.66667%
    }
}

.o-col--9 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--9 {
        -ms-flex:0 0 75%;
        flex: 0 0 75%;
        width: 75%
    }
}

.o-col--10 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--10 {
        -ms-flex:0 0 83.33333%;
        flex: 0 0 83.33333%;
        width: 83.33333%
    }
}

.o-col--11 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--11 {
        -ms-flex:0 0 91.66667%;
        flex: 0 0 91.66667%;
        width: 91.66667%
    }
}

.o-col--12 {
    width: 100%
}

@media (min-width: 900px) {
    .o-col--12 {
        -ms-flex:0 0 100%;
        flex: 0 0 100%;
        width: 100%
    }
}

.o-col--1\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--1\@large {
        -ms-flex:0 0 8.33333%;
        flex: 0 0 8.33333%;
        width: 8.33333%
    }
}

.o-col--2\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--2\@large {
        -ms-flex:0 0 16.66667%;
        flex: 0 0 16.66667%;
        width: 16.66667%
    }
}

.o-col--3\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--3\@large {
        -ms-flex:0 0 25%;
        flex: 0 0 25%;
        width: 25%
    }
}

.o-col--4\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--4\@large {
        -ms-flex:0 0 33.33333%;
        flex: 0 0 33.33333%;
        width: 33.33333%
    }
}

.o-col--5\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--5\@large {
        -ms-flex:0 0 41.66667%;
        flex: 0 0 41.66667%;
        width: 41.66667%
    }
}

.o-col--6\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--6\@large {
        -ms-flex:0 0 50%;
        flex: 0 0 50%;
        width: 50%
    }
}

.o-col--7\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--7\@large {
        -ms-flex:0 0 58.33333%;
        flex: 0 0 58.33333%;
        width: 58.33333%
    }
}

.o-col--8\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--8\@large {
        -ms-flex:0 0 66.66667%;
        flex: 0 0 66.66667%;
        width: 66.66667%
    }
}

.o-col--9\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--9\@large {
        -ms-flex:0 0 75%;
        flex: 0 0 75%;
        width: 75%
    }
}

.o-col--10\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--10\@large {
        -ms-flex:0 0 83.33333%;
        flex: 0 0 83.33333%;
        width: 83.33333%
    }
}

.o-col--11\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--11\@large {
        -ms-flex:0 0 91.66667%;
        flex: 0 0 91.66667%;
        width: 91.66667%
    }
}

.o-col--12\@large {
    width: 100%
}

@media (min-width: 1200px) {
    .o-col--12\@large {
        -ms-flex:0 0 100%;
        flex: 0 0 100%;
        width: 100%
    }
}

@media (min-width: 900px) {
    .o-col--offset-1 {
        margin-left:8.33333%
    }
}

@media (min-width: 900px) {
    .o-col--offset-2 {
        margin-left:16.66667%
    }
}

@media (min-width: 900px) {
    .o-col--offset-3 {
        margin-left:25%
    }
}

@media (min-width: 900px) {
    .o-col--offset-4 {
        margin-left:33.33333%
    }
}

@media (min-width: 900px) {
    .o-col--offset-5 {
        margin-left:41.66667%
    }
}

@media (min-width: 900px) {
    .o-col--offset-6 {
        margin-left:50%
    }
}

@media (min-width: 900px) {
    .o-col--offset-7 {
        margin-left:58.33333%
    }
}

@media (min-width: 900px) {
    .o-col--offset-8 {
        margin-left:66.66667%
    }
}

@media (min-width: 900px) {
    .o-col--offset-9 {
        margin-left:75%
    }
}

@media (min-width: 900px) {
    .o-col--offset-10 {
        margin-left:83.33333%
    }
}

@media (min-width: 900px) {
    .o-col--offset-11 {
        margin-left:91.66667%
    }
}

@media (min-width: 900px) {
    .o-col--offset-12 {
        margin-left:100%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-1\@large {
        margin-left:8.33333%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-2\@large {
        margin-left:16.66667%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-3\@large {
        margin-left:25%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-4\@large {
        margin-left:33.33333%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-5\@large {
        margin-left:41.66667%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-6\@large {
        margin-left:50%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-7\@large {
        margin-left:58.33333%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-8\@large {
        margin-left:66.66667%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-9\@large {
        margin-left:75%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-10\@large {
        margin-left:83.33333%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-11\@large {
        margin-left:91.66667%
    }
}

@media (min-width: 1200px) {
    .o-col--offset-12\@large {
        margin-left:100%
    }
}

.o-col--no-bottom-padding .o-col__inner {
    padding-bottom: 0
}

.o-container {
    display: block;
    max-width: 1460px;
    padding: 0 20px;
    padding: 0 1.25rem;
    margin: 0 auto
}

@media (min-width: 900px) {
    .o-container {
        max-width:1460px
    }
}

.o-grid {
    -ms-flex-line-pack: start;
    align-content: start;
    -ms-flex-align: stretch;
    align-items: stretch;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    -ms-flex-pack: start;
    justify-content: start
}

@media (min-width: 900px) {
    .o-grid {
        margin:0 -10px
    }
}

.o-grid--center {
    -ms-flex-pack: center;
    justify-content: center
}

.o-section {
    display: block;
    padding: 40px 0;
    padding: 2.5rem 0
}

.o-section--small-padding\@small {
    padding: 20px 0;
    padding: 1.25rem 0
}

@media (min-width: 900px) {
    .o-section--small-padding\@small {
        padding:2.5rem 0
    }
}

.c-arrow {
    height: 1px;
    height: .0625rem;
    background: #5470e0;
    display: inline-block;
    width: 10px;
    width: .625rem;
    position: relative;
    vertical-align: middle
}

@media (min-width: 900px) {
    .c-arrow {
        width:.75rem
    }
}

.c-arrow:before {
    height: 1px;
    height: .0625rem;
    background: #5470e0;
    display: inline-block;
    width: 10px;
    width: .625rem;
    position: relative;
    vertical-align: middle;
    content: "";
    position: absolute;
    left: 0;
    transform-origin: left;
    width: 8px;
    width: .5rem;
    transform: rotate(45deg)
}

@media (min-width: 900px) {
    .c-arrow:before {
        width:.75rem;
        width: .625rem
    }
}

.c-arrow:after {
    height: 1px;
    height: .0625rem;
    background: #5470e0;
    display: inline-block;
    width: 10px;
    width: .625rem;
    position: relative;
    vertical-align: middle;
    content: "";
    position: absolute;
    left: 0;
    transform-origin: left;
    width: 8px;
    width: .5rem;
    transform: rotate(-45deg)
}

@media (min-width: 900px) {
    .c-arrow:after {
        width:.75rem;
        width: .625rem
    }
}

.c-arrow--white,.c-arrow--white:after,.c-arrow--white:before {
    background-color: #fff
}

.c-arrow--inline {
    transform: translateY(-.0625rem);
    margin-right: 20px;
    margin-right: 1.25rem
}

.c-button {
    font-family: Montserrat,sans-serif;
    font-size: 12px;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .08333em;
    line-height: 1.16667;
    text-transform: uppercase
}

.c-button,.c-button:link,.c-button:visited {
    -webkit-appearance: none;
    background-color: #5470e0;
    border-radius: 0;
    border: 1px solid transparent;
    border: .0625rem solid transparent;
    color: #fff;
    display: inline-block;
    margin: 0;
    padding: 19px 20px 17px;
    padding: 1.1875rem 1.25rem 1.0625rem;
    position: relative;
    text-align: center;
    transition: background-color .3s cubic-bezier(.5,0,.5,1) 0s,color .3s cubic-bezier(.5,0,.5,1) 0s;
    vertical-align: middle;
    width: 100%
}

@media (min-width: 900px) {
    .c-button,.c-button:link,.c-button:visited {
        padding:1.5rem 3.125rem 1.25rem
    }
}

.c-button:hover {
    background-color: #111a3d
}

.c-button:disabled {
    opacity: .3;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=30)"
}

.c-button:disabled:hover {
    background-color: #5470e0
}

@media (min-width: 900px) {
    .c-button {
        font-size:.875rem;
        line-height: 1.21429
    }
}

.c-button--secondary,.c-button--secondary:link,.c-button--secondary:visited {
    background-color: transparent;
    border-color: #566be2;
    color: #5470e0
}

.c-button--secondary:hover {
    background-color: #5470e0;
    color: #fff
}

.c-button--secondary:hover:disabled {
    background-color: transparent;
    color: #5470e0
}

.c-external-link {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429;
    -ms-flex-align: center;
    align-items: center;
    border-bottom: 1px solid #d7d7d8;
    border-bottom: .0625rem solid #d7d7d8;
    border-top: 1px solid #d7d7d8;
    border-top: .0625rem solid #d7d7d8;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-pack: justify;
    justify-content: space-between;
    margin: 16px 0 32px;
    margin: 1rem 0 2rem;
    padding: 15px 0;
    padding: .9375rem 0;
    width: 100%
}

@media (min-width: 900px) {
    .c-external-link {
        font-size:1rem;
        line-height: 1.375
    }
}

.c-external-link svg {
    height: 13px;
    height: .8125rem;
    width: 13px;
    width: .8125rem
}

.c-external-link--error {
    color: #e82a2a
}

.c-external-link--error svg {
    fill: #e82a2a
}

.c-footer {
    background: #111a3d;
    color: #fff
}

@media print {
    .c-footer {
        display: none
    }
}

.c-footer__container {
    display: block;
    max-width: 1460px;
    padding: 0 20px;
    padding: 0 1.25rem;
    margin: 0 auto;
    padding: 15px 20px;
    padding: .9375rem 1.25rem
}

@media (min-width: 900px) {
    .c-footer__container {
        max-width:1460px;
        max-width: 1216.66667px;
        padding: 2.5rem 1.25rem
    }
}

.c-footer__logos {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    margin: 0
}

.c-footer__logos dt {
    font-family: Montserrat,sans-serif;
    font-size: 12px;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .08333em;
    line-height: 1.16667;
    text-transform: uppercase;
    -ms-flex: 1 0 100%;
    flex: 1 0 100%;
    margin: 20px 0;
    margin: 1.25rem 0;
    width: 100%
}

@media (min-width: 900px) {
    .c-footer__logos dt {
        margin:0 0 1.25rem
    }
}

.c-footer__logos dd {
    -ms-flex-align: center;
    align-items: center;
    display: -ms-flexbox;
    display: flex;
    -ms-flex: 1 0 50%;
    flex: 1 0 50%;
    margin: 0 0 20px;
    margin: 0 0 1.25rem;
    width: 50%
}

@media (min-width: 600px) {
    .c-footer__logos dd {
        -ms-flex:0 0 auto;
        flex: 0 0 auto;
        width: auto;
        margin: 0;
        height: 3.75rem
    }
}

.c-footer__logos a {
    transition: opacity .3s cubic-bezier(.5,0,.5,1) 0s
}

@media (min-width: 600px) {
    .c-footer__logos a {
        margin-top:auto
    }
}

.c-footer__logos a:hover {
    opacity: .5;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)"
}

.c-footer__logo {
    max-height: 64px;
    max-height: 4rem
}

.c-footer__logo,.c-footer__logo-landscape {
    display: block;
    margin-right: 30px;
    margin-right: 1.875rem
}

.c-footer__logo-landscape {
    max-width: 140px;
    max-width: 8.75rem
}

.c-footer__svg-heart svg {
    width: 70px;
    width: 4.375rem
}

.c-footer__svg-diabetes svg,.c-footer__svg-heart svg {
    display: block;
    fill: #fff;
    height: 60px;
    height: 3.75rem;
    margin-right: 30px;
    margin-right: 1.875rem
}

.c-footer__svg-diabetes svg {
    width: 100px;
    width: 6.25rem;
    margin-top: -30px;
    margin-top: -1.875rem
}

@media (min-width: 600px) {
    .c-footer__svg-diabetes svg {
        margin-top:0
    }
}

.c-footer__svg-stroke svg {
    display: block;
    fill: #fff;
    height: 60px;
    height: 3.75rem;
    margin-right: 30px;
    margin-right: 1.875rem;
    width: 107px;
    width: 6.6875rem
}

.c-form-checkbox__input {
    left: -9999em;
    position: absolute
}

.c-form-checkbox__input:checked+.c-form-checkbox__label:before {
    background-color: #000
}

.c-form-checkbox__input:checked+.c-form-checkbox__label:after {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)"
}

.c-form-checkbox__label {
    color: #37383c;
    cursor: pointer;
    font-size: .875em;
    font-weight: 400;
    letter-spacing: 0;
    line-height: 1.6em;
    padding-left: 35px;
    position: relative;
    text-transform: none
}

.c-form-checkbox__label:before {
    background: #fff;
    border-radius: 2px;
    border: 1px solid #000;
    content: ".";
    cursor: pointer;
    height: 20px;
    left: 0;
    transform: translateY(-50%);
    position: absolute;
    text-indent: -999em;
    top: 50%;
    transition: background .2s ease-in-out;
    width: 20px
}

.c-form-checkbox__label:after {
    background-image: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMTAwIDEwMCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTAwIDEwMDsiIHhtbDpzcGFjZT0icHJlc2VydmUiPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+LnN0MHtmaWxsOiNGRkZGRkY7fTwvc3R5bGU+PHBhdGggY2xhc3M9InN0MCIgZD0iTTk2LjksNi42Yy0xLjctMS40LTMuOS0yLTYuMS0xLjhjLTIuMiwwLjItNC4yLDEuMy01LjYsMy4xTDMxLjUsNzQuNUwxNC4yLDU3LjJDMTEsNTQsNS43LDU0LDIuNCw1Ny4yYy0zLjIsMy4yLTMuMiw4LjUsMCwxMS44bDIzLjgsMjMuOGMxLjYsMS42LDMuNywyLjQsNi4zLDIuNGwwLDBjMi40LTAuMSw0LjYtMS4zLDYtMy4xTDk4LDE4LjNDMTAxLDE0LjgsMTAwLjUsOS41LDk2LjksNi42eiIvPjwvc3ZnPg==);
    background-position: 50%;
    background-repeat: no-repeat;
    background-size: contain;
    content: "";
    display: block;
    height: 10px;
    height: .625rem;
    opacity: 0;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    position: absolute;
    top: 50%;
    transform: translate(50%,-50%);
    width: 10px;
    width: .625rem
}

.c-form-error {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429;
    color: #e82a2a;
    display: block;
    margin: 0;
    padding-top: 16px;
    padding-top: 1rem
}

@media (min-width: 900px) {
    .c-form-error {
        font-size:1rem;
        line-height: 1.375
    }
}

.c-form-error--no-top-padding {
    padding-top: 0
}

.c-form-label {
    font-family: Montserrat,sans-serif;
    font-size: 12px;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .08333em;
    line-height: 1.16667;
    text-transform: uppercase;
    display: block;
    margin-bottom: 10px;
    margin-bottom: .625rem;
    color: #37383c;
    opacity: .7;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=70)"
}

@media (min-width: 900px) {
    .c-form-label {
        font-size:.875rem;
        line-height: 1.21429
    }
}

.c-form-radio {
    display: inline-block;
    margin: 0 1px;
    margin: 0 .0625rem;
    width: calc(50% - 2px)
}

.c-form-radio__label {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429;
    background-color: #f3f3f6;
    cursor: pointer;
    display: block;
    padding: 16px;
    padding: 1rem;
    position: relative;
    text-align: center;
    text-transform: none;
    transition: background-color .3s cubic-bezier(.5,0,.5,1),color .3s cubic-bezier(.5,0,.5,1);
    width: 100%
}

@media (min-width: 900px) {
    .c-form-radio__label {
        font-size:1rem;
        line-height: 1.375
    }
}

.c-form-radio__label:hover {
    background-color: #d7d7d8
}

.c-form-radio__label svg {
    display: block;
    fill: #37383c;
    height: 30px;
    height: 1.875rem;
    margin: 0 auto 4px;
    margin: 0 auto .25rem;
    transition: fill .3s cubic-bezier(.5,0,.5,1);
    width: 25px;
    width: 1.5625rem
}

.c-form-radio__input {
    left: -9999em;
    position: absolute
}

.c-form-radio__input:focus+.c-form-radio__label {
    background-color: #d7d7d8
}

.c-form-radio__input:checked+.c-form-radio__label {
    background-color: #566be2;
    color: #fff
}

.c-form-radio__input:checked+.c-form-radio__label svg {
    fill: #fff
}

.c-form-radio--third {
    width: calc(33% - 2px)
}

.c-form-select {
    background-color: #f1f1f1;
    border: 1px solid #eee;
    color: #37383c;
    cursor: pointer;
    display: block;
    font-size: .875em;
    margin: 0;
    padding: 0;
    position: relative
}

.c-form-select.parsley-error {
    border-color: #000
}

.c-form-select:before {
    background-image: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iNTAwcHgiIGhlaWdodD0iNTAwcHgiIHZpZXdCb3g9IjAgMCA1MDAgNTAwIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MDAgNTAwOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+PHBhdGggZD0iTTQxNC44LDExNC40TDMwMC4zLDIyOS41bC01MCw0OS41bC01MC00OS41TDg1LjcsMTE0LjRjLTEwLTEwLTIyLjUtMTQuNS0zNS41LTE0LjVzLTI1LjUsNS0zNS41LDE0LjVjLTE5LjUsMTkuNS0xOS41LDUxLjUsMCw3MWwyMDAuMSwyMDAuMWMyMSwyMC41LDUyLjUsMTguNSw3MC41LDBsMjAwLjEtMjAwLjFjMTkuNS0xOS41LDE5LjUtNTEsMC03MC41QzQ2Ni40LDk0LjksNDM0LjMsOTQuOSw0MTQuOCwxMTQuNHoiLz48L3N2Zz4=);
    background-position: 50%;
    background-repeat: no-repeat;
    background-size: .75rem auto;
    content: "";
    display: block;
    font-size: 11px;
    font-size: .6875rem;
    height: 100%;
    line-height: 1;
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 50px;
    width: 3.125rem
}

.lt-ie10 .c-form-select:before {
    display: none
}

.c-form-select select::-ms-expand {
    display: none
}

.c-form-select__input {
    -moz-appearance: none;
    -webkit-appearance: none;
    appearance: none;
    background-color: transparent;
    background-image: none;
    border: none;
    box-shadow: none;
    color: #37383c;
    cursor: pointer;
    font-size: 14px;
    font-size: .875rem;
    line-height: normal;
    line-height: 1;
    padding: 16px 15px;
    padding: 1rem .9375rem;
    position: relative;
    width: 100%
}

.lt-ie10 .c-form-select__input {
    padding: 11px;
    padding: .6875rem
}

.c-form-stepper {
    width: 100%
}

.c-form-stepper__field {
    padding-bottom: 24px;
    padding-bottom: 1.5rem
}

.c-form-text {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429;
    position: relative
}

@media (min-width: 900px) {
    .c-form-text {
        font-size:1rem;
        line-height: 1.375
    }
}

.c-form-text input,.c-form-text textarea {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    background: #f3f3f6;
    border-radius: 0;
    border: 1px solid #f3f3f6;
    color: #37383c;
    padding: 16px 80px 16px 15px;
    padding: 1rem 5rem 1rem .9375rem;
    transition: border-color .3s cubic-bezier(.5,0,.5,1),background-color .3s cubic-bezier(.5,0,.5,1);
    width: 100%
}

.c-form-text input::-webkit-input-placeholder,.c-form-text textarea::-webkit-input-placeholder {
    color: #37383c;
    opacity: .8;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=80)"
}

.c-form-text input:-ms-input-placeholder,.c-form-text textarea:-ms-input-placeholder {
    color: #37383c;
    opacity: .8;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=80)"
}

.c-form-text input::placeholder,.c-form-text textarea::placeholder {
    color: #37383c;
    opacity: .8;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=80)"
}

.c-form-text input:hover,.c-form-text textarea:hover {
    background-color: #d7d7d8
}

.c-form-text input:focus,.c-form-text textarea:focus {
    outline: none;
    border-color: #5470e0
}

.c-form-text input:disabled,.c-form-text textarea:disabled {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)"
}

.has-error .c-form-text input,.has-error .c-form-text textarea {
    border-color: #e82a2a
}

.c-form-text input[type=number],.c-form-text textarea[type=number] {
    -moz-appearance: textfield
}

.c-form-text input[type=number]::-webkit-inner-spin-button,.c-form-text input[type=number]::-webkit-outer-spin-button,.c-form-text textarea[type=number]::-webkit-inner-spin-button,.c-form-text textarea[type=number]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0
}

.c-form-text__suffix {
    position: absolute;
    right: 16px;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%)
}

.c-header {
    background: linear-gradient(315deg,#7bbbeb,#566be2);
    color: #fff
}

.c-header__container {
    display: block;
    max-width: 1460px;
    padding: 0 20px;
    padding: 0 1.25rem;
    margin: 0 auto;
    padding: 30px 20px;
    padding: 1.875rem 1.25rem
}

@media (min-width: 900px) {
    .c-header__container {
        max-width:1460px;
        padding: 2.5rem 1.25rem
    }
}

@media print {
    .c-header__container {
        padding: 1.25rem
    }
}

.c-header__back {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429
}

@media (min-width: 900px) {
    .c-header__back {
        font-size:1rem;
        line-height: 1.375
    }
}

@media (min-width: 1200px) {
    .c-header__back {
        margin-left:8.33333%
    }
}

.c-header__back,.c-header__back:link,.c-header__back:visited {
    color: #fff;
    display: inline-block;
    margin-bottom: 20px;
    margin-bottom: 1.25rem
}

@media print {
    .c-header__back,.c-header__back:link,.c-header__back:visited {
        display: none
    }
}

.c-header__back:hover {
    text-decoration: underline
}

.c-header__title {
    font-family: Montserrat,sans-serif;
    font-size: 24px;
    font-size: 1.5rem;
    font-weight: 800;
    line-height: 1.25;
    margin: 0
}

@media (min-width: 900px) {
    .c-header__title {
        font-size:2.25rem;
        line-height: 1.36842
    }
}

@media (min-width: 1200px) {
    .c-header__title {
        margin-left:8.33333%
    }
}

.c-header--narrow .c-header__back,.c-header--narrow .c-header__title {
    margin-left: 0
}

@media (min-width: 900px) {
    .c-header--narrow .c-header__container {
        max-width:730px
    }
}

.c-list {
    list-style-type: none;
    margin-bottom: 30px;
    margin-bottom: 1.875rem;
    padding: 0;
    position: relative;
    overflow: hidden
}

.c-list li {
    margin-bottom: 10px;
    margin-bottom: .625rem;
    padding-left: 30px;
    padding-left: 1.875rem;
    position: relative
}

.c-list li:before {
    color: #000;
    display: inline-block;
    left: 0;
    line-height: 1;
    position: absolute;
    top: 0;
    vertical-align: middle
}

.c-list--unordered li:before {
    content: ".";
    font-size: 35px;
    font-size: 2.1875rem;
    line-height: 10px;
    top: -.07em
}

.c-list--ordered {
    counter-reset: a
}

.c-list--ordered li:before {
    content: counter(a,decimal) ".";
    counter-increment: a;
    font-weight: 600;
    left: 0;
    top: .275em
}

.c-list--ordered ol li:before {
    content: counter(a)
}

.c-panel {
    border-bottom: 1px solid #d7d7d8;
    border-bottom: .0625rem solid #d7d7d8;
    border-top: 1px solid #d7d7d8;
    border-top: .0625rem solid #d7d7d8;
    margin-top: -1px;
    margin-top: -.0625rem;
    padding-top: 15px;
    padding-top: .9375rem
}

.c-panel__header {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429;
    -ms-flex-align: center;
    align-items: center;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-pack: justify;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 15px;
    margin-bottom: .9375rem
}

@media (min-width: 900px) {
    .c-panel__header {
        font-size:1rem;
        line-height: 1.375
    }
}

.c-panel__header:focus,.c-panel__header:hover {
    outline: none
}

.c-panel__header .c-arrow {
    transform: rotate(270deg)
}

.is-open .c-panel__header .c-arrow {
    transform: rotate(90deg)
}

.c-panel__header:focus .c-panel__header-inner,.c-panel__header:hover .c-panel__header-inner {
    border-color: #37383c
}

.c-panel__header-inner,.c-panel__header-inner:link,.c-panel__header-inner:visited {
    border-bottom: 1px solid transparent;
    transition: border-color .3s cubic-bezier(.5,0,.5,1) 0s
}

.c-panel__header-inner:hover {
    border-color: #37383c
}

.c-panel__content {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429;
    margin: 20px 0;
    margin: 1.25rem 0
}

@media (min-width: 900px) {
    .c-panel__content {
        font-size:1rem;
        line-height: 1.375
    }
}

.js .c-panel__content {
    display: none
}

@media print {
    .js .c-panel__content {
        display: block
    }
}

.is-open .c-panel__content {
    display: block
}

.c-panel__content p {
    margin-bottom: 15px;
    margin-bottom: .9375rem
}

.c-panel__content dl {
    -ms-flex-align: center;
    align-items: center;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-pack: justify;
    justify-content: space-between;
    margin-bottom: 10px;
    margin-bottom: .625rem
}

.c-panel__content dd,.c-panel__content dt {
    padding: 0
}

.c-panel__content :last-child {
    margin-bottom: 0
}

.c-panel--margin-bottom {
    margin-bottom: 24px;
    margin-bottom: 1.5rem
}

.c-result-graphic {
    -ms-flex-align: center;
    align-items: center;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-pack: justify;
    justify-content: space-between;
    margin-bottom: 20px;
    margin-bottom: 1.25rem;
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429
}

@media (min-width: 900px) {
    .c-result-graphic {
        -ms-flex-align:top;
        align-items: top
    }
}

@media print {
    .c-result-graphic {
        max-width: 25rem;
        page-break-inside: avoid
    }
}

@media (min-width: 900px) {
    .c-result-graphic {
        font-size:1rem;
        line-height: 1.375
    }
}

.c-result-graphic__percentage {
    font-family: Montserrat,sans-serif;
    font-weight: 800;
    font-size: 36px;
    font-size: 2.25rem;
    line-height: 1.38095;
    margin-bottom: 0;
    transform: translateY(.4375rem)
}

@media (min-width: 900px) {
    .c-result-graphic__percentage {
        font-size:4rem;
        line-height: 1.34375;
        transform: translateY(-.25rem)
    }
}

.c-result-graphic__chart {
    white-space: nowrap
}

.c-result-graphic__chart li {
    display: inline-block;
    text-align: center;
    width: 70px;
    width: 4.375rem
}

.c-result-graphic__chart li,.c-result-graphic__chart li:last-child {
    margin-right: 1px;
    margin-right: .0625rem
}

.c-result-graphic__chart li svg {
    display: block;
    fill: #f3f3f6;
    height: 70px;
    height: 4.375rem;
    width: 70px;
    width: 4.375rem;
    margin-bottom: 10px;
    margin-bottom: .625rem
}

.c-result-graphic__chart li svg.is-green {
    fill: #55af27
}

.c-result-graphic__chart li svg.is-yellow {
    fill: #fbce2f
}

.c-result-graphic__chart li svg.is-red {
    fill: #e82a2a
}

.c-result-graphic--low .c-result-graphic__percentage {
    color: #55af27
}

.c-result-graphic--moderate .c-result-graphic__percentage {
    color: #fbce2f
}

.c-result-graphic--high .c-result-graphic__percentage {
    color: #e82a2a
}

.u-visually-hidden {
    border: 0!important;
    clip: rect(1px 1px 1px 1px);
    clip: rect(1px,1px,1px,1px);
    height: 1px!important;
    overflow: hidden;
    padding: 0!important;
    position: absolute!important;
    width: 1px!important
}

.u-skip-to-content {
    left: 0;
    margin-left: -9999em;
    position: absolute;
    top: 0
}

.u-skip-to-content:focus {
    margin-left: 0
}

.u-block.u-block {
    display: block
}

.u-inline-block.u-inline-block {
    display: inline-block
}

.u-block\@medium.u-block\@medium {
    display: block
}

.u-inline-block\@medium.u-inline-block\@medium {
    display: inline-block
}

@media (min-width: 900px) {
    .u-float-left\@medium.u-float-left\@medium {
        float:left!important
    }
}

@media (min-width: 900px) {
    .u-float-right\@medium.u-float-right\@medium {
        float:right!important
    }
}

.u-clearfix.u-clearfix {
    zoom:1}

.u-clearfix.u-clearfix:after,.u-clearfix.u-clearfix:before {
    content: "";
    display: table
}

.u-clearfix.u-clearfix:after {
    clear: both
}

.u-show\@xlarge.u-show\@xlarge {
    display: none
}

@media (min-width: 1400px) {
    .u-show\@xlarge.u-show\@xlarge {
        display:block
    }
}

@media (min-width: 1400px) {
    .u-hide\@xlarge.u-hide\@xlarge {
        display:none
    }
}

.u-show\@large.u-show\@large {
    display: none
}

@media (min-width: 1200px) {
    .u-show\@large.u-show\@large {
        display:block
    }
}

@media (min-width: 1200px) {
    .u-hide\@large.u-hide\@large {
        display:none
    }
}

.u-show\@medium.u-show\@medium {
    display: none
}

@media (min-width: 900px) {
    .u-show\@medium.u-show\@medium {
        display:block
    }
}

@media (min-width: 900px) {
    .u-hide\@medium.u-hide\@medium {
        display:none
    }
}

.u-show\@small.u-show\@small {
    display: none
}

@media (min-width: 600px) {
    .u-show\@small.u-show\@small {
        display:block
    }
}

@media (min-width: 600px) {
    .u-hide\@small.u-hide\@small {
        display:none
    }
}

@media print {
    .u-hide\@print.u-hide\@print {
        display: none
    }
}

.u-spacing-top-zero.u-spacing-top-zero {
    margin-top: 0
}

.u-spacing-bottom-zero.u-spacing-bottom-zero {
    margin-bottom: 0
}

.u-spacing-top-small.u-spacing-top-small {
    margin-top: 15px;
    margin-top: .9375rem
}

.u-spacing-bottom-small.u-spacing-bottom-small {
    margin-bottom: 15px;
    margin-bottom: .9375rem
}

.u-spacing-top-base.u-spacing-top-base {
    margin-top: 20px;
    margin-top: 1.25rem
}

.u-spacing-bottom-base.u-spacing-bottom-base {
    margin-bottom: 20px;
    margin-bottom: 1.25rem
}

.u-spacing-top-medium.u-spacing-top-medium {
    margin-top: 30px;
    margin-top: 1.875rem
}

.u-spacing-bottom-medium.u-spacing-bottom-medium {
    margin-bottom: 30px;
    margin-bottom: 1.875rem
}

@media (min-width: 900px) {
    .u-spacing-top-zero\@medium.u-spacing-top-zero\@medium {
        margin-top:0
    }
}

@media print {
    .u-spacing-top-zero\@medium.u-spacing-top-zero\@medium {
        margin-top: 11.25rem
    }
}

@media (min-width: 900px) {
    .u-spacing-bottom-zero\@medium.u-spacing-bottom-zero\@medium {
        margin-bottom:0
    }
}

@media (min-width: 900px) {
    .u-spacing-top-small\@medium.u-spacing-top-small\@medium {
        margin-top:.9375rem
    }
}

@media (min-width: 900px) {
    .u-spacing-bottom-small\@medium.u-spacing-bottom-small\@medium {
        margin-bottom:.9375rem
    }
}

@media (min-width: 900px) {
    .u-spacing-top-base\@medium.u-spacing-top-base\@medium {
        margin-top:1.25rem
    }
}

@media (min-width: 900px) {
    .u-spacing-bottom-base\@medium.u-spacing-bottom-base\@medium {
        margin-bottom:1.25rem
    }
}

@media (min-width: 900px) {
    .u-spacing-top-medium\@medium.u-spacing-top-medium\@medium {
        margin-top:1.875rem
    }
}

@media (min-width: 900px) {
    .u-spacing-bottom-medium\@medium.u-spacing-bottom-medium\@medium {
        margin-bottom:1.875rem
    }
}

.u-heading-1 {
    font-family: Montserrat,sans-serif;
    font-size: 24px;
    font-size: 1.5rem;
    font-weight: 800;
    line-height: 1.25
}

@media (min-width: 900px) {
    .u-heading-1 {
        font-size:2.25rem;
        line-height: 1.36842
    }
}

.u-heading-2 {
    font-family: Montserrat,sans-serif;
    font-size: 16px;
    font-size: 1rem;
    font-weight: 800;
    line-height: 1.1875
}

@media (min-width: 900px) {
    .u-heading-2 {
        font-size:1.125rem;
        line-height: 1.22222
    }
}

.u-body-copy {
    font-family: Montserrat,sans-serif;
    font-size: 16px;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.1875
}

@media (min-width: 900px) {
    .u-body-copy {
        font-size:1.125rem;
        line-height: 1.33333
    }
}

.u-small-copy {
    font-family: Montserrat,sans-serif;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    line-height: 1.21429
}

@media (min-width: 900px) {
    .u-small-copy {
        font-size:1rem;
        line-height: 1.375
    }
}

.u-percentage {
    font-family: Montserrat,sans-serif;
    font-weight: 800;
    font-size: 36px;
    font-size: 2.25rem;
    line-height: 1.38095
}

@media (min-width: 900px) {
    .u-percentage {
        font-size:4rem;
        line-height: 1.34375
    }
}

.u-button-text {
    font-family: Montserrat,sans-serif;
    font-size: 12px;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .08333em;
    line-height: 1.16667;
    text-transform: uppercase
}

@media (min-width: 900px) {
    .u-button-text {
        font-size:.875rem;
        line-height: 1.21429
    }
}

.u-label {
    font-family: Montserrat,sans-serif;
    font-size: 12px;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .08333em;
    line-height: 1.16667;
    text-transform: uppercase
}

@media (min-width: 900px) {
    .u-label {
        font-size:.875rem;
        line-height: 1.21429
    }
}

.u-align-left.u-align-left {
    text-align: left
}

.u-align-center.u-align-center {
    text-align: center
}

.u-align-right.u-align-right {
    text-align: right
}

.u-uppercase.u-uppercase {
    text-transform: uppercase
}

.u-lowercase.u-lowercase {
    text-transform: lowercase
}

.u-no-case.u-no-case {
    text-transform: none
}

.u-ui-body {
    padding-top: 60px;
    transition: transform .5s cubic-bezier(.5,0,.5,1)
}

@media (min-width: 1400px) {
    .u-ui-body {
        padding-left:300px
    }
}

.ui-guide-menu-active .u-ui-body {
    transform: translateX(300px)
}

@media (min-width: 1400px) {
    .ui-guide-menu-active .u-ui-body {
        transform:none!important
    }
}

.u-ui-header {
    background: #fff;
    color: #fff;
    position: fixed;
    left: 0;
    top: 0;
    z-index: 3
}

.u-ui-header,.u-ui-header__banner {
    -ms-flex-align: center;
    align-items: center;
    min-height: 60px;
    display: -ms-flexbox;
    display: flex;
    width: 100%
}

.u-ui-header__banner {
    background-color: #000;
    background-color: rgba(0,0,0,.8);
    padding: 20px;
    transition: all .5s cubic-bezier(.5,0,.5,1)
}

@media (min-width: 1400px) {
    .u-ui-header__banner {
        padding-left:50px;
        width: calc(100% - 300px)
    }
}

.ui-guide-menu-active .u-ui-header__banner {
    transform: translateX(300px)
}

@media (min-width: 1400px) {
    .ui-guide-menu-active .u-ui-header__banner {
        transform:none!important
    }
}

.u-ui-header__banner h1 {
    border: none;
    color: #fff;
    font-size: 16px;
    font-size: 1rem;
    font-weight: 400;
    letter-spacing: .02em;
    line-height: 1.3;
    margin: 0
}

@media (min-width: 1400px) {
    .u-ui-header__banner h1 {
        font-size:1.125rem
    }
}

.u-ui-header .u-ui-header-logo {
    -ms-flex-align: center;
    align-items: center;
    background-color: #fff;
    border-bottom: 1px solid rgba(0,0,0,.15);
    display: -ms-flexbox;
    display: flex;
    left: 0;
    min-height: 60px;
    padding: 20px;
    position: fixed;
    top: 0;
    transform: translateX(-100%);
    width: 300px;
    z-index: 2
}

@media (min-width: 1400px) {
    .u-ui-header .u-ui-header-logo {
        position:relative;
        background: #fff;
        transform: none;
        width: 300px
    }
}

.ui-guide-menu-active .u-ui-header .u-ui-header-logo {
    transform: none
}

.u-ui-header .u-ui-header-logo svg {
    fill: #202020;
    height: 20px;
    width: 70px
}

.u-ui-menu-btn {
    display: block;
    height: 16px;
    position: relative;
    width: 25px;
    margin-right: 40px
}

@media (min-width: 1400px) {
    .u-ui-menu-btn {
        display:none
    }
}

.u-ui-menu-btn:focus {
    outline: none
}

.u-ui-menu-btn__icon {
    background-color: #fff;
    display: block;
    height: 2px;
    width: 100%
}

.u-ui-menu-btn__icon:after,.u-ui-menu-btn__icon:before {
    background-color: #fff;
    content: "";
    height: 2px;
    left: 0;
    position: absolute;
    width: 100%
}

.u-ui-menu-btn__icon:before {
    top: 0
}

.u-ui-menu-btn__icon:after {
    bottom: 0
}

.u-ui-sidebar {
    background: #fff;
    border-right: 1px solid rgba(0,0,0,.15);
    font-size: 13px;
    font-size: .8125rem;
    font-weight: 600;
    height: 100%;
    left: 0;
    padding-bottom: 100px;
    padding-top: 60px;
    position: fixed;
    top: 0;
    transform: translateX(-100%);
    transition: transform .5s cubic-bezier(.5,0,.5,1);
    width: 300px;
    z-index: 1
}

@media (min-width: 1400px) {
    .u-ui-sidebar {
        transform:none
    }
}

.ui-guide-menu-active .u-ui-sidebar {
    transform: none
}

.u-ui-sidebar li {
    padding: 0!important;
    margin: 0!important
}

.u-ui-sidebar li:before {
    display: none!important
}

.u-ui-sidebar li.is-indented a {
    color: #000;
    color: rgba(0,0,0,.7);
    padding-left: 40px;
    font-weight: 400;
    padding-top: 5px;
    padding-bottom: 5px
}

.u-ui-sidebar a {
    border: none;
    color: #000;
    color: rgba(0,0,0,.8);
    display: block;
    padding: 5px 20px;
    position: relative
}

.u-ui-sidebar a:focus {
    outline: none
}

.u-ui-sidebar a:after {
    background-color: #000;
    background-color: rgba(0,0,0,.25);
    content: "";
    height: 100%;
    left: 0;
    position: absolute;
    top: 0;
    transition: width .3s cubic-bezier(.5,0,.5,1);
    width: 0
}

.u-ui-sidebar a:hover:after {
    width: 5px
}

.u-ui-sidebar__inner {
    height: calc(100vh - 60px);
    padding: 10px 0 0;
    overflow: auto
}

.u-ui-sidebar__inner ul {
    min-height: calc(100vh - 170px)
}

.u-ui-sidebar__footer {
    background: #fff;
    border-top: 1px solid rgba(0,0,0,.15);
    color: #000;
    color: rgba(0,0,0,.5);
    cursor: pointer;
    font-size: 10px;
    font-size: .625rem;
    font-weight: 400;
    letter-spacing: .025em;
    line-height: 1.3;
    margin-top: 30px;
    padding: 20px;
    width: 100%;
    z-index: 3
}

.u-ui-sidebar__footer p {
    margin: 0
}

.u-ui-heading-large,.u-ui-heading-medium,.u-ui-heading-small {
    border-bottom: 1px solid tint(#000,75%);
    color: tint(#000,50%);
    font-weight: 400;
    line-height: 1;
    margin-bottom: 50px;
    margin-top: 0
}

.u-ui-heading-large {
    border: none;
    color: #fff;
    font-size: 42px;
    font-size: 2.625rem;
    font-weight: 600;
    line-height: 1.3;
    margin-bottom: 0
}

.u-ui-heading-medium {
    font-size: 30px;
    font-size: 1.875rem;
    padding-bottom: 10px
}

.u-ui-heading-small {
    font-size: 21px;
    font-size: 1.3125rem;
    line-height: 1;
    padding-bottom: 10px;
    margin: 30px 0
}

.u-ui-color {
    border-radius: 3px;
    box-shadow: 0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24);
    display: inline-block;
    font-size: 14px;
    font-size: .875rem;
    line-height: 1.3;
    margin: 0 5px 20px;
    overflow: hidden;
    padding-top: 120px;
    width: 20%
}

.u-ui-color:first-of-type {
    margin-left: 0
}

.u-ui-color>div {
    background: #fff;
    padding: 10px
}

.u-ui-color h4 {
    font-size: 14px;
    font-size: .875rem;
    font-weight: 400;
    margin: 0
}

.u-ui-section {
    padding: 50px 0
}

.u-ui-section-medium {
    background: #eee
}

.u-ui-section-medium [class^=ui-heading] {
    color: tint(#000,35%);
    border-color: tint(#000,35%)
}

.u-ui-section-dark {
    background: #666
}

.u-ui-section-dark [class^=ui-heading] {
    color: #fff;
    border-color: #fff
}

.u-ui-bg-wrap {
    display: inline-block;
    padding: 15px
}

.u-ui-code-wrap,.u-ui-heading-large code,.u-ui-heading-medium code,.u-ui-heading-small code {
    background-color: #666;
    color: #fff;
    display: inline-block;
    font-family: monospace;
    font-size: 14px;
    font-size: .875rem;
    font-style: normal;
    font-weight: 400;
    line-height: 1;
    margin-left: 20px;
    padding: 10px 15px;
    text-transform: none;
    vertical-align: middle
}

.u-ui-note {
    background-color: #754acc;
    color: #fff;
    display: block;
    margin: 30px 0;
    padding: 25px
}

.u-ui-note:before {
    content: "DEVELOPER NOTE*";
    display: block;
    font-size: 14px;
    font-size: .875rem;
    font-weight: 700;
    margin-bottom: 10px;
    text-decoration: underline
}

.u-ui-note a {
    color: #fff;
    text-decoration: underline
}

.u-ui-heading-large .u-ui-note code,.u-ui-heading-medium .u-ui-note code,.u-ui-heading-small .u-ui-note code,.u-ui-note .u-ui-code-wrap,.u-ui-note .u-ui-heading-large code,.u-ui-note .u-ui-heading-medium code,.u-ui-note .u-ui-heading-small code {
    background-color: #fff;
    color: #754acc;
    margin-left: 10px;
    margin-right: 10px
}

.u-ui-grid-col {
    background-color: #000;
    background-color: rgba(0,0,0,.15);
    padding: 10px;
    width: 100%
}

.s-cms-content {
    zoom:1}

.s-cms-content:after,.s-cms-content:before {
    content: "";
    display: table
}

.s-cms-content:after {
    clear: both
}

.s-cms-content a {
    border-bottom: 1px solid;
    color: #5470e0;
    text-decoration: none
}

.s-cms-content a:hover {
    color: #37383c;
    border-bottom-color: transparent
}

.s-cms-content a:active,.s-cms-content a:visited {
    color: #37383c;
    border-bottom: 1px solid
}

.s-cms-content figure {
    margin-bottom: 30px;
    margin-bottom: 1.875rem
}

.s-cms-content figcaption {
    background: #ccc;
    padding: 15px 20px;
    padding: .9375rem 1.25rem
}

.s-cms-content a {
    word-break: break-word
}

.s-cms-content p {
    margin-bottom: 30px;
    margin-bottom: 1.875rem;
    margin-top: 0
}

.s-cms-content p:last-of-type:last-child {
    margin-bottom: 0
}

.s-cms-content ul {
    list-style-type: none;
    margin-bottom: 30px;
    margin-bottom: 1.875rem;
    padding: 0;
    position: relative;
    overflow: hidden
}

.s-cms-content ul li {
    margin-bottom: 10px;
    margin-bottom: .625rem;
    padding-left: 30px;
    padding-left: 1.875rem;
    position: relative
}

.s-cms-content ul li:before {
    color: #000;
    display: inline-block;
    left: 0;
    line-height: 1;
    position: absolute;
    top: 0;
    vertical-align: middle;
    content: ".";
    font-size: 35px;
    font-size: 2.1875rem;
    line-height: 10px;
    top: -.07em
}

.s-cms-content ol {
    list-style-type: none;
    margin-bottom: 30px;
    margin-bottom: 1.875rem;
    padding: 0;
    position: relative;
    overflow: hidden;
    counter-reset: a
}

.s-cms-content ol li {
    margin-bottom: 10px;
    margin-bottom: .625rem;
    padding-left: 30px;
    padding-left: 1.875rem;
    position: relative
}

.s-cms-content ol li:before {
    color: #000;
    display: inline-block;
    line-height: 1;
    position: absolute;
    top: 0;
    vertical-align: middle;
    content: counter(a,decimal) ".";
    counter-increment: a;
    font-weight: 600;
    left: 0;
    top: .275em
}

.s-cms-content ol ol li:before {
    content: counter(a)
}

.s-healthcheck [class] {
    outline: 5px solid #d3d3d3
}

.s-healthcheck [class*=__] {
    outline: 5px solid grey
}

.s-healthcheck [class*="--"] {
    outline: 5px solid #a9a9a9
}

.s-healthcheck [class*=" o-"],.s-healthcheck [class^=o-] {
    outline: 5px solid orange
}

.s-healthcheck [class*=" c-"],.s-healthcheck [class^=c-] {
    outline: 5px solid cyan
}

.s-healthcheck [class*="@"] {
    outline: 5px solid #bc8f8f
}

.s-healthcheck [class^=_] {
    outline: 5px solid red
}

/*# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi9zYXNzL3N0eWxlcy5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7QUFBOEUsVUFBVSxNQUFNLENBQUMsaUNBQWlDLFdBQVcsYUFBYSxDQUFDLGdCQUFnQixVQUFVLENBQUMsV0FBVyxjQUFjLFdBQVcsd0JBQXdCLFdBQVcsV0FBVyxDQUFDLDZOQUE2TixxQkFBcUIsYUFBYSxXQUFXLENBQUM7O0FBRWxoQiw0REFBNEQsS0FBSyx1QkFBdUIsMEJBQTBCLDZCQUE2QixDQUFDLEtBQUssUUFBUSxDQUFDLDJGQUEyRixhQUFhLENBQUMsNEJBQTRCLHFCQUFxQix1QkFBdUIsQ0FBQyxzQkFBc0IsYUFBYSxRQUFRLENBQUMsa0JBQWtCLFlBQVksQ0FBQyxFQUFFLDRCQUE0QixDQUFDLGlCQUFpQixTQUFTLENBQUMsWUFBWSx3QkFBd0IsQ0FBQyxTQUFTLGVBQWUsQ0FBQyxJQUFJLGlCQUFpQixDQUFDLEdBQUcsY0FBYyxjQUFjLENBQUMsS0FBSyxnQkFBZ0IsVUFBVSxDQUFDLE1BQU0sYUFBYSxDQUFDLFFBQVEsY0FBYyxjQUFjLGtCQUFrQix1QkFBdUIsQ0FBQyxJQUFJLFNBQVMsQ0FBQyxJQUFJLGFBQWEsQ0FBQyxJQUFJLFFBQVEsQ0FBQyxlQUFlLGVBQWUsQ0FBQyxPQUFPLGVBQWUsQ0FBQyxHQUFHLHVCQUF1QixRQUFRLENBQUMsSUFBSSxhQUFhLENBQUMsa0JBQWtCLGdDQUFnQyxhQUFhLENBQUMsc0NBQXNDLGNBQWMsYUFBYSxRQUFRLENBQUMsT0FBTyxnQkFBZ0IsQ0FBQyxjQUFjLG1CQUFtQixDQUFDLG9FQUFvRSwwQkFBMEIsY0FBYyxDQUFDLHNDQUFzQyxjQUFjLENBQUMsaURBQWlELFNBQVMsU0FBUyxDQUFDLE1BQU0sa0JBQWtCLENBQUMsdUNBQXVDLHNCQUFzQixTQUFTLENBQUMsNEZBQTRGLFdBQVcsQ0FBQyxtQkFBbUIsNkJBQTZCLHNCQUFzQixDQUFDLCtGQUErRix1QkFBdUIsQ0FBQyxTQUFTLHdCQUF3Qixh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c0JBQXNCLGlCQUFpQixDQUFDLDRCQUE0QixXQUFXLHFCQUFxQixjQUFjLGtCQUFrQixNQUFNLHNCQUFzQiwrQkFBK0Isb0JBQW9CLGdCQUFnQixPQUFPLFVBQVUsQ0FBQywrQkFBK0Isa0JBQWtCLENBQUMsdUJBQXVCLHlCQUF5QixDQUFDLDJCQUEyQixzQkFBc0IsQ0FBQyw2QkFBNkIseUJBQXlCLENBQUMseURBQXlELHdCQUF3QixDQUFDLHlEQUF5RCxzQkFBc0IsQ0FBQyw0QkFBNEIseUJBQXlCLENBQUMsMEJBQTBCLHFCQUFxQixDIiwiZmlsZSI6Ii4uLy4uL2Nzcy9zdHlsZXMuY3NzIiwic291cmNlc0NvbnRlbnQiOlsiQGltcG9ydCB1cmwoXCJodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2Nzcz9mYW1pbHk9TW9udHNlcnJhdDo0MDAsNzAwLDgwMFwiKTsuY2xlYXJmaXh7em9vbToxfS5jbGVhcmZpeDphZnRlciwuY2xlYXJmaXg6YmVmb3Jle2NvbnRlbnQ6XCJcIjtkaXNwbGF5OnRhYmxlfS5jbGVhcmZpeDphZnRlcntjbGVhcjpib3RofS5zLWV4YW1wbGV7ZGlzcGxheTpibG9jaztjb250ZW50OlwiXCI7YmFja2dyb3VuZC1wb3NpdGlvbjowIDA7d2lkdGg6MzJweDtoZWlnaHQ6MzJweH0uc3ZnLWFycm93LWxlZnQsLnN2Zy1hcnJvdy1yaWdodCwuc3ZnLWNoZXZyb24tZG93biwuc3ZnLWNoZXZyb24tbGVmdCwuc3ZnLWNoZXZyb24tcmlnaHQsLnN2Zy1jaGV2cm9uLXVwLC5zdmctZ29vZ2xlLXBsdXMsLnN2Zy1pbnN0YWdyYW0sLnN2Zy1waW50ZXJlc3QsLnN2Zy1zZWFyY2gsLnN2Zy1zaGFyZSwuc3ZnLXRpY2ssLnN2Zy10d2l0dGVyLC5zdmctdmltZW8sLnN2Zy15b3V0dWJle2Rpc3BsYXk6aW5saW5lLWJsb2NrO2hlaWdodDoxMDBweDt3aWR0aDoxMDBweH1cblxuLyohIG5vcm1hbGl6ZS5jc3MgdjMuMC4yIHwgTUlUIExpY2Vuc2UgfCBnaXQuaW8vbm9ybWFsaXplICovaHRtbHtmb250LWZhbWlseTpzYW5zLXNlcmlmOy1tcy10ZXh0LXNpemUtYWRqdXN0OjEwMCU7LXdlYmtpdC10ZXh0LXNpemUtYWRqdXN0OjEwMCV9Ym9keXttYXJnaW46MH1hcnRpY2xlLGFzaWRlLGRldGFpbHMsZmlnY2FwdGlvbixmaWd1cmUsZm9vdGVyLGhlYWRlcixoZ3JvdXAsbWFpbixtZW51LG5hdixzZWN0aW9uLHN1bW1hcnl7ZGlzcGxheTpibG9ja31hdWRpbyxjYW52YXMscHJvZ3Jlc3MsdmlkZW97ZGlzcGxheTppbmxpbmUtYmxvY2s7dmVydGljYWwtYWxpZ246YmFzZWxpbmV9YXVkaW86bm90KFtjb250cm9sc10pe2Rpc3BsYXk6bm9uZTtoZWlnaHQ6MH1baGlkZGVuXSx0ZW1wbGF0ZXtkaXNwbGF5Om5vbmV9YXtiYWNrZ3JvdW5kLWNvbG9yOnRyYW5zcGFyZW50fWE6YWN0aXZlLGE6aG92ZXJ7b3V0bGluZTowfWFiYnJbdGl0bGVde2JvcmRlci1ib3R0b206MXB4IGRvdHRlZH1iLHN0cm9uZ3tmb250LXdlaWdodDo3MDB9ZGZue2ZvbnQtc3R5bGU6aXRhbGljfWgxe2ZvbnQtc2l6ZToyZW07bWFyZ2luOi42N2VtIDB9bWFya3tiYWNrZ3JvdW5kOiNmZjA7Y29sb3I6IzAwMH1zbWFsbHtmb250LXNpemU6ODAlfXN1YixzdXB7Zm9udC1zaXplOjc1JTtsaW5lLWhlaWdodDowO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOmJhc2VsaW5lfXN1cHt0b3A6LS41ZW19c3Vie2JvdHRvbTotLjI1ZW19aW1ne2JvcmRlcjowfXN2Zzpub3QoOnJvb3Qpe292ZXJmbG93OmhpZGRlbn1maWd1cmV7bWFyZ2luOjFlbSA0MHB4fWhye2JveC1zaXppbmc6Y29udGVudC1ib3g7aGVpZ2h0OjB9cHJle292ZXJmbG93OmF1dG99Y29kZSxrYmQscHJlLHNhbXB7Zm9udC1mYW1pbHk6bW9ub3NwYWNlLG1vbm9zcGFjZTtmb250LXNpemU6MWVtfWJ1dHRvbixpbnB1dCxvcHRncm91cCxzZWxlY3QsdGV4dGFyZWF7Y29sb3I6aW5oZXJpdDtmb250OmluaGVyaXQ7bWFyZ2luOjB9YnV0dG9ue292ZXJmbG93OnZpc2libGV9YnV0dG9uLHNlbGVjdHt0ZXh0LXRyYW5zZm9ybTpub25lfWJ1dHRvbixodG1sIGlucHV0W3R5cGU9YnV0dG9uXSxpbnB1dFt0eXBlPXJlc2V0XSxpbnB1dFt0eXBlPXN1Ym1pdF17LXdlYmtpdC1hcHBlYXJhbmNlOmJ1dHRvbjtjdXJzb3I6cG9pbnRlcn1idXR0b25bZGlzYWJsZWRdLGh0bWwgaW5wdXRbZGlzYWJsZWRde2N1cnNvcjpkZWZhdWx0fWJ1dHRvbjo6LW1vei1mb2N1cy1pbm5lcixpbnB1dDo6LW1vei1mb2N1cy1pbm5lcntib3JkZXI6MDtwYWRkaW5nOjB9aW5wdXR7bGluZS1oZWlnaHQ6bm9ybWFsfWlucHV0W3R5cGU9Y2hlY2tib3hdLGlucHV0W3R5cGU9cmFkaW9de2JveC1zaXppbmc6Ym9yZGVyLWJveDtwYWRkaW5nOjB9aW5wdXRbdHlwZT1udW1iZXJdOjotd2Via2l0LWlubmVyLXNwaW4tYnV0dG9uLGlucHV0W3R5cGU9bnVtYmVyXTo6LXdlYmtpdC1vdXRlci1zcGluLWJ1dHRvbntoZWlnaHQ6YXV0b31pbnB1dFt0eXBlPXNlYXJjaF17LXdlYmtpdC1hcHBlYXJhbmNlOnRleHRmaWVsZDtib3gtc2l6aW5nOmNvbnRlbnQtYm94fWlucHV0W3R5cGU9c2VhcmNoXTo6LXdlYmtpdC1zZWFyY2gtY2FuY2VsLWJ1dHRvbixpbnB1dFt0eXBlPXNlYXJjaF06Oi13ZWJraXQtc2VhcmNoLWRlY29yYXRpb257LXdlYmtpdC1hcHBlYXJhbmNlOm5vbmV9ZmllbGRzZXR7Ym9yZGVyOjFweCBzb2xpZCBzaWx2ZXI7bWFyZ2luOjAgMnB4O3BhZGRpbmc6LjM1ZW0gLjYyNWVtIC43NWVtfWxlZ2VuZHtib3JkZXI6MDtwYWRkaW5nOjB9dGV4dGFyZWF7b3ZlcmZsb3c6YXV0b31vcHRncm91cHtmb250LXdlaWdodDo3MDB9dGFibGV7Ym9yZGVyLWNvbGxhcHNlOmNvbGxhcHNlO2JvcmRlci1zcGFjaW5nOjB9dGQsdGh7cGFkZGluZzowfSosOmFmdGVyLDpiZWZvcmV7Ym94LXNpemluZzpib3JkZXItYm94fTpmb2N1c3tvdXRsaW5lOjFweCBkb3R0ZWQgI2YxZjFmMX06OnNlbGVjdGlvbntjb2xvcjojZmZmO2JhY2tncm91bmQ6IzM3MzgzY306Oi1tb3otc2VsZWN0aW9ue2NvbG9yOiNmZmY7YmFja2dyb3VuZDojMzczODNjfWJvZHksaHRtbHstbW96LW9zeC1mb250LXNtb290aGluZzphdXRvOy1tb3otb3N4LWZvbnQtc21vb3RoaW5nOmdyYXlzY2FsZTstd2Via2l0LWJhY2tmYWNlLXZpc2liaWxpdHk6aGlkZGVuOy13ZWJraXQtZm9udC1zbW9vdGhpbmc6YW50aWFsaWFzZWQhaW1wb3J0YW50O2NvbG9yOiMzNzM4M2M7Zm9udC1mYW1pbHk6TW9udHNlcnJhdCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNnB4O2ZvbnQtd2VpZ2h0OjQwMDtsaW5lLWhlaWdodDoxLjY7bWluLXdpZHRoOjMyMHB4O3Bvc2l0aW9uOnJlbGF0aXZlO3RleHQtcmVuZGVyaW5nOm9wdGltaXplTGVnaWJpbGl0eSFpbXBvcnRhbnQ7d2lkdGg6MTAwJTt6LWluZGV4OjB9Ym9keXtmb250LXNpemU6MTZweDtmb250LXNpemU6MXJlbX1hW2hyZWYqPVwibWFpbHRvOlwiXXt3b3JkLXdyYXA6YnJlYWstd29yZH1idXR0b257YmFja2dyb3VuZC1jb2xvcjp0cmFuc3BhcmVudDtvdXRsaW5lOm5vbmV9aDEsaDIsaDMsaDQsaDUsaDZ7bWFyZ2luLXRvcDowfW9sLHVse2xpc3Qtc3R5bGU6bm9uZTttYXJnaW46MDtwYWRkaW5nOjB9YXt0ZXh0LWRlY29yYXRpb246bm9uZTtjb2xvcjojNTQ3MGUwfWE6aG92ZXJ7dGV4dC1kZWNvcmF0aW9uOnVuZGVybGluZX1we21hcmdpbi10b3A6MDttYXJnaW4tYm90dG9tOjIwcHg7bWFyZ2luLWJvdHRvbToxLjI1cmVtfXAgYixwIHN0cm9uZ3tmb250LXdlaWdodDo2MDB9cCBlbSxwIGl7Zm9udC1zdHlsZTppdGFsaWN9W2NsYXNzXj1jLWJ0bl0sYSxidXR0b24saW5wdXRbdHlwZT10ZXh0XSx0ZXh0YXJlYXtmb250LWZhbWlseTpNb250c2VycmF0LHNhbnMtc2VyaWY7Zm9udC1zaXplOjE0cHg7Zm9udC1zaXplOi44NzVyZW07Zm9udC13ZWlnaHQ6NDAwO2xpbmUtaGVpZ2h0OjEuMjE0Mjk7dHJhbnNpdGlvbi1kdXJhdGlvbjouNXM7dHJhbnNpdGlvbi1wcm9wZXJ0eTpiYWNrZ3JvdW5kLWNvbG9yLGNvbG9yLG9wYWNpdHksYm9yZGVyLGJvcmRlci1jb2xvcixiYWNrZ3JvdW5kLXBvc2l0aW9uLG91dGxpbmUsYm94LXNoYWRvdyxib3JkZXItYm90dG9tLHRleHQtZGVjb3JhdGlvbixsZWZ0LHRvcCx0cmFuc2Zvcm07dHJhbnNpdGlvbi10aW1pbmctZnVuY3Rpb246Y3ViaWMtYmV6aWVyKC41LDAsLjUsMSk7dHJhbnNmb3JtLW9yaWdpbjpjZW50ZXIgY2VudGVyfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXtbY2xhc3NePWMtYnRuXSxhLGJ1dHRvbixpbnB1dFt0eXBlPXRleHRdLHRleHRhcmVhe2ZvbnQtc2l6ZToxcmVtO2xpbmUtaGVpZ2h0OjEuMzc1fX1mb3JtIGZpZWxkc2V0e2JvcmRlcjpub25lO3BhZGRpbmc6MH1mb3JtIG9se3pvb206MX1mb3JtIG9sOmFmdGVyLGZvcm0gb2w6YmVmb3Jle2NvbnRlbnQ6XCJcIjtkaXNwbGF5OnRhYmxlfWZvcm0gb2w6YWZ0ZXJ7Y2xlYXI6Ym90aH1mb3JtIG9sIGxpe3pvb206MTttYXJnaW4tYm90dG9tOjIwcHg7bWFyZ2luLWJvdHRvbToxLjI1cmVtfWZvcm0gb2wgbGk6YWZ0ZXIsZm9ybSBvbCBsaTpiZWZvcmV7Y29udGVudDpcIlwiO2Rpc3BsYXk6dGFibGV9Zm9ybSBvbCBsaTphZnRlcntjbGVhcjpib3RofWJ1dHRvbntiYWNrZ3JvdW5kOm5vbmU7Ym9yZGVyOm5vbmU7cGFkZGluZzowfWltZ3tkaXNwbGF5OmJsb2NrO2hlaWdodDphdXRvO21heC13aWR0aDoxMDAlfWZpZ3VyZXttYXJnaW46MH1AbWVkaWEgcHJpbnR7KntiYWNrZ3JvdW5kOnRyYW5zcGFyZW50IWltcG9ydGFudDtjb2xvcjojMDAwIWltcG9ydGFudDtib3gtc2hhZG93Om5vbmUhaW1wb3J0YW50O3RleHQtc2hhZG93Om5vbmUhaW1wb3J0YW50fWEsYTp2aXNpdGVke3RleHQtZGVjb3JhdGlvbjp1bmRlcmxpbmV9YVtocmVmXTphZnRlcntjb250ZW50OlwiIChcIiBhdHRyKGhyZWYpIFwiKVwifWFiYnJbdGl0bGVdOmFmdGVye2NvbnRlbnQ6XCIgKFwiIGF0dHIodGl0bGUpIFwiKVwifS5pciBhOmFmdGVyLGFbaHJlZl49XCIjXCJdOmFmdGVyLGFbaHJlZl49XCJqYXZhc2NyaXB0OlwiXTphZnRlcntjb250ZW50OlwiXCJ9YmxvY2txdW90ZSxwcmV7Ym9yZGVyOjFweCBzb2xpZCAjOTk5O3BhZ2UtYnJlYWstaW5zaWRlOmF2b2lkfXRoZWFke2Rpc3BsYXk6dGFibGUtaGVhZGVyLWdyb3VwfWltZyx0cntwYWdlLWJyZWFrLWluc2lkZTphdm9pZH1pbWd7bWF4LXdpZHRoOjEwMCUhaW1wb3J0YW50fUBwYWdle21hcmdpbjouNWNtfWgyLGgzLHB7b3JwaGFuczozO3dpZG93czozfWgyLGgze3BhZ2UtYnJlYWstYWZ0ZXI6YXZvaWR9fS5vLWNvbHtkaXNwbGF5OmlubGluZS1ibG9jazt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2x7LW1zLWZsZXg6MCAwIDguMzMzMzMlO2ZsZXg6MCAwIDguMzMzMzMlO3dpZHRoOjguMzMzMzMlfX0uby1jb2xfX2lubmVye3BhZGRpbmc6MCAwIDIwcHh9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLWNvbF9faW5uZXJ7cGFkZGluZzowIDEwcHggMjBweH19Lm8tY29sLS0xe3dpZHRoOjEwMCV9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLWNvbC0tMXstbXMtZmxleDowIDAgOC4zMzMzMyU7ZmxleDowIDAgOC4zMzMzMyU7d2lkdGg6OC4zMzMzMyV9fS5vLWNvbC0tMnt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLTJ7LW1zLWZsZXg6MCAwIDE2LjY2NjY3JTtmbGV4OjAgMCAxNi42NjY2NyU7d2lkdGg6MTYuNjY2NjclfX0uby1jb2wtLTN7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7Lm8tY29sLS0zey1tcy1mbGV4OjAgMCAyNSU7ZmxleDowIDAgMjUlO3dpZHRoOjI1JX19Lm8tY29sLS00e3dpZHRoOjEwMCV9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLWNvbC0tNHstbXMtZmxleDowIDAgMzMuMzMzMzMlO2ZsZXg6MCAwIDMzLjMzMzMzJTt3aWR0aDozMy4zMzMzMyV9fS5vLWNvbC0tNXt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLTV7LW1zLWZsZXg6MCAwIDQxLjY2NjY3JTtmbGV4OjAgMCA0MS42NjY2NyU7d2lkdGg6NDEuNjY2NjclfX0uby1jb2wtLTZ7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7Lm8tY29sLS02ey1tcy1mbGV4OjAgMCA1MCU7ZmxleDowIDAgNTAlO3dpZHRoOjUwJX19Lm8tY29sLS03e3dpZHRoOjEwMCV9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLWNvbC0tN3stbXMtZmxleDowIDAgNTguMzMzMzMlO2ZsZXg6MCAwIDU4LjMzMzMzJTt3aWR0aDo1OC4zMzMzMyV9fS5vLWNvbC0tOHt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLTh7LW1zLWZsZXg6MCAwIDY2LjY2NjY3JTtmbGV4OjAgMCA2Ni42NjY2NyU7d2lkdGg6NjYuNjY2NjclfX0uby1jb2wtLTl7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7Lm8tY29sLS05ey1tcy1mbGV4OjAgMCA3NSU7ZmxleDowIDAgNzUlO3dpZHRoOjc1JX19Lm8tY29sLS0xMHt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLTEwey1tcy1mbGV4OjAgMCA4My4zMzMzMyU7ZmxleDowIDAgODMuMzMzMzMlO3dpZHRoOjgzLjMzMzMzJX19Lm8tY29sLS0xMXt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLTExey1tcy1mbGV4OjAgMCA5MS42NjY2NyU7ZmxleDowIDAgOTEuNjY2NjclO3dpZHRoOjkxLjY2NjY3JX19Lm8tY29sLS0xMnt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLTEyey1tcy1mbGV4OjAgMCAxMDAlO2ZsZXg6MCAwIDEwMCU7d2lkdGg6MTAwJX19Lm8tY29sLS0xXFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tMVxcQGxhcmdley1tcy1mbGV4OjAgMCA4LjMzMzMzJTtmbGV4OjAgMCA4LjMzMzMzJTt3aWR0aDo4LjMzMzMzJX19Lm8tY29sLS0yXFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tMlxcQGxhcmdley1tcy1mbGV4OjAgMCAxNi42NjY2NyU7ZmxleDowIDAgMTYuNjY2NjclO3dpZHRoOjE2LjY2NjY3JX19Lm8tY29sLS0zXFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tM1xcQGxhcmdley1tcy1mbGV4OjAgMCAyNSU7ZmxleDowIDAgMjUlO3dpZHRoOjI1JX19Lm8tY29sLS00XFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tNFxcQGxhcmdley1tcy1mbGV4OjAgMCAzMy4zMzMzMyU7ZmxleDowIDAgMzMuMzMzMzMlO3dpZHRoOjMzLjMzMzMzJX19Lm8tY29sLS01XFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tNVxcQGxhcmdley1tcy1mbGV4OjAgMCA0MS42NjY2NyU7ZmxleDowIDAgNDEuNjY2NjclO3dpZHRoOjQxLjY2NjY3JX19Lm8tY29sLS02XFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tNlxcQGxhcmdley1tcy1mbGV4OjAgMCA1MCU7ZmxleDowIDAgNTAlO3dpZHRoOjUwJX19Lm8tY29sLS03XFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tN1xcQGxhcmdley1tcy1mbGV4OjAgMCA1OC4zMzMzMyU7ZmxleDowIDAgNTguMzMzMzMlO3dpZHRoOjU4LjMzMzMzJX19Lm8tY29sLS04XFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tOFxcQGxhcmdley1tcy1mbGV4OjAgMCA2Ni42NjY2NyU7ZmxleDowIDAgNjYuNjY2NjclO3dpZHRoOjY2LjY2NjY3JX19Lm8tY29sLS05XFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tOVxcQGxhcmdley1tcy1mbGV4OjAgMCA3NSU7ZmxleDowIDAgNzUlO3dpZHRoOjc1JX19Lm8tY29sLS0xMFxcQGxhcmdle3dpZHRoOjEwMCV9QG1lZGlhIChtaW4td2lkdGg6MTIwMHB4KXsuby1jb2wtLTEwXFxAbGFyZ2V7LW1zLWZsZXg6MCAwIDgzLjMzMzMzJTtmbGV4OjAgMCA4My4zMzMzMyU7d2lkdGg6ODMuMzMzMzMlfX0uby1jb2wtLTExXFxAbGFyZ2V7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tMTFcXEBsYXJnZXstbXMtZmxleDowIDAgOTEuNjY2NjclO2ZsZXg6MCAwIDkxLjY2NjY3JTt3aWR0aDo5MS42NjY2NyV9fS5vLWNvbC0tMTJcXEBsYXJnZXt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjEyMDBweCl7Lm8tY29sLS0xMlxcQGxhcmdley1tcy1mbGV4OjAgMCAxMDAlO2ZsZXg6MCAwIDEwMCU7d2lkdGg6MTAwJX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLWNvbC0tb2Zmc2V0LTF7bWFyZ2luLWxlZnQ6OC4zMzMzMyV9fUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLW9mZnNldC0ye21hcmdpbi1sZWZ0OjE2LjY2NjY3JX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLWNvbC0tb2Zmc2V0LTN7bWFyZ2luLWxlZnQ6MjUlfX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7Lm8tY29sLS1vZmZzZXQtNHttYXJnaW4tbGVmdDozMy4zMzMzMyV9fUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLW9mZnNldC01e21hcmdpbi1sZWZ0OjQxLjY2NjY3JX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLWNvbC0tb2Zmc2V0LTZ7bWFyZ2luLWxlZnQ6NTAlfX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7Lm8tY29sLS1vZmZzZXQtN3ttYXJnaW4tbGVmdDo1OC4zMzMzMyV9fUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb2wtLW9mZnNldC04e21hcmdpbi1sZWZ0OjY2LjY2NjY3JX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLWNvbC0tb2Zmc2V0LTl7bWFyZ2luLWxlZnQ6NzUlfX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7Lm8tY29sLS1vZmZzZXQtMTB7bWFyZ2luLWxlZnQ6ODMuMzMzMzMlfX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7Lm8tY29sLS1vZmZzZXQtMTF7bWFyZ2luLWxlZnQ6OTEuNjY2NjclfX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7Lm8tY29sLS1vZmZzZXQtMTJ7bWFyZ2luLWxlZnQ6MTAwJX19QG1lZGlhIChtaW4td2lkdGg6MTIwMHB4KXsuby1jb2wtLW9mZnNldC0xXFxAbGFyZ2V7bWFyZ2luLWxlZnQ6OC4zMzMzMyV9fUBtZWRpYSAobWluLXdpZHRoOjEyMDBweCl7Lm8tY29sLS1vZmZzZXQtMlxcQGxhcmdle21hcmdpbi1sZWZ0OjE2LjY2NjY3JX19QG1lZGlhIChtaW4td2lkdGg6MTIwMHB4KXsuby1jb2wtLW9mZnNldC0zXFxAbGFyZ2V7bWFyZ2luLWxlZnQ6MjUlfX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tb2Zmc2V0LTRcXEBsYXJnZXttYXJnaW4tbGVmdDozMy4zMzMzMyV9fUBtZWRpYSAobWluLXdpZHRoOjEyMDBweCl7Lm8tY29sLS1vZmZzZXQtNVxcQGxhcmdle21hcmdpbi1sZWZ0OjQxLjY2NjY3JX19QG1lZGlhIChtaW4td2lkdGg6MTIwMHB4KXsuby1jb2wtLW9mZnNldC02XFxAbGFyZ2V7bWFyZ2luLWxlZnQ6NTAlfX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tb2Zmc2V0LTdcXEBsYXJnZXttYXJnaW4tbGVmdDo1OC4zMzMzMyV9fUBtZWRpYSAobWluLXdpZHRoOjEyMDBweCl7Lm8tY29sLS1vZmZzZXQtOFxcQGxhcmdle21hcmdpbi1sZWZ0OjY2LjY2NjY3JX19QG1lZGlhIChtaW4td2lkdGg6MTIwMHB4KXsuby1jb2wtLW9mZnNldC05XFxAbGFyZ2V7bWFyZ2luLWxlZnQ6NzUlfX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tb2Zmc2V0LTEwXFxAbGFyZ2V7bWFyZ2luLWxlZnQ6ODMuMzMzMzMlfX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tb2Zmc2V0LTExXFxAbGFyZ2V7bWFyZ2luLWxlZnQ6OTEuNjY2NjclfX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5vLWNvbC0tb2Zmc2V0LTEyXFxAbGFyZ2V7bWFyZ2luLWxlZnQ6MTAwJX19Lm8tY29sLS1uby1ib3R0b20tcGFkZGluZyAuby1jb2xfX2lubmVye3BhZGRpbmctYm90dG9tOjB9Lm8tY29udGFpbmVye2Rpc3BsYXk6YmxvY2s7bWF4LXdpZHRoOjE0NjBweDtwYWRkaW5nOjAgMjBweDtwYWRkaW5nOjAgMS4yNXJlbTttYXJnaW46MCBhdXRvfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1jb250YWluZXJ7bWF4LXdpZHRoOjE0NjBweH19Lm8tZ3JpZHstbXMtZmxleC1saW5lLXBhY2s6c3RhcnQ7YWxpZ24tY29udGVudDpzdGFydDstbXMtZmxleC1hbGlnbjpzdHJldGNoO2FsaWduLWl0ZW1zOnN0cmV0Y2g7ZGlzcGxheTotbXMtZmxleGJveDtkaXNwbGF5OmZsZXg7LW1zLWZsZXgtd3JhcDp3cmFwO2ZsZXgtd3JhcDp3cmFwOy1tcy1mbGV4LXBhY2s6c3RhcnQ7anVzdGlmeS1jb250ZW50OnN0YXJ0fUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuby1ncmlke21hcmdpbjowIC0xMHB4fX0uby1ncmlkLS1jZW50ZXJ7LW1zLWZsZXgtcGFjazpjZW50ZXI7anVzdGlmeS1jb250ZW50OmNlbnRlcn0uby1zZWN0aW9ue2Rpc3BsYXk6YmxvY2s7cGFkZGluZzo0MHB4IDA7cGFkZGluZzoyLjVyZW0gMH0uby1zZWN0aW9uLS1zbWFsbC1wYWRkaW5nXFxAc21hbGx7cGFkZGluZzoyMHB4IDA7cGFkZGluZzoxLjI1cmVtIDB9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5vLXNlY3Rpb24tLXNtYWxsLXBhZGRpbmdcXEBzbWFsbHtwYWRkaW5nOjIuNXJlbSAwfX0uYy1hcnJvd3toZWlnaHQ6MXB4O2hlaWdodDouMDYyNXJlbTtiYWNrZ3JvdW5kOiM1NDcwZTA7ZGlzcGxheTppbmxpbmUtYmxvY2s7d2lkdGg6MTBweDt3aWR0aDouNjI1cmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOm1pZGRsZX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtYXJyb3d7d2lkdGg6Ljc1cmVtfX0uYy1hcnJvdzpiZWZvcmV7aGVpZ2h0OjFweDtoZWlnaHQ6LjA2MjVyZW07YmFja2dyb3VuZDojNTQ3MGUwO2Rpc3BsYXk6aW5saW5lLWJsb2NrO3dpZHRoOjEwcHg7d2lkdGg6LjYyNXJlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7Y29udGVudDpcIlwiO3Bvc2l0aW9uOmFic29sdXRlO2xlZnQ6MDt0cmFuc2Zvcm0tb3JpZ2luOmxlZnQ7d2lkdGg6OHB4O3dpZHRoOi41cmVtO3RyYW5zZm9ybTpyb3RhdGUoNDVkZWcpfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuYy1hcnJvdzpiZWZvcmV7d2lkdGg6Ljc1cmVtO3dpZHRoOi42MjVyZW19fS5jLWFycm93OmFmdGVye2hlaWdodDoxcHg7aGVpZ2h0Oi4wNjI1cmVtO2JhY2tncm91bmQ6IzU0NzBlMDtkaXNwbGF5OmlubGluZS1ibG9jazt3aWR0aDoxMHB4O3dpZHRoOi42MjVyZW07cG9zaXRpb246cmVsYXRpdmU7dmVydGljYWwtYWxpZ246bWlkZGxlO2NvbnRlbnQ6XCJcIjtwb3NpdGlvbjphYnNvbHV0ZTtsZWZ0OjA7dHJhbnNmb3JtLW9yaWdpbjpsZWZ0O3dpZHRoOjhweDt3aWR0aDouNXJlbTt0cmFuc2Zvcm06cm90YXRlKC00NWRlZyl9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5jLWFycm93OmFmdGVye3dpZHRoOi43NXJlbTt3aWR0aDouNjI1cmVtfX0uYy1hcnJvdy0td2hpdGUsLmMtYXJyb3ctLXdoaXRlOmFmdGVyLC5jLWFycm93LS13aGl0ZTpiZWZvcmV7YmFja2dyb3VuZC1jb2xvcjojZmZmfS5jLWFycm93LS1pbmxpbmV7dHJhbnNmb3JtOnRyYW5zbGF0ZVkoLS4wNjI1cmVtKTttYXJnaW4tcmlnaHQ6MjBweDttYXJnaW4tcmlnaHQ6MS4yNXJlbX0uYy1idXR0b257Zm9udC1mYW1pbHk6TW9udHNlcnJhdCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxMnB4O2ZvbnQtc2l6ZTouNzVyZW07Zm9udC13ZWlnaHQ6NzAwO2xldHRlci1zcGFjaW5nOi4wODMzM2VtO2xpbmUtaGVpZ2h0OjEuMTY2Njc7dGV4dC10cmFuc2Zvcm06dXBwZXJjYXNlfS5jLWJ1dHRvbiwuYy1idXR0b246bGluaywuYy1idXR0b246dmlzaXRlZHstd2Via2l0LWFwcGVhcmFuY2U6bm9uZTtiYWNrZ3JvdW5kLWNvbG9yOiM1NDcwZTA7Ym9yZGVyLXJhZGl1czowO2JvcmRlcjoxcHggc29saWQgdHJhbnNwYXJlbnQ7Ym9yZGVyOi4wNjI1cmVtIHNvbGlkIHRyYW5zcGFyZW50O2NvbG9yOiNmZmY7ZGlzcGxheTppbmxpbmUtYmxvY2s7bWFyZ2luOjA7cGFkZGluZzoxOXB4IDIwcHggMTdweDtwYWRkaW5nOjEuMTg3NXJlbSAxLjI1cmVtIDEuMDYyNXJlbTtwb3NpdGlvbjpyZWxhdGl2ZTt0ZXh0LWFsaWduOmNlbnRlcjt0cmFuc2l0aW9uOmJhY2tncm91bmQtY29sb3IgLjNzIGN1YmljLWJlemllciguNSwwLC41LDEpIDBzLGNvbG9yIC4zcyBjdWJpYy1iZXppZXIoLjUsMCwuNSwxKSAwczt2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7d2lkdGg6MTAwJX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtYnV0dG9uLC5jLWJ1dHRvbjpsaW5rLC5jLWJ1dHRvbjp2aXNpdGVke3BhZGRpbmc6MS41cmVtIDMuMTI1cmVtIDEuMjVyZW19fS5jLWJ1dHRvbjpob3ZlcntiYWNrZ3JvdW5kLWNvbG9yOiMxMTFhM2R9LmMtYnV0dG9uOmRpc2FibGVke29wYWNpdHk6LjM7LW1zLWZpbHRlcjpcInByb2dpZDpEWEltYWdlVHJhbnNmb3JtLk1pY3Jvc29mdC5BbHBoYShPcGFjaXR5PTMwKVwifS5jLWJ1dHRvbjpkaXNhYmxlZDpob3ZlcntiYWNrZ3JvdW5kLWNvbG9yOiM1NDcwZTB9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5jLWJ1dHRvbntmb250LXNpemU6Ljg3NXJlbTtsaW5lLWhlaWdodDoxLjIxNDI5fX0uYy1idXR0b24tLXNlY29uZGFyeSwuYy1idXR0b24tLXNlY29uZGFyeTpsaW5rLC5jLWJ1dHRvbi0tc2Vjb25kYXJ5OnZpc2l0ZWR7YmFja2dyb3VuZC1jb2xvcjp0cmFuc3BhcmVudDtib3JkZXItY29sb3I6IzU2NmJlMjtjb2xvcjojNTQ3MGUwfS5jLWJ1dHRvbi0tc2Vjb25kYXJ5OmhvdmVye2JhY2tncm91bmQtY29sb3I6IzU0NzBlMDtjb2xvcjojZmZmfS5jLWJ1dHRvbi0tc2Vjb25kYXJ5OmhvdmVyOmRpc2FibGVke2JhY2tncm91bmQtY29sb3I6dHJhbnNwYXJlbnQ7Y29sb3I6IzU0NzBlMH0uYy1leHRlcm5hbC1saW5re2ZvbnQtZmFtaWx5Ok1vbnRzZXJyYXQsc2Fucy1zZXJpZjtmb250LXNpemU6MTRweDtmb250LXNpemU6Ljg3NXJlbTtmb250LXdlaWdodDo0MDA7bGluZS1oZWlnaHQ6MS4yMTQyOTstbXMtZmxleC1hbGlnbjpjZW50ZXI7YWxpZ24taXRlbXM6Y2VudGVyO2JvcmRlci1ib3R0b206MXB4IHNvbGlkICNkN2Q3ZDg7Ym9yZGVyLWJvdHRvbTouMDYyNXJlbSBzb2xpZCAjZDdkN2Q4O2JvcmRlci10b3A6MXB4IHNvbGlkICNkN2Q3ZDg7Ym9yZGVyLXRvcDouMDYyNXJlbSBzb2xpZCAjZDdkN2Q4O2Rpc3BsYXk6LW1zLWZsZXhib3g7ZGlzcGxheTpmbGV4Oy1tcy1mbGV4LXBhY2s6anVzdGlmeTtqdXN0aWZ5LWNvbnRlbnQ6c3BhY2UtYmV0d2VlbjttYXJnaW46MTZweCAwIDMycHg7bWFyZ2luOjFyZW0gMCAycmVtO3BhZGRpbmc6MTVweCAwO3BhZGRpbmc6LjkzNzVyZW0gMDt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuYy1leHRlcm5hbC1saW5re2ZvbnQtc2l6ZToxcmVtO2xpbmUtaGVpZ2h0OjEuMzc1fX0uYy1leHRlcm5hbC1saW5rIHN2Z3toZWlnaHQ6MTNweDtoZWlnaHQ6LjgxMjVyZW07d2lkdGg6MTNweDt3aWR0aDouODEyNXJlbX0uYy1leHRlcm5hbC1saW5rLS1lcnJvcntjb2xvcjojZTgyYTJhfS5jLWV4dGVybmFsLWxpbmstLWVycm9yIHN2Z3tmaWxsOiNlODJhMmF9LmMtZm9vdGVye2JhY2tncm91bmQ6IzExMWEzZDtjb2xvcjojZmZmfUBtZWRpYSBwcmludHsuYy1mb290ZXJ7ZGlzcGxheTpub25lfX0uYy1mb290ZXJfX2NvbnRhaW5lcntkaXNwbGF5OmJsb2NrO21heC13aWR0aDoxNDYwcHg7cGFkZGluZzowIDIwcHg7cGFkZGluZzowIDEuMjVyZW07bWFyZ2luOjAgYXV0bztwYWRkaW5nOjE1cHggMjBweDtwYWRkaW5nOi45Mzc1cmVtIDEuMjVyZW19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5jLWZvb3Rlcl9fY29udGFpbmVye21heC13aWR0aDoxNDYwcHg7bWF4LXdpZHRoOjEyMTYuNjY2NjdweDtwYWRkaW5nOjIuNXJlbSAxLjI1cmVtfX0uYy1mb290ZXJfX2xvZ29ze2Rpc3BsYXk6LW1zLWZsZXhib3g7ZGlzcGxheTpmbGV4Oy1tcy1mbGV4LXdyYXA6d3JhcDtmbGV4LXdyYXA6d3JhcDttYXJnaW46MH0uYy1mb290ZXJfX2xvZ29zIGR0e2ZvbnQtZmFtaWx5Ok1vbnRzZXJyYXQsc2Fucy1zZXJpZjtmb250LXNpemU6MTJweDtmb250LXNpemU6Ljc1cmVtO2ZvbnQtd2VpZ2h0OjcwMDtsZXR0ZXItc3BhY2luZzouMDgzMzNlbTtsaW5lLWhlaWdodDoxLjE2NjY3O3RleHQtdHJhbnNmb3JtOnVwcGVyY2FzZTstbXMtZmxleDoxIDAgMTAwJTtmbGV4OjEgMCAxMDAlO21hcmdpbjoyMHB4IDA7bWFyZ2luOjEuMjVyZW0gMDt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuYy1mb290ZXJfX2xvZ29zIGR0e21hcmdpbjowIDAgMS4yNXJlbX19LmMtZm9vdGVyX19sb2dvcyBkZHstbXMtZmxleC1hbGlnbjpjZW50ZXI7YWxpZ24taXRlbXM6Y2VudGVyO2Rpc3BsYXk6LW1zLWZsZXhib3g7ZGlzcGxheTpmbGV4Oy1tcy1mbGV4OjEgMCA1MCU7ZmxleDoxIDAgNTAlO21hcmdpbjowIDAgMjBweDttYXJnaW46MCAwIDEuMjVyZW07d2lkdGg6NTAlfUBtZWRpYSAobWluLXdpZHRoOjYwMHB4KXsuYy1mb290ZXJfX2xvZ29zIGRkey1tcy1mbGV4OjAgMCBhdXRvO2ZsZXg6MCAwIGF1dG87d2lkdGg6YXV0bzttYXJnaW46MDtoZWlnaHQ6My43NXJlbX19LmMtZm9vdGVyX19sb2dvcyBhe3RyYW5zaXRpb246b3BhY2l0eSAuM3MgY3ViaWMtYmV6aWVyKC41LDAsLjUsMSkgMHN9QG1lZGlhIChtaW4td2lkdGg6NjAwcHgpey5jLWZvb3Rlcl9fbG9nb3MgYXttYXJnaW4tdG9wOmF1dG99fS5jLWZvb3Rlcl9fbG9nb3MgYTpob3ZlcntvcGFjaXR5Oi41Oy1tcy1maWx0ZXI6XCJwcm9naWQ6RFhJbWFnZVRyYW5zZm9ybS5NaWNyb3NvZnQuQWxwaGEoT3BhY2l0eT01MClcIn0uYy1mb290ZXJfX2xvZ297ZGlzcGxheTpibG9jazttYXgtaGVpZ2h0OjY0cHg7bWF4LWhlaWdodDo0cmVtO21hcmdpbi1yaWdodDozMHB4O21hcmdpbi1yaWdodDoxLjg3NXJlbX0uYy1mb290ZXJfX2xvZ28tbGFuZHNjYXBle2Rpc3BsYXk6YmxvY2s7bWFyZ2luLXJpZ2h0OjMwcHg7bWFyZ2luLXJpZ2h0OjEuODc1cmVtO21heC13aWR0aDoxNDBweDttYXgtd2lkdGg6OC43NXJlbX0uYy1mb290ZXJfX3N2Zy1oZWFydCBzdmd7d2lkdGg6NzBweDt3aWR0aDo0LjM3NXJlbX0uYy1mb290ZXJfX3N2Zy1kaWFiZXRlcyBzdmcsLmMtZm9vdGVyX19zdmctaGVhcnQgc3Zne2Rpc3BsYXk6YmxvY2s7ZmlsbDojZmZmO2hlaWdodDo2MHB4O2hlaWdodDozLjc1cmVtO21hcmdpbi1yaWdodDozMHB4O21hcmdpbi1yaWdodDoxLjg3NXJlbX0uYy1mb290ZXJfX3N2Zy1kaWFiZXRlcyBzdmd7d2lkdGg6MTAwcHg7d2lkdGg6Ni4yNXJlbTttYXJnaW4tdG9wOi0zMHB4O21hcmdpbi10b3A6LTEuODc1cmVtfUBtZWRpYSAobWluLXdpZHRoOjYwMHB4KXsuYy1mb290ZXJfX3N2Zy1kaWFiZXRlcyBzdmd7bWFyZ2luLXRvcDowfX0uYy1mb290ZXJfX3N2Zy1zdHJva2Ugc3Zne2Rpc3BsYXk6YmxvY2s7ZmlsbDojZmZmO2hlaWdodDo2MHB4O2hlaWdodDozLjc1cmVtO21hcmdpbi1yaWdodDozMHB4O21hcmdpbi1yaWdodDoxLjg3NXJlbTt3aWR0aDoxMDdweDt3aWR0aDo2LjY4NzVyZW19LmMtZm9ybS1jaGVja2JveF9faW5wdXR7bGVmdDotOTk5OWVtO3Bvc2l0aW9uOmFic29sdXRlfS5jLWZvcm0tY2hlY2tib3hfX2lucHV0OmNoZWNrZWQrLmMtZm9ybS1jaGVja2JveF9fbGFiZWw6YmVmb3Jle2JhY2tncm91bmQtY29sb3I6IzAwMH0uYy1mb3JtLWNoZWNrYm94X19pbnB1dDpjaGVja2VkKy5jLWZvcm0tY2hlY2tib3hfX2xhYmVsOmFmdGVye29wYWNpdHk6MTstbXMtZmlsdGVyOlwicHJvZ2lkOkRYSW1hZ2VUcmFuc2Zvcm0uTWljcm9zb2Z0LkFscGhhKE9wYWNpdHk9MTAwKVwifS5jLWZvcm0tY2hlY2tib3hfX2xhYmVse2NvbG9yOiMzNzM4M2M7Y3Vyc29yOnBvaW50ZXI7Zm9udC1zaXplOi44NzVlbTtmb250LXdlaWdodDo0MDA7bGV0dGVyLXNwYWNpbmc6MDtsaW5lLWhlaWdodDoxLjZlbTtwYWRkaW5nLWxlZnQ6MzVweDtwb3NpdGlvbjpyZWxhdGl2ZTt0ZXh0LXRyYW5zZm9ybTpub25lfS5jLWZvcm0tY2hlY2tib3hfX2xhYmVsOmJlZm9yZXtiYWNrZ3JvdW5kOiNmZmY7Ym9yZGVyLXJhZGl1czoycHg7Ym9yZGVyOjFweCBzb2xpZCAjMDAwO2NvbnRlbnQ6XCIuXCI7Y3Vyc29yOnBvaW50ZXI7aGVpZ2h0OjIwcHg7bGVmdDowO3RyYW5zZm9ybTp0cmFuc2xhdGVZKC01MCUpO3Bvc2l0aW9uOmFic29sdXRlO3RleHQtaW5kZW50Oi05OTllbTt0b3A6NTAlO3RyYW5zaXRpb246YmFja2dyb3VuZCAuMnMgZWFzZS1pbi1vdXQ7d2lkdGg6MjBweH0uYy1mb3JtLWNoZWNrYm94X19sYWJlbDphZnRlcntiYWNrZ3JvdW5kLWltYWdlOnVybChkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBEOTRiV3dnZG1WeWMybHZiajBpTVM0d0lpQmxibU52WkdsdVp6MGlkWFJtTFRnaVB6NDhjM1puSUhabGNuTnBiMjQ5SWpFdU1TSWdhV1E5SWt4aGVXVnlYekVpSUhodGJHNXpQU0pvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeUlnZUcxc2JuTTZlR3hwYm1zOUltaDBkSEE2THk5M2QzY3Vkek11YjNKbkx6RTVPVGt2ZUd4cGJtc2lJSGc5SWpCd2VDSWdlVDBpTUhCNElpQjJhV1YzUW05NFBTSXdJREFnTVRBd0lERXdNQ0lnYzNSNWJHVTlJbVZ1WVdKc1pTMWlZV05yWjNKdmRXNWtPbTVsZHlBd0lEQWdNVEF3SURFd01Ec2lJSGh0YkRwemNHRmpaVDBpY0hKbGMyVnlkbVVpUGp4emRIbHNaU0IwZVhCbFBTSjBaWGgwTDJOemN5SStMbk4wTUh0bWFXeHNPaU5HUmtaR1JrWTdmVHd2YzNSNWJHVStQSEJoZEdnZ1kyeGhjM005SW5OME1DSWdaRDBpVFRrMkxqa3NOaTQyWXkweExqY3RNUzQwTFRNdU9TMHlMVFl1TVMweExqaGpMVEl1TWl3d0xqSXROQzR5TERFdU15MDFMallzTXk0eFRETXhMalVzTnpRdU5Vd3hOQzR5TERVM0xqSkRNVEVzTlRRc05TNDNMRFUwTERJdU5DdzFOeTR5WXkwekxqSXNNeTR5TFRNdU1pdzRMalVzTUN3eE1TNDRiREl6TGpnc01qTXVPR014TGpZc01TNDJMRE11Tnl3eUxqUXNOaTR6TERJdU5Hd3dMREJqTWk0MExUQXVNU3cwTGpZdE1TNHpMRFl0TXk0eFREazRMREU0TGpORE1UQXhMREUwTGpnc01UQXdMalVzT1M0MUxEazJMamtzTmk0MmVpSXZQand2YzNablBnPT0pO2JhY2tncm91bmQtcG9zaXRpb246NTAlO2JhY2tncm91bmQtcmVwZWF0Om5vLXJlcGVhdDtiYWNrZ3JvdW5kLXNpemU6Y29udGFpbjtjb250ZW50OlwiXCI7ZGlzcGxheTpibG9jaztoZWlnaHQ6MTBweDtoZWlnaHQ6LjYyNXJlbTtvcGFjaXR5OjA7LW1zLWZpbHRlcjpcInByb2dpZDpEWEltYWdlVHJhbnNmb3JtLk1pY3Jvc29mdC5BbHBoYShPcGFjaXR5PTApXCI7cG9zaXRpb246YWJzb2x1dGU7dG9wOjUwJTt0cmFuc2Zvcm06dHJhbnNsYXRlKDUwJSwtNTAlKTt3aWR0aDoxMHB4O3dpZHRoOi42MjVyZW19LmMtZm9ybS1lcnJvcntmb250LWZhbWlseTpNb250c2VycmF0LHNhbnMtc2VyaWY7Zm9udC1zaXplOjE0cHg7Zm9udC1zaXplOi44NzVyZW07Zm9udC13ZWlnaHQ6NDAwO2xpbmUtaGVpZ2h0OjEuMjE0Mjk7Y29sb3I6I2U4MmEyYTtkaXNwbGF5OmJsb2NrO21hcmdpbjowO3BhZGRpbmctdG9wOjE2cHg7cGFkZGluZy10b3A6MXJlbX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtZm9ybS1lcnJvcntmb250LXNpemU6MXJlbTtsaW5lLWhlaWdodDoxLjM3NX19LmMtZm9ybS1lcnJvci0tbm8tdG9wLXBhZGRpbmd7cGFkZGluZy10b3A6MH0uYy1mb3JtLWxhYmVse2ZvbnQtZmFtaWx5Ok1vbnRzZXJyYXQsc2Fucy1zZXJpZjtmb250LXNpemU6MTJweDtmb250LXNpemU6Ljc1cmVtO2ZvbnQtd2VpZ2h0OjcwMDtsZXR0ZXItc3BhY2luZzouMDgzMzNlbTtsaW5lLWhlaWdodDoxLjE2NjY3O3RleHQtdHJhbnNmb3JtOnVwcGVyY2FzZTtkaXNwbGF5OmJsb2NrO21hcmdpbi1ib3R0b206MTBweDttYXJnaW4tYm90dG9tOi42MjVyZW07Y29sb3I6IzM3MzgzYztvcGFjaXR5Oi43Oy1tcy1maWx0ZXI6XCJwcm9naWQ6RFhJbWFnZVRyYW5zZm9ybS5NaWNyb3NvZnQuQWxwaGEoT3BhY2l0eT03MClcIn1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtZm9ybS1sYWJlbHtmb250LXNpemU6Ljg3NXJlbTtsaW5lLWhlaWdodDoxLjIxNDI5fX0uYy1mb3JtLXJhZGlve2Rpc3BsYXk6aW5saW5lLWJsb2NrO21hcmdpbjowIDFweDttYXJnaW46MCAuMDYyNXJlbTt3aWR0aDpjYWxjKDUwJSAtIDJweCl9LmMtZm9ybS1yYWRpb19fbGFiZWx7Zm9udC1mYW1pbHk6TW9udHNlcnJhdCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNHB4O2ZvbnQtc2l6ZTouODc1cmVtO2ZvbnQtd2VpZ2h0OjQwMDtsaW5lLWhlaWdodDoxLjIxNDI5O2JhY2tncm91bmQtY29sb3I6I2YzZjNmNjtjdXJzb3I6cG9pbnRlcjtkaXNwbGF5OmJsb2NrO3BhZGRpbmc6MTZweDtwYWRkaW5nOjFyZW07cG9zaXRpb246cmVsYXRpdmU7dGV4dC1hbGlnbjpjZW50ZXI7dGV4dC10cmFuc2Zvcm06bm9uZTt0cmFuc2l0aW9uOmJhY2tncm91bmQtY29sb3IgLjNzIGN1YmljLWJlemllciguNSwwLC41LDEpLGNvbG9yIC4zcyBjdWJpYy1iZXppZXIoLjUsMCwuNSwxKTt3aWR0aDoxMDAlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuYy1mb3JtLXJhZGlvX19sYWJlbHtmb250LXNpemU6MXJlbTtsaW5lLWhlaWdodDoxLjM3NX19LmMtZm9ybS1yYWRpb19fbGFiZWw6aG92ZXJ7YmFja2dyb3VuZC1jb2xvcjojZDdkN2Q4fS5jLWZvcm0tcmFkaW9fX2xhYmVsIHN2Z3tkaXNwbGF5OmJsb2NrO2ZpbGw6IzM3MzgzYztoZWlnaHQ6MzBweDtoZWlnaHQ6MS44NzVyZW07bWFyZ2luOjAgYXV0byA0cHg7bWFyZ2luOjAgYXV0byAuMjVyZW07dHJhbnNpdGlvbjpmaWxsIC4zcyBjdWJpYy1iZXppZXIoLjUsMCwuNSwxKTt3aWR0aDoyNXB4O3dpZHRoOjEuNTYyNXJlbX0uYy1mb3JtLXJhZGlvX19pbnB1dHtsZWZ0Oi05OTk5ZW07cG9zaXRpb246YWJzb2x1dGV9LmMtZm9ybS1yYWRpb19faW5wdXQ6Zm9jdXMrLmMtZm9ybS1yYWRpb19fbGFiZWx7YmFja2dyb3VuZC1jb2xvcjojZDdkN2Q4fS5jLWZvcm0tcmFkaW9fX2lucHV0OmNoZWNrZWQrLmMtZm9ybS1yYWRpb19fbGFiZWx7YmFja2dyb3VuZC1jb2xvcjojNTY2YmUyO2NvbG9yOiNmZmZ9LmMtZm9ybS1yYWRpb19faW5wdXQ6Y2hlY2tlZCsuYy1mb3JtLXJhZGlvX19sYWJlbCBzdmd7ZmlsbDojZmZmfS5jLWZvcm0tcmFkaW8tLXRoaXJke3dpZHRoOmNhbGMoMzMlIC0gMnB4KX0uYy1mb3JtLXNlbGVjdHtiYWNrZ3JvdW5kLWNvbG9yOiNmMWYxZjE7Ym9yZGVyOjFweCBzb2xpZCAjZWVlO2NvbG9yOiMzNzM4M2M7Y3Vyc29yOnBvaW50ZXI7ZGlzcGxheTpibG9jaztmb250LXNpemU6Ljg3NWVtO21hcmdpbjowO3BhZGRpbmc6MDtwb3NpdGlvbjpyZWxhdGl2ZX0uYy1mb3JtLXNlbGVjdC5wYXJzbGV5LWVycm9ye2JvcmRlci1jb2xvcjojMDAwfS5jLWZvcm0tc2VsZWN0OmJlZm9yZXtiYWNrZ3JvdW5kLWltYWdlOnVybChkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBEOTRiV3dnZG1WeWMybHZiajBpTVM0d0lpQmxibU52WkdsdVp6MGlkWFJtTFRnaVB6NDhjM1puSUhabGNuTnBiMjQ5SWpFdU1TSWdhV1E5SWt4aGVXVnlYekVpSUhodGJHNXpQU0pvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeUlnZUcxc2JuTTZlR3hwYm1zOUltaDBkSEE2THk5M2QzY3Vkek11YjNKbkx6RTVPVGt2ZUd4cGJtc2lJSGc5SWpCd2VDSWdlVDBpTUhCNElpQjNhV1IwYUQwaU5UQXdjSGdpSUdobGFXZG9kRDBpTlRBd2NIZ2lJSFpwWlhkQ2IzZzlJakFnTUNBMU1EQWdOVEF3SWlCemRIbHNaVDBpWlc1aFlteGxMV0poWTJ0bmNtOTFibVE2Ym1WM0lEQWdNQ0ExTURBZ05UQXdPeUlnZUcxc09uTndZV05sUFNKd2NtVnpaWEoyWlNJK1BIQmhkR2dnWkQwaVRUUXhOQzQ0TERFeE5DNDBURE13TUM0ekxESXlPUzQxYkMwMU1DdzBPUzQxYkMwMU1DMDBPUzQxVERnMUxqY3NNVEUwTGpSakxURXdMVEV3TFRJeUxqVXRNVFF1TlMwek5TNDFMVEUwTGpWekxUSTFMalVzTlMwek5TNDFMREUwTGpWakxURTVMalVzTVRrdU5TMHhPUzQxTERVeExqVXNNQ3czTVd3eU1EQXVNU3d5TURBdU1XTXlNU3d5TUM0MUxEVXlMalVzTVRndU5TdzNNQzQxTERCc01qQXdMakV0TWpBd0xqRmpNVGt1TlMweE9TNDFMREU1TGpVdE5URXNNQzAzTUM0MVF6UTJOaTQwTERrMExqa3NORE0wTGpNc09UUXVPU3cwTVRRdU9Dd3hNVFF1TkhvaUx6NDhMM04yWno0PSk7YmFja2dyb3VuZC1wb3NpdGlvbjo1MCU7YmFja2dyb3VuZC1yZXBlYXQ6bm8tcmVwZWF0O2JhY2tncm91bmQtc2l6ZTouNzVyZW0gYXV0bztjb250ZW50OlwiXCI7ZGlzcGxheTpibG9jaztmb250LXNpemU6MTFweDtmb250LXNpemU6LjY4NzVyZW07aGVpZ2h0OjEwMCU7bGluZS1oZWlnaHQ6MTtwb3NpdGlvbjphYnNvbHV0ZTtyaWdodDowO3RvcDo1MCU7dHJhbnNmb3JtOnRyYW5zbGF0ZVkoLTUwJSk7d2lkdGg6NTBweDt3aWR0aDozLjEyNXJlbX0ubHQtaWUxMCAuYy1mb3JtLXNlbGVjdDpiZWZvcmV7ZGlzcGxheTpub25lfS5jLWZvcm0tc2VsZWN0IHNlbGVjdDo6LW1zLWV4cGFuZHtkaXNwbGF5Om5vbmV9LmMtZm9ybS1zZWxlY3RfX2lucHV0ey1tb3otYXBwZWFyYW5jZTpub25lOy13ZWJraXQtYXBwZWFyYW5jZTpub25lO2FwcGVhcmFuY2U6bm9uZTtiYWNrZ3JvdW5kLWNvbG9yOnRyYW5zcGFyZW50O2JhY2tncm91bmQtaW1hZ2U6bm9uZTtib3JkZXI6bm9uZTtib3gtc2hhZG93Om5vbmU7Y29sb3I6IzM3MzgzYztjdXJzb3I6cG9pbnRlcjtmb250LXNpemU6MTRweDtmb250LXNpemU6Ljg3NXJlbTtsaW5lLWhlaWdodDpub3JtYWw7bGluZS1oZWlnaHQ6MTtwYWRkaW5nOjE2cHggMTVweDtwYWRkaW5nOjFyZW0gLjkzNzVyZW07cG9zaXRpb246cmVsYXRpdmU7d2lkdGg6MTAwJX0ubHQtaWUxMCAuYy1mb3JtLXNlbGVjdF9faW5wdXR7cGFkZGluZzoxMXB4O3BhZGRpbmc6LjY4NzVyZW19LmMtZm9ybS1zdGVwcGVye3dpZHRoOjEwMCV9LmMtZm9ybS1zdGVwcGVyX19maWVsZHtwYWRkaW5nLWJvdHRvbToyNHB4O3BhZGRpbmctYm90dG9tOjEuNXJlbX0uYy1mb3JtLXRleHR7Zm9udC1mYW1pbHk6TW9udHNlcnJhdCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNHB4O2ZvbnQtc2l6ZTouODc1cmVtO2ZvbnQtd2VpZ2h0OjQwMDtsaW5lLWhlaWdodDoxLjIxNDI5O3Bvc2l0aW9uOnJlbGF0aXZlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuYy1mb3JtLXRleHR7Zm9udC1zaXplOjFyZW07bGluZS1oZWlnaHQ6MS4zNzV9fS5jLWZvcm0tdGV4dCBpbnB1dCwuYy1mb3JtLXRleHQgdGV4dGFyZWF7LXdlYmtpdC1hcHBlYXJhbmNlOm5vbmU7LW1vei1hcHBlYXJhbmNlOm5vbmU7YXBwZWFyYW5jZTpub25lO2JhY2tncm91bmQ6I2YzZjNmNjtib3JkZXItcmFkaXVzOjA7Ym9yZGVyOjFweCBzb2xpZCAjZjNmM2Y2O2NvbG9yOiMzNzM4M2M7cGFkZGluZzoxNnB4IDgwcHggMTZweCAxNXB4O3BhZGRpbmc6MXJlbSA1cmVtIDFyZW0gLjkzNzVyZW07dHJhbnNpdGlvbjpib3JkZXItY29sb3IgLjNzIGN1YmljLWJlemllciguNSwwLC41LDEpLGJhY2tncm91bmQtY29sb3IgLjNzIGN1YmljLWJlemllciguNSwwLC41LDEpO3dpZHRoOjEwMCV9LmMtZm9ybS10ZXh0IGlucHV0Ojotd2Via2l0LWlucHV0LXBsYWNlaG9sZGVyLC5jLWZvcm0tdGV4dCB0ZXh0YXJlYTo6LXdlYmtpdC1pbnB1dC1wbGFjZWhvbGRlcntjb2xvcjojMzczODNjO29wYWNpdHk6Ljg7LW1zLWZpbHRlcjpcInByb2dpZDpEWEltYWdlVHJhbnNmb3JtLk1pY3Jvc29mdC5BbHBoYShPcGFjaXR5PTgwKVwifS5jLWZvcm0tdGV4dCBpbnB1dDotbXMtaW5wdXQtcGxhY2Vob2xkZXIsLmMtZm9ybS10ZXh0IHRleHRhcmVhOi1tcy1pbnB1dC1wbGFjZWhvbGRlcntjb2xvcjojMzczODNjO29wYWNpdHk6Ljg7LW1zLWZpbHRlcjpcInByb2dpZDpEWEltYWdlVHJhbnNmb3JtLk1pY3Jvc29mdC5BbHBoYShPcGFjaXR5PTgwKVwifS5jLWZvcm0tdGV4dCBpbnB1dDo6cGxhY2Vob2xkZXIsLmMtZm9ybS10ZXh0IHRleHRhcmVhOjpwbGFjZWhvbGRlcntjb2xvcjojMzczODNjO29wYWNpdHk6Ljg7LW1zLWZpbHRlcjpcInByb2dpZDpEWEltYWdlVHJhbnNmb3JtLk1pY3Jvc29mdC5BbHBoYShPcGFjaXR5PTgwKVwifS5jLWZvcm0tdGV4dCBpbnB1dDpob3ZlciwuYy1mb3JtLXRleHQgdGV4dGFyZWE6aG92ZXJ7YmFja2dyb3VuZC1jb2xvcjojZDdkN2Q4fS5jLWZvcm0tdGV4dCBpbnB1dDpmb2N1cywuYy1mb3JtLXRleHQgdGV4dGFyZWE6Zm9jdXN7b3V0bGluZTpub25lO2JvcmRlci1jb2xvcjojNTQ3MGUwfS5jLWZvcm0tdGV4dCBpbnB1dDpkaXNhYmxlZCwuYy1mb3JtLXRleHQgdGV4dGFyZWE6ZGlzYWJsZWR7b3BhY2l0eToxOy1tcy1maWx0ZXI6XCJwcm9naWQ6RFhJbWFnZVRyYW5zZm9ybS5NaWNyb3NvZnQuQWxwaGEoT3BhY2l0eT0xMDApXCJ9Lmhhcy1lcnJvciAuYy1mb3JtLXRleHQgaW5wdXQsLmhhcy1lcnJvciAuYy1mb3JtLXRleHQgdGV4dGFyZWF7Ym9yZGVyLWNvbG9yOiNlODJhMmF9LmMtZm9ybS10ZXh0IGlucHV0W3R5cGU9bnVtYmVyXSwuYy1mb3JtLXRleHQgdGV4dGFyZWFbdHlwZT1udW1iZXJdey1tb3otYXBwZWFyYW5jZTp0ZXh0ZmllbGR9LmMtZm9ybS10ZXh0IGlucHV0W3R5cGU9bnVtYmVyXTo6LXdlYmtpdC1pbm5lci1zcGluLWJ1dHRvbiwuYy1mb3JtLXRleHQgaW5wdXRbdHlwZT1udW1iZXJdOjotd2Via2l0LW91dGVyLXNwaW4tYnV0dG9uLC5jLWZvcm0tdGV4dCB0ZXh0YXJlYVt0eXBlPW51bWJlcl06Oi13ZWJraXQtaW5uZXItc3Bpbi1idXR0b24sLmMtZm9ybS10ZXh0IHRleHRhcmVhW3R5cGU9bnVtYmVyXTo6LXdlYmtpdC1vdXRlci1zcGluLWJ1dHRvbnstd2Via2l0LWFwcGVhcmFuY2U6bm9uZTttYXJnaW46MH0uYy1mb3JtLXRleHRfX3N1ZmZpeHtwb3NpdGlvbjphYnNvbHV0ZTtyaWdodDoxNnB4O3JpZ2h0OjFyZW07dG9wOjUwJTt0cmFuc2Zvcm06dHJhbnNsYXRlWSgtNTAlKX0uYy1oZWFkZXJ7YmFja2dyb3VuZDpsaW5lYXItZ3JhZGllbnQoMzE1ZGVnLCM3YmJiZWIsIzU2NmJlMik7Y29sb3I6I2ZmZn0uYy1oZWFkZXJfX2NvbnRhaW5lcntkaXNwbGF5OmJsb2NrO21heC13aWR0aDoxNDYwcHg7cGFkZGluZzowIDIwcHg7cGFkZGluZzowIDEuMjVyZW07bWFyZ2luOjAgYXV0bztwYWRkaW5nOjMwcHggMjBweDtwYWRkaW5nOjEuODc1cmVtIDEuMjVyZW19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5jLWhlYWRlcl9fY29udGFpbmVye21heC13aWR0aDoxNDYwcHg7cGFkZGluZzoyLjVyZW0gMS4yNXJlbX19QG1lZGlhIHByaW50ey5jLWhlYWRlcl9fY29udGFpbmVye3BhZGRpbmc6MS4yNXJlbX19LmMtaGVhZGVyX19iYWNre2ZvbnQtZmFtaWx5Ok1vbnRzZXJyYXQsc2Fucy1zZXJpZjtmb250LXNpemU6MTRweDtmb250LXNpemU6Ljg3NXJlbTtmb250LXdlaWdodDo0MDA7bGluZS1oZWlnaHQ6MS4yMTQyOX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtaGVhZGVyX19iYWNre2ZvbnQtc2l6ZToxcmVtO2xpbmUtaGVpZ2h0OjEuMzc1fX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5jLWhlYWRlcl9fYmFja3ttYXJnaW4tbGVmdDo4LjMzMzMzJX19LmMtaGVhZGVyX19iYWNrLC5jLWhlYWRlcl9fYmFjazpsaW5rLC5jLWhlYWRlcl9fYmFjazp2aXNpdGVke2NvbG9yOiNmZmY7ZGlzcGxheTppbmxpbmUtYmxvY2s7bWFyZ2luLWJvdHRvbToyMHB4O21hcmdpbi1ib3R0b206MS4yNXJlbX1AbWVkaWEgcHJpbnR7LmMtaGVhZGVyX19iYWNrLC5jLWhlYWRlcl9fYmFjazpsaW5rLC5jLWhlYWRlcl9fYmFjazp2aXNpdGVke2Rpc3BsYXk6bm9uZX19LmMtaGVhZGVyX19iYWNrOmhvdmVye3RleHQtZGVjb3JhdGlvbjp1bmRlcmxpbmV9LmMtaGVhZGVyX190aXRsZXtmb250LWZhbWlseTpNb250c2VycmF0LHNhbnMtc2VyaWY7Zm9udC1zaXplOjI0cHg7Zm9udC1zaXplOjEuNXJlbTtmb250LXdlaWdodDo4MDA7bGluZS1oZWlnaHQ6MS4yNTttYXJnaW46MH1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtaGVhZGVyX190aXRsZXtmb250LXNpemU6Mi4yNXJlbTtsaW5lLWhlaWdodDoxLjM2ODQyfX1AbWVkaWEgKG1pbi13aWR0aDoxMjAwcHgpey5jLWhlYWRlcl9fdGl0bGV7bWFyZ2luLWxlZnQ6OC4zMzMzMyV9fS5jLWhlYWRlci0tbmFycm93IC5jLWhlYWRlcl9fYmFjaywuYy1oZWFkZXItLW5hcnJvdyAuYy1oZWFkZXJfX3RpdGxle21hcmdpbi1sZWZ0OjB9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5jLWhlYWRlci0tbmFycm93IC5jLWhlYWRlcl9fY29udGFpbmVye21heC13aWR0aDo3MzBweH19LmMtbGlzdHtsaXN0LXN0eWxlLXR5cGU6bm9uZTttYXJnaW4tYm90dG9tOjMwcHg7bWFyZ2luLWJvdHRvbToxLjg3NXJlbTtwYWRkaW5nOjA7cG9zaXRpb246cmVsYXRpdmU7b3ZlcmZsb3c6aGlkZGVufS5jLWxpc3QgbGl7bWFyZ2luLWJvdHRvbToxMHB4O21hcmdpbi1ib3R0b206LjYyNXJlbTtwYWRkaW5nLWxlZnQ6MzBweDtwYWRkaW5nLWxlZnQ6MS44NzVyZW07cG9zaXRpb246cmVsYXRpdmV9LmMtbGlzdCBsaTpiZWZvcmV7Y29sb3I6IzAwMDtkaXNwbGF5OmlubGluZS1ibG9jaztsZWZ0OjA7bGluZS1oZWlnaHQ6MTtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDt2ZXJ0aWNhbC1hbGlnbjptaWRkbGV9LmMtbGlzdC0tdW5vcmRlcmVkIGxpOmJlZm9yZXtjb250ZW50OlwiLlwiO2ZvbnQtc2l6ZTozNXB4O2ZvbnQtc2l6ZToyLjE4NzVyZW07bGluZS1oZWlnaHQ6MTBweDt0b3A6LS4wN2VtfS5jLWxpc3QtLW9yZGVyZWR7Y291bnRlci1yZXNldDphfS5jLWxpc3QtLW9yZGVyZWQgbGk6YmVmb3Jle2NvbnRlbnQ6Y291bnRlcihhLGRlY2ltYWwpIFwiLlwiO2NvdW50ZXItaW5jcmVtZW50OmE7Zm9udC13ZWlnaHQ6NjAwO2xlZnQ6MDt0b3A6LjI3NWVtfS5jLWxpc3QtLW9yZGVyZWQgb2wgbGk6YmVmb3Jle2NvbnRlbnQ6Y291bnRlcihhKX0uYy1wYW5lbHtib3JkZXItYm90dG9tOjFweCBzb2xpZCAjZDdkN2Q4O2JvcmRlci1ib3R0b206LjA2MjVyZW0gc29saWQgI2Q3ZDdkODtib3JkZXItdG9wOjFweCBzb2xpZCAjZDdkN2Q4O2JvcmRlci10b3A6LjA2MjVyZW0gc29saWQgI2Q3ZDdkODttYXJnaW4tdG9wOi0xcHg7bWFyZ2luLXRvcDotLjA2MjVyZW07cGFkZGluZy10b3A6MTVweDtwYWRkaW5nLXRvcDouOTM3NXJlbX0uYy1wYW5lbF9faGVhZGVye2ZvbnQtZmFtaWx5Ok1vbnRzZXJyYXQsc2Fucy1zZXJpZjtmb250LXNpemU6MTRweDtmb250LXNpemU6Ljg3NXJlbTtmb250LXdlaWdodDo0MDA7bGluZS1oZWlnaHQ6MS4yMTQyOTstbXMtZmxleC1hbGlnbjpjZW50ZXI7YWxpZ24taXRlbXM6Y2VudGVyO2Rpc3BsYXk6LW1zLWZsZXhib3g7ZGlzcGxheTpmbGV4Oy1tcy1mbGV4LXBhY2s6anVzdGlmeTtqdXN0aWZ5LWNvbnRlbnQ6c3BhY2UtYmV0d2Vlbjt3aWR0aDoxMDAlO21hcmdpbi1ib3R0b206MTVweDttYXJnaW4tYm90dG9tOi45Mzc1cmVtfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsuYy1wYW5lbF9faGVhZGVye2ZvbnQtc2l6ZToxcmVtO2xpbmUtaGVpZ2h0OjEuMzc1fX0uYy1wYW5lbF9faGVhZGVyOmZvY3VzLC5jLXBhbmVsX19oZWFkZXI6aG92ZXJ7b3V0bGluZTpub25lfS5jLXBhbmVsX19oZWFkZXIgLmMtYXJyb3d7dHJhbnNmb3JtOnJvdGF0ZSgyNzBkZWcpfS5pcy1vcGVuIC5jLXBhbmVsX19oZWFkZXIgLmMtYXJyb3d7dHJhbnNmb3JtOnJvdGF0ZSg5MGRlZyl9LmMtcGFuZWxfX2hlYWRlcjpmb2N1cyAuYy1wYW5lbF9faGVhZGVyLWlubmVyLC5jLXBhbmVsX19oZWFkZXI6aG92ZXIgLmMtcGFuZWxfX2hlYWRlci1pbm5lcntib3JkZXItY29sb3I6IzM3MzgzY30uYy1wYW5lbF9faGVhZGVyLWlubmVyLC5jLXBhbmVsX19oZWFkZXItaW5uZXI6bGluaywuYy1wYW5lbF9faGVhZGVyLWlubmVyOnZpc2l0ZWR7Ym9yZGVyLWJvdHRvbToxcHggc29saWQgdHJhbnNwYXJlbnQ7dHJhbnNpdGlvbjpib3JkZXItY29sb3IgLjNzIGN1YmljLWJlemllciguNSwwLC41LDEpIDBzfS5jLXBhbmVsX19oZWFkZXItaW5uZXI6aG92ZXJ7Ym9yZGVyLWNvbG9yOiMzNzM4M2N9LmMtcGFuZWxfX2NvbnRlbnR7Zm9udC1mYW1pbHk6TW9udHNlcnJhdCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNHB4O2ZvbnQtc2l6ZTouODc1cmVtO2ZvbnQtd2VpZ2h0OjQwMDtsaW5lLWhlaWdodDoxLjIxNDI5O21hcmdpbjoyMHB4IDA7bWFyZ2luOjEuMjVyZW0gMH1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtcGFuZWxfX2NvbnRlbnR7Zm9udC1zaXplOjFyZW07bGluZS1oZWlnaHQ6MS4zNzV9fS5qcyAuYy1wYW5lbF9fY29udGVudHtkaXNwbGF5Om5vbmV9QG1lZGlhIHByaW50ey5qcyAuYy1wYW5lbF9fY29udGVudHtkaXNwbGF5OmJsb2NrfX0uaXMtb3BlbiAuYy1wYW5lbF9fY29udGVudHtkaXNwbGF5OmJsb2NrfS5jLXBhbmVsX19jb250ZW50IHB7bWFyZ2luLWJvdHRvbToxNXB4O21hcmdpbi1ib3R0b206LjkzNzVyZW19LmMtcGFuZWxfX2NvbnRlbnQgZGx7LW1zLWZsZXgtYWxpZ246Y2VudGVyO2FsaWduLWl0ZW1zOmNlbnRlcjtkaXNwbGF5Oi1tcy1mbGV4Ym94O2Rpc3BsYXk6ZmxleDstbXMtZmxleC1wYWNrOmp1c3RpZnk7anVzdGlmeS1jb250ZW50OnNwYWNlLWJldHdlZW47bWFyZ2luLWJvdHRvbToxMHB4O21hcmdpbi1ib3R0b206LjYyNXJlbX0uYy1wYW5lbF9fY29udGVudCBkZCwuYy1wYW5lbF9fY29udGVudCBkdHtwYWRkaW5nOjB9LmMtcGFuZWxfX2NvbnRlbnQgOmxhc3QtY2hpbGR7bWFyZ2luLWJvdHRvbTowfS5jLXBhbmVsLS1tYXJnaW4tYm90dG9te21hcmdpbi1ib3R0b206MjRweDttYXJnaW4tYm90dG9tOjEuNXJlbX0uYy1yZXN1bHQtZ3JhcGhpY3stbXMtZmxleC1hbGlnbjpjZW50ZXI7YWxpZ24taXRlbXM6Y2VudGVyO2Rpc3BsYXk6LW1zLWZsZXhib3g7ZGlzcGxheTpmbGV4Oy1tcy1mbGV4LXBhY2s6anVzdGlmeTtqdXN0aWZ5LWNvbnRlbnQ6c3BhY2UtYmV0d2VlbjttYXJnaW4tYm90dG9tOjIwcHg7bWFyZ2luLWJvdHRvbToxLjI1cmVtO2ZvbnQtZmFtaWx5Ok1vbnRzZXJyYXQsc2Fucy1zZXJpZjtmb250LXNpemU6MTRweDtmb250LXNpemU6Ljg3NXJlbTtmb250LXdlaWdodDo0MDA7bGluZS1oZWlnaHQ6MS4yMTQyOX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtcmVzdWx0LWdyYXBoaWN7LW1zLWZsZXgtYWxpZ246dG9wO2FsaWduLWl0ZW1zOnRvcH19QG1lZGlhIHByaW50ey5jLXJlc3VsdC1ncmFwaGlje21heC13aWR0aDoyNXJlbTtwYWdlLWJyZWFrLWluc2lkZTphdm9pZH19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey5jLXJlc3VsdC1ncmFwaGlje2ZvbnQtc2l6ZToxcmVtO2xpbmUtaGVpZ2h0OjEuMzc1fX0uYy1yZXN1bHQtZ3JhcGhpY19fcGVyY2VudGFnZXtmb250LWZhbWlseTpNb250c2VycmF0LHNhbnMtc2VyaWY7Zm9udC13ZWlnaHQ6ODAwO2ZvbnQtc2l6ZTozNnB4O2ZvbnQtc2l6ZToyLjI1cmVtO2xpbmUtaGVpZ2h0OjEuMzgwOTU7bWFyZ2luLWJvdHRvbTowO3RyYW5zZm9ybTp0cmFuc2xhdGVZKC40Mzc1cmVtKX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LmMtcmVzdWx0LWdyYXBoaWNfX3BlcmNlbnRhZ2V7Zm9udC1zaXplOjRyZW07bGluZS1oZWlnaHQ6MS4zNDM3NTt0cmFuc2Zvcm06dHJhbnNsYXRlWSgtLjI1cmVtKX19LmMtcmVzdWx0LWdyYXBoaWNfX2NoYXJ0e3doaXRlLXNwYWNlOm5vd3JhcH0uYy1yZXN1bHQtZ3JhcGhpY19fY2hhcnQgbGl7ZGlzcGxheTppbmxpbmUtYmxvY2s7dGV4dC1hbGlnbjpjZW50ZXI7d2lkdGg6NzBweDt3aWR0aDo0LjM3NXJlbTttYXJnaW4tcmlnaHQ6MXB4O21hcmdpbi1yaWdodDouMDYyNXJlbX0uYy1yZXN1bHQtZ3JhcGhpY19fY2hhcnQgbGk6bGFzdC1jaGlsZHttYXJnaW4tcmlnaHQ6MXB4O21hcmdpbi1yaWdodDouMDYyNXJlbX0uYy1yZXN1bHQtZ3JhcGhpY19fY2hhcnQgbGkgc3Zne2Rpc3BsYXk6YmxvY2s7ZmlsbDojZjNmM2Y2O2hlaWdodDo3MHB4O2hlaWdodDo0LjM3NXJlbTt3aWR0aDo3MHB4O3dpZHRoOjQuMzc1cmVtO21hcmdpbi1ib3R0b206MTBweDttYXJnaW4tYm90dG9tOi42MjVyZW19LmMtcmVzdWx0LWdyYXBoaWNfX2NoYXJ0IGxpIHN2Zy5pcy1ncmVlbntmaWxsOiM1NWFmMjd9LmMtcmVzdWx0LWdyYXBoaWNfX2NoYXJ0IGxpIHN2Zy5pcy15ZWxsb3d7ZmlsbDojZmJjZTJmfS5jLXJlc3VsdC1ncmFwaGljX19jaGFydCBsaSBzdmcuaXMtcmVke2ZpbGw6I2U4MmEyYX0uYy1yZXN1bHQtZ3JhcGhpYy0tbG93IC5jLXJlc3VsdC1ncmFwaGljX19wZXJjZW50YWdle2NvbG9yOiM1NWFmMjd9LmMtcmVzdWx0LWdyYXBoaWMtLW1vZGVyYXRlIC5jLXJlc3VsdC1ncmFwaGljX19wZXJjZW50YWdle2NvbG9yOiNmYmNlMmZ9LmMtcmVzdWx0LWdyYXBoaWMtLWhpZ2ggLmMtcmVzdWx0LWdyYXBoaWNfX3BlcmNlbnRhZ2V7Y29sb3I6I2U4MmEyYX0udS12aXN1YWxseS1oaWRkZW57Ym9yZGVyOjAhaW1wb3J0YW50O2NsaXA6cmVjdCgxcHggMXB4IDFweCAxcHgpO2NsaXA6cmVjdCgxcHgsMXB4LDFweCwxcHgpO2hlaWdodDoxcHghaW1wb3J0YW50O292ZXJmbG93OmhpZGRlbjtwYWRkaW5nOjAhaW1wb3J0YW50O3Bvc2l0aW9uOmFic29sdXRlIWltcG9ydGFudDt3aWR0aDoxcHghaW1wb3J0YW50fS51LXNraXAtdG8tY29udGVudHtsZWZ0OjA7bWFyZ2luLWxlZnQ6LTk5OTllbTtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MH0udS1za2lwLXRvLWNvbnRlbnQ6Zm9jdXN7bWFyZ2luLWxlZnQ6MH0udS1ibG9jay51LWJsb2Nre2Rpc3BsYXk6YmxvY2t9LnUtaW5saW5lLWJsb2NrLnUtaW5saW5lLWJsb2Nre2Rpc3BsYXk6aW5saW5lLWJsb2NrfS51LWJsb2NrXFxAbWVkaXVtLnUtYmxvY2tcXEBtZWRpdW17ZGlzcGxheTpibG9ja30udS1pbmxpbmUtYmxvY2tcXEBtZWRpdW0udS1pbmxpbmUtYmxvY2tcXEBtZWRpdW17ZGlzcGxheTppbmxpbmUtYmxvY2t9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LWZsb2F0LWxlZnRcXEBtZWRpdW0udS1mbG9hdC1sZWZ0XFxAbWVkaXVte2Zsb2F0OmxlZnQhaW1wb3J0YW50fX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LnUtZmxvYXQtcmlnaHRcXEBtZWRpdW0udS1mbG9hdC1yaWdodFxcQG1lZGl1bXtmbG9hdDpyaWdodCFpbXBvcnRhbnR9fS51LWNsZWFyZml4LnUtY2xlYXJmaXh7em9vbToxfS51LWNsZWFyZml4LnUtY2xlYXJmaXg6YWZ0ZXIsLnUtY2xlYXJmaXgudS1jbGVhcmZpeDpiZWZvcmV7Y29udGVudDpcIlwiO2Rpc3BsYXk6dGFibGV9LnUtY2xlYXJmaXgudS1jbGVhcmZpeDphZnRlcntjbGVhcjpib3RofS51LXNob3dcXEB4bGFyZ2UudS1zaG93XFxAeGxhcmdle2Rpc3BsYXk6bm9uZX1AbWVkaWEgKG1pbi13aWR0aDoxNDAwcHgpey51LXNob3dcXEB4bGFyZ2UudS1zaG93XFxAeGxhcmdle2Rpc3BsYXk6YmxvY2t9fUBtZWRpYSAobWluLXdpZHRoOjE0MDBweCl7LnUtaGlkZVxcQHhsYXJnZS51LWhpZGVcXEB4bGFyZ2V7ZGlzcGxheTpub25lfX0udS1zaG93XFxAbGFyZ2UudS1zaG93XFxAbGFyZ2V7ZGlzcGxheTpub25lfUBtZWRpYSAobWluLXdpZHRoOjEyMDBweCl7LnUtc2hvd1xcQGxhcmdlLnUtc2hvd1xcQGxhcmdle2Rpc3BsYXk6YmxvY2t9fUBtZWRpYSAobWluLXdpZHRoOjEyMDBweCl7LnUtaGlkZVxcQGxhcmdlLnUtaGlkZVxcQGxhcmdle2Rpc3BsYXk6bm9uZX19LnUtc2hvd1xcQG1lZGl1bS51LXNob3dcXEBtZWRpdW17ZGlzcGxheTpub25lfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsudS1zaG93XFxAbWVkaXVtLnUtc2hvd1xcQG1lZGl1bXtkaXNwbGF5OmJsb2NrfX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LnUtaGlkZVxcQG1lZGl1bS51LWhpZGVcXEBtZWRpdW17ZGlzcGxheTpub25lfX0udS1zaG93XFxAc21hbGwudS1zaG93XFxAc21hbGx7ZGlzcGxheTpub25lfUBtZWRpYSAobWluLXdpZHRoOjYwMHB4KXsudS1zaG93XFxAc21hbGwudS1zaG93XFxAc21hbGx7ZGlzcGxheTpibG9ja319QG1lZGlhIChtaW4td2lkdGg6NjAwcHgpey51LWhpZGVcXEBzbWFsbC51LWhpZGVcXEBzbWFsbHtkaXNwbGF5Om5vbmV9fUBtZWRpYSBwcmludHsudS1oaWRlXFxAcHJpbnQudS1oaWRlXFxAcHJpbnR7ZGlzcGxheTpub25lfX0udS1zcGFjaW5nLXRvcC16ZXJvLnUtc3BhY2luZy10b3AtemVyb3ttYXJnaW4tdG9wOjB9LnUtc3BhY2luZy1ib3R0b20temVyby51LXNwYWNpbmctYm90dG9tLXplcm97bWFyZ2luLWJvdHRvbTowfS51LXNwYWNpbmctdG9wLXNtYWxsLnUtc3BhY2luZy10b3Atc21hbGx7bWFyZ2luLXRvcDoxNXB4O21hcmdpbi10b3A6LjkzNzVyZW19LnUtc3BhY2luZy1ib3R0b20tc21hbGwudS1zcGFjaW5nLWJvdHRvbS1zbWFsbHttYXJnaW4tYm90dG9tOjE1cHg7bWFyZ2luLWJvdHRvbTouOTM3NXJlbX0udS1zcGFjaW5nLXRvcC1iYXNlLnUtc3BhY2luZy10b3AtYmFzZXttYXJnaW4tdG9wOjIwcHg7bWFyZ2luLXRvcDoxLjI1cmVtfS51LXNwYWNpbmctYm90dG9tLWJhc2UudS1zcGFjaW5nLWJvdHRvbS1iYXNle21hcmdpbi1ib3R0b206MjBweDttYXJnaW4tYm90dG9tOjEuMjVyZW19LnUtc3BhY2luZy10b3AtbWVkaXVtLnUtc3BhY2luZy10b3AtbWVkaXVte21hcmdpbi10b3A6MzBweDttYXJnaW4tdG9wOjEuODc1cmVtfS51LXNwYWNpbmctYm90dG9tLW1lZGl1bS51LXNwYWNpbmctYm90dG9tLW1lZGl1bXttYXJnaW4tYm90dG9tOjMwcHg7bWFyZ2luLWJvdHRvbToxLjg3NXJlbX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LnUtc3BhY2luZy10b3AtemVyb1xcQG1lZGl1bS51LXNwYWNpbmctdG9wLXplcm9cXEBtZWRpdW17bWFyZ2luLXRvcDowfX1AbWVkaWEgcHJpbnR7LnUtc3BhY2luZy10b3AtemVyb1xcQG1lZGl1bS51LXNwYWNpbmctdG9wLXplcm9cXEBtZWRpdW17bWFyZ2luLXRvcDoxMS4yNXJlbX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LXNwYWNpbmctYm90dG9tLXplcm9cXEBtZWRpdW0udS1zcGFjaW5nLWJvdHRvbS16ZXJvXFxAbWVkaXVte21hcmdpbi1ib3R0b206MH19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LXNwYWNpbmctdG9wLXNtYWxsXFxAbWVkaXVtLnUtc3BhY2luZy10b3Atc21hbGxcXEBtZWRpdW17bWFyZ2luLXRvcDouOTM3NXJlbX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LXNwYWNpbmctYm90dG9tLXNtYWxsXFxAbWVkaXVtLnUtc3BhY2luZy1ib3R0b20tc21hbGxcXEBtZWRpdW17bWFyZ2luLWJvdHRvbTouOTM3NXJlbX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LXNwYWNpbmctdG9wLWJhc2VcXEBtZWRpdW0udS1zcGFjaW5nLXRvcC1iYXNlXFxAbWVkaXVte21hcmdpbi10b3A6MS4yNXJlbX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LXNwYWNpbmctYm90dG9tLWJhc2VcXEBtZWRpdW0udS1zcGFjaW5nLWJvdHRvbS1iYXNlXFxAbWVkaXVte21hcmdpbi1ib3R0b206MS4yNXJlbX19QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LXNwYWNpbmctdG9wLW1lZGl1bVxcQG1lZGl1bS51LXNwYWNpbmctdG9wLW1lZGl1bVxcQG1lZGl1bXttYXJnaW4tdG9wOjEuODc1cmVtfX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LnUtc3BhY2luZy1ib3R0b20tbWVkaXVtXFxAbWVkaXVtLnUtc3BhY2luZy1ib3R0b20tbWVkaXVtXFxAbWVkaXVte21hcmdpbi1ib3R0b206MS44NzVyZW19fS51LWhlYWRpbmctMXtmb250LWZhbWlseTpNb250c2VycmF0LHNhbnMtc2VyaWY7Zm9udC1zaXplOjI0cHg7Zm9udC1zaXplOjEuNXJlbTtmb250LXdlaWdodDo4MDA7bGluZS1oZWlnaHQ6MS4yNX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LnUtaGVhZGluZy0xe2ZvbnQtc2l6ZToyLjI1cmVtO2xpbmUtaGVpZ2h0OjEuMzY4NDJ9fS51LWhlYWRpbmctMntmb250LWZhbWlseTpNb250c2VycmF0LHNhbnMtc2VyaWY7Zm9udC1zaXplOjE2cHg7Zm9udC1zaXplOjFyZW07Zm9udC13ZWlnaHQ6ODAwO2xpbmUtaGVpZ2h0OjEuMTg3NX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LnUtaGVhZGluZy0ye2ZvbnQtc2l6ZToxLjEyNXJlbTtsaW5lLWhlaWdodDoxLjIyMjIyfX0udS1ib2R5LWNvcHl7Zm9udC1mYW1pbHk6TW9udHNlcnJhdCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNnB4O2ZvbnQtc2l6ZToxcmVtO2ZvbnQtd2VpZ2h0OjQwMDtsaW5lLWhlaWdodDoxLjE4NzV9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LWJvZHktY29weXtmb250LXNpemU6MS4xMjVyZW07bGluZS1oZWlnaHQ6MS4zMzMzM319LnUtc21hbGwtY29weXtmb250LWZhbWlseTpNb250c2VycmF0LHNhbnMtc2VyaWY7Zm9udC1zaXplOjE0cHg7Zm9udC1zaXplOi44NzVyZW07Zm9udC13ZWlnaHQ6NDAwO2xpbmUtaGVpZ2h0OjEuMjE0Mjl9QG1lZGlhIChtaW4td2lkdGg6OTAwcHgpey51LXNtYWxsLWNvcHl7Zm9udC1zaXplOjFyZW07bGluZS1oZWlnaHQ6MS4zNzV9fS51LXBlcmNlbnRhZ2V7Zm9udC1mYW1pbHk6TW9udHNlcnJhdCxzYW5zLXNlcmlmO2ZvbnQtd2VpZ2h0OjgwMDtmb250LXNpemU6MzZweDtmb250LXNpemU6Mi4yNXJlbTtsaW5lLWhlaWdodDoxLjM4MDk1fUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsudS1wZXJjZW50YWdle2ZvbnQtc2l6ZTo0cmVtO2xpbmUtaGVpZ2h0OjEuMzQzNzV9fS51LWJ1dHRvbi10ZXh0e2ZvbnQtZmFtaWx5Ok1vbnRzZXJyYXQsc2Fucy1zZXJpZjtmb250LXNpemU6MTJweDtmb250LXNpemU6Ljc1cmVtO2ZvbnQtd2VpZ2h0OjcwMDtsZXR0ZXItc3BhY2luZzouMDgzMzNlbTtsaW5lLWhlaWdodDoxLjE2NjY3O3RleHQtdHJhbnNmb3JtOnVwcGVyY2FzZX1AbWVkaWEgKG1pbi13aWR0aDo5MDBweCl7LnUtYnV0dG9uLXRleHR7Zm9udC1zaXplOi44NzVyZW07bGluZS1oZWlnaHQ6MS4yMTQyOX19LnUtbGFiZWx7Zm9udC1mYW1pbHk6TW9udHNlcnJhdCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxMnB4O2ZvbnQtc2l6ZTouNzVyZW07Zm9udC13ZWlnaHQ6NzAwO2xldHRlci1zcGFjaW5nOi4wODMzM2VtO2xpbmUtaGVpZ2h0OjEuMTY2Njc7dGV4dC10cmFuc2Zvcm06dXBwZXJjYXNlfUBtZWRpYSAobWluLXdpZHRoOjkwMHB4KXsudS1sYWJlbHtmb250LXNpemU6Ljg3NXJlbTtsaW5lLWhlaWdodDoxLjIxNDI5fX0udS1hbGlnbi1sZWZ0LnUtYWxpZ24tbGVmdHt0ZXh0LWFsaWduOmxlZnR9LnUtYWxpZ24tY2VudGVyLnUtYWxpZ24tY2VudGVye3RleHQtYWxpZ246Y2VudGVyfS51LWFsaWduLXJpZ2h0LnUtYWxpZ24tcmlnaHR7dGV4dC1hbGlnbjpyaWdodH0udS11cHBlcmNhc2UudS11cHBlcmNhc2V7dGV4dC10cmFuc2Zvcm06dXBwZXJjYXNlfS51LWxvd2VyY2FzZS51LWxvd2VyY2FzZXt0ZXh0LXRyYW5zZm9ybTpsb3dlcmNhc2V9LnUtbm8tY2FzZS51LW5vLWNhc2V7dGV4dC10cmFuc2Zvcm06bm9uZX0udS11aS1ib2R5e3BhZGRpbmctdG9wOjYwcHg7dHJhbnNpdGlvbjp0cmFuc2Zvcm0gLjVzIGN1YmljLWJlemllciguNSwwLC41LDEpfUBtZWRpYSAobWluLXdpZHRoOjE0MDBweCl7LnUtdWktYm9keXtwYWRkaW5nLWxlZnQ6MzAwcHh9fS51aS1ndWlkZS1tZW51LWFjdGl2ZSAudS11aS1ib2R5e3RyYW5zZm9ybTp0cmFuc2xhdGVYKDMwMHB4KX1AbWVkaWEgKG1pbi13aWR0aDoxNDAwcHgpey51aS1ndWlkZS1tZW51LWFjdGl2ZSAudS11aS1ib2R5e3RyYW5zZm9ybTpub25lIWltcG9ydGFudH19LnUtdWktaGVhZGVye2JhY2tncm91bmQ6I2ZmZjtjb2xvcjojZmZmO3Bvc2l0aW9uOmZpeGVkO2xlZnQ6MDt0b3A6MDt6LWluZGV4OjN9LnUtdWktaGVhZGVyLC51LXVpLWhlYWRlcl9fYmFubmVyey1tcy1mbGV4LWFsaWduOmNlbnRlcjthbGlnbi1pdGVtczpjZW50ZXI7bWluLWhlaWdodDo2MHB4O2Rpc3BsYXk6LW1zLWZsZXhib3g7ZGlzcGxheTpmbGV4O3dpZHRoOjEwMCV9LnUtdWktaGVhZGVyX19iYW5uZXJ7YmFja2dyb3VuZC1jb2xvcjojMDAwMDAwO2JhY2tncm91bmQtY29sb3I6cmdiYSgwLDAsMCwuOCk7cGFkZGluZzoyMHB4O3RyYW5zaXRpb246YWxsIC41cyBjdWJpYy1iZXppZXIoLjUsMCwuNSwxKX1AbWVkaWEgKG1pbi13aWR0aDoxNDAwcHgpey51LXVpLWhlYWRlcl9fYmFubmVye3BhZGRpbmctbGVmdDo1MHB4O3dpZHRoOmNhbGMoMTAwJSAtIDMwMHB4KX19LnVpLWd1aWRlLW1lbnUtYWN0aXZlIC51LXVpLWhlYWRlcl9fYmFubmVye3RyYW5zZm9ybTp0cmFuc2xhdGVYKDMwMHB4KX1AbWVkaWEgKG1pbi13aWR0aDoxNDAwcHgpey51aS1ndWlkZS1tZW51LWFjdGl2ZSAudS11aS1oZWFkZXJfX2Jhbm5lcnt0cmFuc2Zvcm06bm9uZSFpbXBvcnRhbnR9fS51LXVpLWhlYWRlcl9fYmFubmVyIGgxe2JvcmRlcjpub25lO2NvbG9yOiNmZmY7Zm9udC1zaXplOjE2cHg7Zm9udC1zaXplOjFyZW07Zm9udC13ZWlnaHQ6NDAwO2xldHRlci1zcGFjaW5nOi4wMmVtO2xpbmUtaGVpZ2h0OjEuMzttYXJnaW46MH1AbWVkaWEgKG1pbi13aWR0aDoxNDAwcHgpey51LXVpLWhlYWRlcl9fYmFubmVyIGgxe2ZvbnQtc2l6ZToxLjEyNXJlbX19LnUtdWktaGVhZGVyIC51LXVpLWhlYWRlci1sb2dvey1tcy1mbGV4LWFsaWduOmNlbnRlcjthbGlnbi1pdGVtczpjZW50ZXI7YmFja2dyb3VuZC1jb2xvcjojZmZmO2JvcmRlci1ib3R0b206MXB4IHNvbGlkIHJnYmEoMCwwLDAsLjE1KTtkaXNwbGF5Oi1tcy1mbGV4Ym94O2Rpc3BsYXk6ZmxleDtsZWZ0OjA7bWluLWhlaWdodDo2MHB4O3BhZGRpbmc6MjBweDtwb3NpdGlvbjpmaXhlZDt0b3A6MDt0cmFuc2Zvcm06dHJhbnNsYXRlWCgtMTAwJSk7d2lkdGg6MzAwcHg7ei1pbmRleDoyfUBtZWRpYSAobWluLXdpZHRoOjE0MDBweCl7LnUtdWktaGVhZGVyIC51LXVpLWhlYWRlci1sb2dve3Bvc2l0aW9uOnJlbGF0aXZlO2JhY2tncm91bmQ6I2ZmZjt0cmFuc2Zvcm06bm9uZTt3aWR0aDozMDBweH19LnVpLWd1aWRlLW1lbnUtYWN0aXZlIC51LXVpLWhlYWRlciAudS11aS1oZWFkZXItbG9nb3t0cmFuc2Zvcm06bm9uZX0udS11aS1oZWFkZXIgLnUtdWktaGVhZGVyLWxvZ28gc3Zne2ZpbGw6IzIwMjAyMDtoZWlnaHQ6MjBweDt3aWR0aDo3MHB4fS51LXVpLW1lbnUtYnRue2Rpc3BsYXk6YmxvY2s7aGVpZ2h0OjE2cHg7cG9zaXRpb246cmVsYXRpdmU7d2lkdGg6MjVweDttYXJnaW4tcmlnaHQ6NDBweH1AbWVkaWEgKG1pbi13aWR0aDoxNDAwcHgpey51LXVpLW1lbnUtYnRue2Rpc3BsYXk6bm9uZX19LnUtdWktbWVudS1idG46Zm9jdXN7b3V0bGluZTpub25lfS51LXVpLW1lbnUtYnRuX19pY29ue2JhY2tncm91bmQtY29sb3I6I2ZmZjtkaXNwbGF5OmJsb2NrO2hlaWdodDoycHg7d2lkdGg6MTAwJX0udS11aS1tZW51LWJ0bl9faWNvbjphZnRlciwudS11aS1tZW51LWJ0bl9faWNvbjpiZWZvcmV7YmFja2dyb3VuZC1jb2xvcjojZmZmO2NvbnRlbnQ6XCJcIjtoZWlnaHQ6MnB4O2xlZnQ6MDtwb3NpdGlvbjphYnNvbHV0ZTt3aWR0aDoxMDAlfS51LXVpLW1lbnUtYnRuX19pY29uOmJlZm9yZXt0b3A6MH0udS11aS1tZW51LWJ0bl9faWNvbjphZnRlcntib3R0b206MH0udS11aS1zaWRlYmFye2JhY2tncm91bmQ6I2ZmZjtib3JkZXItcmlnaHQ6MXB4IHNvbGlkIHJnYmEoMCwwLDAsLjE1KTtmb250LXNpemU6MTNweDtmb250LXNpemU6LjgxMjVyZW07Zm9udC13ZWlnaHQ6NjAwO2hlaWdodDoxMDAlO2xlZnQ6MDtwYWRkaW5nLWJvdHRvbToxMDBweDtwYWRkaW5nLXRvcDo2MHB4O3Bvc2l0aW9uOmZpeGVkO3RvcDowO3RyYW5zZm9ybTp0cmFuc2xhdGVYKC0xMDAlKTt0cmFuc2l0aW9uOnRyYW5zZm9ybSAuNXMgY3ViaWMtYmV6aWVyKC41LDAsLjUsMSk7d2lkdGg6MzAwcHg7ei1pbmRleDoxfUBtZWRpYSAobWluLXdpZHRoOjE0MDBweCl7LnUtdWktc2lkZWJhcnt0cmFuc2Zvcm06bm9uZX19LnVpLWd1aWRlLW1lbnUtYWN0aXZlIC51LXVpLXNpZGViYXJ7dHJhbnNmb3JtOm5vbmV9LnUtdWktc2lkZWJhciBsaXtwYWRkaW5nOjAhaW1wb3J0YW50O21hcmdpbjowIWltcG9ydGFudH0udS11aS1zaWRlYmFyIGxpOmJlZm9yZXtkaXNwbGF5Om5vbmUhaW1wb3J0YW50fS51LXVpLXNpZGViYXIgbGkuaXMtaW5kZW50ZWQgYXtjb2xvcjojMDAwMDAwO2NvbG9yOnJnYmEoMCwwLDAsLjcpO3BhZGRpbmctbGVmdDo0MHB4O2ZvbnQtd2VpZ2h0OjQwMDtwYWRkaW5nLXRvcDo1cHg7cGFkZGluZy1ib3R0b206NXB4fS51LXVpLXNpZGViYXIgYXtib3JkZXI6bm9uZTtjb2xvcjojMDAwMDAwO2NvbG9yOnJnYmEoMCwwLDAsLjgpO2Rpc3BsYXk6YmxvY2s7cGFkZGluZzo1cHggMjBweDtwb3NpdGlvbjpyZWxhdGl2ZX0udS11aS1zaWRlYmFyIGE6Zm9jdXN7b3V0bGluZTpub25lfS51LXVpLXNpZGViYXIgYTphZnRlcntiYWNrZ3JvdW5kLWNvbG9yOiMwMDAwMDA7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDAsMCwwLC4yNSk7Y29udGVudDpcIlwiO2hlaWdodDoxMDAlO2xlZnQ6MDtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDt0cmFuc2l0aW9uOndpZHRoIC4zcyBjdWJpYy1iZXppZXIoLjUsMCwuNSwxKTt3aWR0aDowfS51LXVpLXNpZGViYXIgYTpob3ZlcjphZnRlcnt3aWR0aDo1cHh9LnUtdWktc2lkZWJhcl9faW5uZXJ7aGVpZ2h0OmNhbGMoMTAwdmggLSA2MHB4KTtwYWRkaW5nOjEwcHggMCAwO292ZXJmbG93OmF1dG99LnUtdWktc2lkZWJhcl9faW5uZXIgdWx7bWluLWhlaWdodDpjYWxjKDEwMHZoIC0gMTcwcHgpfS51LXVpLXNpZGViYXJfX2Zvb3RlcntiYWNrZ3JvdW5kOiNmZmY7Ym9yZGVyLXRvcDoxcHggc29saWQgcmdiYSgwLDAsMCwuMTUpO2NvbG9yOiMwMDAwMDA7Y29sb3I6cmdiYSgwLDAsMCwuNSk7Y3Vyc29yOnBvaW50ZXI7Zm9udC1zaXplOjEwcHg7Zm9udC1zaXplOi42MjVyZW07Zm9udC13ZWlnaHQ6NDAwO2xldHRlci1zcGFjaW5nOi4wMjVlbTtsaW5lLWhlaWdodDoxLjM7bWFyZ2luLXRvcDozMHB4O3BhZGRpbmc6MjBweDt3aWR0aDoxMDAlO3otaW5kZXg6M30udS11aS1zaWRlYmFyX19mb290ZXIgcHttYXJnaW46MH0udS11aS1oZWFkaW5nLWxhcmdlLC51LXVpLWhlYWRpbmctbWVkaXVtLC51LXVpLWhlYWRpbmctc21hbGx7Ym9yZGVyLWJvdHRvbToxcHggc29saWQgdGludCgjMDAwLDc1JSk7Y29sb3I6dGludCgjMDAwLDUwJSk7Zm9udC13ZWlnaHQ6NDAwO2xpbmUtaGVpZ2h0OjE7bWFyZ2luLWJvdHRvbTo1MHB4O21hcmdpbi10b3A6MH0udS11aS1oZWFkaW5nLWxhcmdle2JvcmRlcjpub25lO2NvbG9yOiNmZmY7Zm9udC1zaXplOjQycHg7Zm9udC1zaXplOjIuNjI1cmVtO2ZvbnQtd2VpZ2h0OjYwMDtsaW5lLWhlaWdodDoxLjM7bWFyZ2luLWJvdHRvbTowfS51LXVpLWhlYWRpbmctbWVkaXVte2ZvbnQtc2l6ZTozMHB4O2ZvbnQtc2l6ZToxLjg3NXJlbTtwYWRkaW5nLWJvdHRvbToxMHB4fS51LXVpLWhlYWRpbmctc21hbGx7Zm9udC1zaXplOjIxcHg7Zm9udC1zaXplOjEuMzEyNXJlbTtsaW5lLWhlaWdodDoxO3BhZGRpbmctYm90dG9tOjEwcHg7bWFyZ2luOjMwcHggMH0udS11aS1jb2xvcntib3JkZXItcmFkaXVzOjNweDtib3gtc2hhZG93OjAgMXB4IDNweCByZ2JhKDAsMCwwLC4xMiksMCAxcHggMnB4IHJnYmEoMCwwLDAsLjI0KTtkaXNwbGF5OmlubGluZS1ibG9jaztmb250LXNpemU6MTRweDtmb250LXNpemU6Ljg3NXJlbTtsaW5lLWhlaWdodDoxLjM7bWFyZ2luOjAgNXB4IDIwcHg7b3ZlcmZsb3c6aGlkZGVuO3BhZGRpbmctdG9wOjEyMHB4O3dpZHRoOjIwJX0udS11aS1jb2xvcjpmaXJzdC1vZi10eXBle21hcmdpbi1sZWZ0OjB9LnUtdWktY29sb3I+ZGl2e2JhY2tncm91bmQ6I2ZmZjtwYWRkaW5nOjEwcHh9LnUtdWktY29sb3IgaDR7Zm9udC1zaXplOjE0cHg7Zm9udC1zaXplOi44NzVyZW07Zm9udC13ZWlnaHQ6NDAwO21hcmdpbjowfS51LXVpLXNlY3Rpb257cGFkZGluZzo1MHB4IDB9LnUtdWktc2VjdGlvbi1tZWRpdW17YmFja2dyb3VuZDojZWVlfS51LXVpLXNlY3Rpb24tbWVkaXVtIFtjbGFzc149dWktaGVhZGluZ117Y29sb3I6dGludCgjMDAwLDM1JSk7Ym9yZGVyLWNvbG9yOnRpbnQoIzAwMCwzNSUpfS51LXVpLXNlY3Rpb24tZGFya3tiYWNrZ3JvdW5kOiM2NjZ9LnUtdWktc2VjdGlvbi1kYXJrIFtjbGFzc149dWktaGVhZGluZ117Y29sb3I6I2ZmZjtib3JkZXItY29sb3I6I2ZmZn0udS11aS1iZy13cmFwe2Rpc3BsYXk6aW5saW5lLWJsb2NrO3BhZGRpbmc6MTVweH0udS11aS1jb2RlLXdyYXAsLnUtdWktaGVhZGluZy1sYXJnZSBjb2RlLC51LXVpLWhlYWRpbmctbWVkaXVtIGNvZGUsLnUtdWktaGVhZGluZy1zbWFsbCBjb2Rle2JhY2tncm91bmQtY29sb3I6IzY2Njtjb2xvcjojZmZmO2Rpc3BsYXk6aW5saW5lLWJsb2NrO2ZvbnQtZmFtaWx5Om1vbm9zcGFjZTtmb250LXNpemU6MTRweDtmb250LXNpemU6Ljg3NXJlbTtmb250LXN0eWxlOm5vcm1hbDtmb250LXdlaWdodDo0MDA7bGluZS1oZWlnaHQ6MTttYXJnaW4tbGVmdDoyMHB4O3BhZGRpbmc6MTBweCAxNXB4O3RleHQtdHJhbnNmb3JtOm5vbmU7dmVydGljYWwtYWxpZ246bWlkZGxlfS51LXVpLW5vdGV7YmFja2dyb3VuZC1jb2xvcjojNzU0YWNjO2NvbG9yOiNmZmY7ZGlzcGxheTpibG9jazttYXJnaW46MzBweCAwO3BhZGRpbmc6MjVweH0udS11aS1ub3RlOmJlZm9yZXtjb250ZW50OlwiREVWRUxPUEVSIE5PVEUqXCI7ZGlzcGxheTpibG9jaztmb250LXNpemU6MTRweDtmb250LXNpemU6Ljg3NXJlbTtmb250LXdlaWdodDo3MDA7bWFyZ2luLWJvdHRvbToxMHB4O3RleHQtZGVjb3JhdGlvbjp1bmRlcmxpbmV9LnUtdWktbm90ZSBhe2NvbG9yOiNmZmY7dGV4dC1kZWNvcmF0aW9uOnVuZGVybGluZX0udS11aS1oZWFkaW5nLWxhcmdlIC51LXVpLW5vdGUgY29kZSwudS11aS1oZWFkaW5nLW1lZGl1bSAudS11aS1ub3RlIGNvZGUsLnUtdWktaGVhZGluZy1zbWFsbCAudS11aS1ub3RlIGNvZGUsLnUtdWktbm90ZSAudS11aS1jb2RlLXdyYXAsLnUtdWktbm90ZSAudS11aS1oZWFkaW5nLWxhcmdlIGNvZGUsLnUtdWktbm90ZSAudS11aS1oZWFkaW5nLW1lZGl1bSBjb2RlLC51LXVpLW5vdGUgLnUtdWktaGVhZGluZy1zbWFsbCBjb2Rle2JhY2tncm91bmQtY29sb3I6I2ZmZjtjb2xvcjojNzU0YWNjO21hcmdpbi1sZWZ0OjEwcHg7bWFyZ2luLXJpZ2h0OjEwcHh9LnUtdWktZ3JpZC1jb2x7YmFja2dyb3VuZC1jb2xvcjojMDAwMDAwO2JhY2tncm91bmQtY29sb3I6cmdiYSgwLDAsMCwuMTUpO3BhZGRpbmc6MTBweDt3aWR0aDoxMDAlfS5zLWNtcy1jb250ZW50e3pvb206MX0ucy1jbXMtY29udGVudDphZnRlciwucy1jbXMtY29udGVudDpiZWZvcmV7Y29udGVudDpcIlwiO2Rpc3BsYXk6dGFibGV9LnMtY21zLWNvbnRlbnQ6YWZ0ZXJ7Y2xlYXI6Ym90aH0ucy1jbXMtY29udGVudCBhe2JvcmRlci1ib3R0b206MXB4IHNvbGlkO2NvbG9yOiM1NDcwZTA7dGV4dC1kZWNvcmF0aW9uOm5vbmV9LnMtY21zLWNvbnRlbnQgYTpob3Zlcntjb2xvcjojMzczODNjO2JvcmRlci1ib3R0b20tY29sb3I6dHJhbnNwYXJlbnR9LnMtY21zLWNvbnRlbnQgYTphY3RpdmUsLnMtY21zLWNvbnRlbnQgYTp2aXNpdGVke2NvbG9yOiMzNzM4M2M7Ym9yZGVyLWJvdHRvbToxcHggc29saWR9LnMtY21zLWNvbnRlbnQgZmlndXJle21hcmdpbi1ib3R0b206MzBweDttYXJnaW4tYm90dG9tOjEuODc1cmVtfS5zLWNtcy1jb250ZW50IGZpZ2NhcHRpb257YmFja2dyb3VuZDojY2NjO3BhZGRpbmc6MTVweCAyMHB4O3BhZGRpbmc6LjkzNzVyZW0gMS4yNXJlbX0ucy1jbXMtY29udGVudCBhe3dvcmQtYnJlYWs6YnJlYWstd29yZH0ucy1jbXMtY29udGVudCBwe21hcmdpbi1ib3R0b206MzBweDttYXJnaW4tYm90dG9tOjEuODc1cmVtO21hcmdpbi10b3A6MH0ucy1jbXMtY29udGVudCBwOmxhc3Qtb2YtdHlwZTpsYXN0LWNoaWxke21hcmdpbi1ib3R0b206MH0ucy1jbXMtY29udGVudCB1bHtsaXN0LXN0eWxlLXR5cGU6bm9uZTttYXJnaW4tYm90dG9tOjMwcHg7bWFyZ2luLWJvdHRvbToxLjg3NXJlbTtwYWRkaW5nOjA7cG9zaXRpb246cmVsYXRpdmU7b3ZlcmZsb3c6aGlkZGVufS5zLWNtcy1jb250ZW50IHVsIGxpe21hcmdpbi1ib3R0b206MTBweDttYXJnaW4tYm90dG9tOi42MjVyZW07cGFkZGluZy1sZWZ0OjMwcHg7cGFkZGluZy1sZWZ0OjEuODc1cmVtO3Bvc2l0aW9uOnJlbGF0aXZlfS5zLWNtcy1jb250ZW50IHVsIGxpOmJlZm9yZXtjb2xvcjojMDAwO2Rpc3BsYXk6aW5saW5lLWJsb2NrO2xlZnQ6MDtsaW5lLWhlaWdodDoxO3Bvc2l0aW9uOmFic29sdXRlO3RvcDowO3ZlcnRpY2FsLWFsaWduOm1pZGRsZTtjb250ZW50OlwiLlwiO2ZvbnQtc2l6ZTozNXB4O2ZvbnQtc2l6ZToyLjE4NzVyZW07bGluZS1oZWlnaHQ6MTBweDt0b3A6LS4wN2VtfS5zLWNtcy1jb250ZW50IG9se2xpc3Qtc3R5bGUtdHlwZTpub25lO21hcmdpbi1ib3R0b206MzBweDttYXJnaW4tYm90dG9tOjEuODc1cmVtO3BhZGRpbmc6MDtwb3NpdGlvbjpyZWxhdGl2ZTtvdmVyZmxvdzpoaWRkZW47Y291bnRlci1yZXNldDphfS5zLWNtcy1jb250ZW50IG9sIGxpe21hcmdpbi1ib3R0b206MTBweDttYXJnaW4tYm90dG9tOi42MjVyZW07cGFkZGluZy1sZWZ0OjMwcHg7cGFkZGluZy1sZWZ0OjEuODc1cmVtO3Bvc2l0aW9uOnJlbGF0aXZlfS5zLWNtcy1jb250ZW50IG9sIGxpOmJlZm9yZXtjb2xvcjojMDAwO2Rpc3BsYXk6aW5saW5lLWJsb2NrO2xpbmUtaGVpZ2h0OjE7cG9zaXRpb246YWJzb2x1dGU7dG9wOjA7dmVydGljYWwtYWxpZ246bWlkZGxlO2NvbnRlbnQ6Y291bnRlcihhLGRlY2ltYWwpIFwiLlwiO2NvdW50ZXItaW5jcmVtZW50OmE7Zm9udC13ZWlnaHQ6NjAwO2xlZnQ6MDt0b3A6LjI3NWVtfS5zLWNtcy1jb250ZW50IG9sIG9sIGxpOmJlZm9yZXtjb250ZW50OmNvdW50ZXIoYSl9LnMtaGVhbHRoY2hlY2sgW2NsYXNzXXtvdXRsaW5lOjVweCBzb2xpZCAjZDNkM2QzfS5zLWhlYWx0aGNoZWNrIFtjbGFzcyo9X19de291dGxpbmU6NXB4IHNvbGlkIGdyZXl9LnMtaGVhbHRoY2hlY2sgW2NsYXNzKj1cIi0tXCJde291dGxpbmU6NXB4IHNvbGlkICNhOWE5YTl9LnMtaGVhbHRoY2hlY2sgW2NsYXNzKj1cIiBvLVwiXSwucy1oZWFsdGhjaGVjayBbY2xhc3NePW8tXXtvdXRsaW5lOjVweCBzb2xpZCBvcmFuZ2V9LnMtaGVhbHRoY2hlY2sgW2NsYXNzKj1cIiBjLVwiXSwucy1oZWFsdGhjaGVjayBbY2xhc3NePWMtXXtvdXRsaW5lOjVweCBzb2xpZCBjeWFufS5zLWhlYWx0aGNoZWNrIFtjbGFzcyo9XCJAXCJde291dGxpbmU6NXB4IHNvbGlkICNiYzhmOGZ9LnMtaGVhbHRoY2hlY2sgW2NsYXNzXj1fXXtvdXRsaW5lOjVweCBzb2xpZCByZWR9Il0sInNvdXJjZVJvb3QiOiIifQ==*/

</style>