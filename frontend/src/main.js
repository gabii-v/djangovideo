import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import router from './router'

/*createApp(App).mount('#app')*/
/*createApp(App).use(router).mount('#app')*/


const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')

