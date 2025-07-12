// src/stores/user.js
import { defineStore } from 'pinia';
import { loginUser, getUsuarioAutenticado } from '@/api/usuarios';

export const useUserStore = defineStore('user', {
    state: () => ({
        usuario: null,
        token: localStorage.getItem('token') || null,
    }),
    actions: {
        async login({ username, password }) {
            // 1) Logueo y recibo token JWT
            const data = await loginUser({ username, password });
            this.token = data.access;
            localStorage.setItem('token', this.token);

            // 2) Traigo datos completos del usuario usando el token
            const usuarioData = await getUsuarioAutenticado(this.token);
            this.usuario = usuarioData;
        },
        logout() {
            this.usuario = null;
            this.token = null;
            localStorage.removeItem('token');
        },
        async cargarUsuario() {
            // Método para cargar usuario si ya hay token guardado (al iniciar app)
            if (this.token) {
                try {
                    const usuarioData = await getUsuarioAutenticado(this.token);
                    this.usuario = usuarioData;
                } catch {
                    this.logout();
                }
            }
        }
    },
    getters: {
        isLoggedIn: (state) => !!state.usuario,
    }
});
