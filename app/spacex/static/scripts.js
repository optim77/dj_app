let app = Vue.createApp({
    delimiters: [ '[[', ']]' ],
    methods:{
      deleteItem: function(id){
        if(confirm('Are you sure to remove this item?')){
          let data = {
            method: 'POST'
          };
          fetch('/delete/'+id +'/', data)
          .then(response => response.json())
        }
      },
      addToBasket: function(id){
        console.log(id);
        let data = {
            method: "POST",
            credentials: 'include',
            body: id,
            id: id
        }
        fetch('/add_to_basket/' + id, data)
        .then(response => response.json())
      },
      show_basket: function(){
        console.log('hover')
      }
    }
})

app.component('slide-basket', {
  template: `

  `
});

app.mount("#app")
