<template>
</template>

<script>
export default {
  name: 'MyCard',
  data () {
    return {
      adding: false,
      temp_data: {
        url: 'http://',
        name: 'name',
        intro: '...'
      },
      favorites: []
    }
  },
  created() {
    axios.get('http://localhost:8000/api/links/').then(response => {
      let links = response.data.map(link => {
        return {
          key: link.id,
          url: link.url,
          name: link.name,
          intro: link.description
        }
      })
      this.favorites = links
    }).catch(erro => {
      console.log(erro);
    })
  },
  methods: {
    addNew(){
      this.adding = true
      this.temp_data = {
        url: 'http://',
        name: '',
        intro: ''
      }
    },
    postNew(){
      let payload = {
        url: this.temp_data.url,
        name: this.temp_data.name,
        description: this.temp_data.intro
      }
      axios.post('http://localhost:8000/api/links/', payload).then(response => {
        this.favorites.push({
          key: response.data.id,
          url: response.data.url,
          name: response.data.name,
          intro: response.data.description
        })
        this.adding = false
        this.favorites = links
      }).catch(erro => {
        console.log(erro);
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
