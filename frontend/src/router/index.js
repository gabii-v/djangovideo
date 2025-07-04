import { createRouter, createWebHistory } from 'vue-router'
import Inicio from '../views/Inicio.vue'
import Tienda from '../views/Tienda.vue'
import Contacto from '../views/Contacto.vue'
import Registrarse from '../views/IniciarSesión.vue'
import RegistroUsuario from '../views/Registro.vue'
import Mensajes from '../views/Mensajes.vue'
import MisCompras from '../views/MisCompras.vue'
import Usuario from '../views/Usuario.vue'

const routes = [
    { path: '/', component: Inicio },
    { path: '/tienda', component: Tienda },
    { path: '/contacto', component: Contacto },
    { path: '/IniciarSesión', component: Registrarse },
    { path: '/registro', component: RegistroUsuario },
    { path: '/mensajes', component: Mensajes },
    { path: '/mis-compras', component: MisCompras },
    { path: '/usuario', component: Usuario },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
