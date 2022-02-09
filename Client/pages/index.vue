<template>
  <main>
    <h2>Choisir la bonne emotion</h2>
    <div class="space">
      <input type='input' placeholder='Ecrire votre phrase' class='input' v-model='line'>
    </div>
    <div class="space">
      <input type='button' value='Positif' class='btn' :style='emotion === "+" ? "background: green" : "" ' @click='emotion="+"'>
      <input type='button' value='Negatif' class='btn' :style='emotion === "-" ? "background: red" : "" ' @click='emotion="-"'>
    </div>
    <div class='error' v-if='error'>
      {{ error }}
    </div>
    <div class='result' v-if='result' :style='result.includes("bonne") ? "color: green" : "color: red"'>
      {{ result }}
    </div>
    <div>
      <input type='button' value='Envoyer' class='btn' @click='send'>
    </div>

  </main>
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
          this.error = 'Veuillez choisir une emotion';
          return ;
        }
        else if (!this.line) {
          this.error = 'Veuillez ecrire une phrase';
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
main {
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%);
    text-align: center;
    background-color: #4f467e;
    padding: 40px;
    border-radius: 2em;
}
h2 {

}
.btn {
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
