let contact = Vue.createApp({

    data(){
        return{

        }
    }
})
contact.component('contact-form',{
    delimiters: [ '[[', ']]' ],
    template: `
        <form @submit.prevent="save()">
        <h3>[[ title ]]</h3>
            <div class="form-group">
                <input type="text" v-model="username" required class="form-control" id="username" aria-describedby="username" placeholder="Full Name">
            </div>
            <div class="form-group">
                <input type="email" v-model="email" required class="form-control" id="mail" placeholder="Email">
            </div>
            <div class="form-check">

                <textarea name="id_message" v-model="message" required class="form-control" placeholder="Your message" id="id_message" cols="80" rows="5"></textarea>
                <br>
                <button type="submit" class="btn btn-primary">Submit</button>
            </div>





        </form>
    `,
    data(){
        return{
            title: 'Contact form',
            username: 'boyeo',
            email: 'plajerowy@gmail.com',
            message: 'message'
        }
    },
    methods:{

        save(){
            let pack = {
                username: this.username,
                email: this.email,
                message: this.message
            }
            fetch('/contact/', {
                credentials: 'include',
                method: 'POST',
                meta:{requiresAuth: false},
                headers: {'Content-Type': 'application/json; charset=UTF-8', 'Accept': 'application/json',},
                body: JSON.stringify(pack)
            })
                .then(res => console.log(res))
                .then((json) => console.log(json ))

        }

    }
})

contact.mount("#contact")