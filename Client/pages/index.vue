<template>
  <body>


    <div id="main">
      <header>
        <h2 >choose the right feeling</h2>
      </header>

      <section>
        <div class="space">
          <input type='input' placeholder='Write your lines' class='input' v-model='line'>
        </div>
        <div class="space">
          <input type='button' value='Positive' class='btn' :style='emotion === "+" ? "background: green" : "" ' @click='emotion="+"'>
          <input type='button' value='Negative' class='btn' :style='emotion === "-" ? "background: red" : "" ' @click='emotion="-"'>
        </div>
        <div class='error' v-if='error'>
          {{ error }}
        </div>
        <div class='result' v-if='result' :style='result.includes("bonne") ? "color: green" : "color: red"'>
          {{ result }}
        </div>
        <div>
          <input type='button' value='Send' class='btn' @click='send'>
        </div>
      </section>
      <footer>

      </footer>

    </div>
  </body>

</template>

<script>
  export default {
    data() {
      return {
        line: '',
        emotion: '',
        error: '',
        result: ''
      }
    },
    watch: {
      emotion: function() {
        if (this.error) this.error = ''
        if (this.result) this.result = ''
      },
      line: function() {
        if (this.error) this.error = ''
        if (this.result) this.result = ''
      }
    },
    created() {
      //const ip = await this.$axios.$get('http://icanhazip.com')
      //console.log(ip)
    },
    methods: {
      async send() {
        this.result = ''
        if (!this.emotion) {
          this.error = 'please choose a feeling';
          return ;
        }
        else if (!this.line) {
          this.error = 'please write a line';
          return ;
        }
        this.error = ''
        try {
          let obj = {
            line: this.line,
            emotion: this.emotion
          }
          this.line = ''
          this.emotion = ''
          let response = await this.$axios.$post('http://localhost:8000/analyse', obj)
          this.result = `La serveur a predit la ${response ? 'bonne' : 'mauvaise'} emotion`
        } catch (err) {
          this.result = `Le serveur a merdé`
        }

      }
    },


  }
</script>

<style>
html, body {
  height: 100%;
  margin: 0; padding: 0;
}
body {

  display : table;
  width: 100%;
  background-color: burlywood;
}
footer{

  background: url("../image/images.jpg");
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  position:absolute;

  bottom:0;

  width:100%;

  padding-top:50px;

  height:50px;

}
.form-group{
  background: aqua;
}

section{
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%);
    text-align: center;
    background-color: #b2aeb0;
    padding: 40px;
    border-radius: 2em;
}
h2 {
  text-align: center;
  border: 3px solid green;
}
.btn {
  margin-left :10px;
  box-shadow: 5px 5px 5px black;
  padding: 10px;
  border: 0;
  border-radius: 4px;
  cursor:pointer;
}
.input {
  padding: 10px 40px 10px 40px;
  text-align: center;
  border-radius: 10px;
  border: none;
}
.space {
  margin: 30px;
}
.error {
  color: red;
  margin: 20px;
  font-weight: bold;
}
.result {
  margin: 20px;
  font-weight: bold;
}

</style>
