
    let app = Vue.createApp({
        delimiters: ['[[', ']]'],
        data: function (){
            return{
                greeting: "Hello Vue 3",
                isVisible: false
            }
        },
        methods:{
            toggleBox(){
                this.isVisible = !this.isVisible;
            },
            greet(){
                console.log()
            }
        }
    })

    app.component('login-form',{
        delimiters: ['[[', ']]'],
        template: `
            <form @submit.prevent="handleSubmit">
                <h1>[[ title ]]</h1>
                <p v-for="str in inputs" :key="str">[[ str ]]</p>
                <custom-input v-for="(input, i) in inputs" :key="i" v-model="input.value" :label="input.label" :type="input.type" />
                <input type="submit">
            </form>
        `,
        components: ['custom-input'],
        data(){
            return{
                title: 'Login',
                inputs:[
                    {
                        label: 'Email',
                        value: '',
                        type: 'email'
                    },
                    {
                        label: 'Password',
                        value: '',
                        type: 'password'
                    }
                ],
                email: '',
                password: '',
                emailLabel: 'Email',
                passwdLabel: 'Password'
            }
        },
        methods:{
            handleSubmit(){
                console.log(this.inputs[0].value)
            }
        }
    })
    app.component('custom-input',{
        delimiters: ['[[', ']]'],
        template: `
            <label>
                [[label]]
                   <input :type="type" v-model="inputValue"/>
            </label>
        `,
        props: ['label', 'type', 'modelValue'],
        computed:{
          inputValue: {
              get(){
                 return this.modelValue
              },
              set(value){
                  this.$emit('update:modelValue', value)
              }
          }
        },
        //data(){
        //    return{
        //        inputValue: ''
        //    }
        //}
    })
    app.mount('#app')