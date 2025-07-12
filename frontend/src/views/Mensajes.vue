<template>
    <section class="mensajes">
        <h2>Mis Mensajes</h2>

        <div v-if="mensajes.length === 0" class="empty-state">
            <p>No tienes mensajes nuevos.</p>
        </div>

        <ul v-else class="lista-mensajes">
            <li v-for="mensaje in mensajes" :key="mensaje.id" class="mensaje-item">
                <strong>
                    {{ mensaje.emisor_username === userStore.usuario.username ? 'Yo' : mensaje.emisor_username }}
                    → {{ mensaje.receptor_username }}
                </strong>

                <p><em>Artículo:</em> {{ mensaje.articulo_titulo }}</p>
                <p>{{ mensaje.contenido }}</p>
                <small>{{ new Date(mensaje.fecha_envio).toLocaleString() }}</small>
            </li>
        </ul>
    </section>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
    name: 'MisMensajes',
    data() {
        return {
            mensajes: [],
            userStore: useUserStore(),
        };
    },
    async mounted() {
        try {
            const token = this.userStore.token;

            // Esperar hasta que el usuario esté cargado (máximo 3 segundos)
            let espera = 0;
            while ((!this.userStore.usuario || !this.userStore.usuario.id) && espera < 3000) {
                await new Promise(resolve => setTimeout(resolve, 100));
                espera += 100;
            }

            if (!this.userStore.usuario || !this.userStore.usuario.id) {
                console.warn('El usuario no está disponible en userStore después de esperar.');
                return;
            }

            const userId = this.userStore.usuario.id;

            const response = await axios.get('http://127.0.0.1:8000/api/mensajes/', {
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            });

            console.log('Mensajes obtenidos:', response.data);

            const mensajesFiltrados = response.data.filter(
                (m) => m.receptor === userId || m.emisor === userId
            );

            this.mensajes = mensajesFiltrados;

        } catch (error) {
            console.error('Error al cargar los mensajes:', error);
        }
    }
};
</script>

<style scoped>
.mensajes {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background: #f0fff0;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.mensajes h2 {
    color: #006400;
    text-align: center;
    margin-bottom: 1.5rem;
}

.lista-mensajes {
    list-style: none;
    padding: 0;
}

.mensaje-item {
    background: white;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 6px rgba(0, 100, 0, 0.1);
    transition: background-color 0.2s ease;
}

.mensaje-item:hover {
    background-color: #e6ffe6;
}

.mensaje-item strong {
    display: block;
    color: #004d00;
    margin-bottom: 0.3rem;
}

.mensaje-item p {
    margin: 0 0 0.5rem 0;
}

.mensaje-item small {
    color: #666;
    font-size: 0.85rem;
}

.empty-state {
    text-align: center;
    font-style: italic;
    color: #666;
    padding: 2rem;
}
</style>
