<template>
  <section class="mensajes">
    <h2>Mis Mensajes</h2>

    <div v-if="mensajes.length === 0" class="empty-state">
      <p>No tienes mensajes nuevos.</p>
    </div>

    <ul v-else class="lista-mensajes">
      <li v-for="mensaje in mensajes" :key="mensaje.id" class="mensaje-item">
        <div class="mensaje-principal">
          <strong>
            {{ mensaje.emisor_username === userStore.usuario.username ? 'Yo' : mensaje.emisor_username }}
            → {{ mensaje.receptor_username }}
          </strong>
          <p><em>Artículo:</em> {{ mensaje.articulo_titulo }}</p>
          <p>{{ mensaje.contenido }}</p>
          <small>{{ new Date(mensaje.fecha_envio).toLocaleString() }}</small>

          <!-- Botón para mostrar u ocultar respuestas -->
          <button
            v-if="mensaje.respuestas && mensaje.respuestas.length"
            @click="toggleRespuestas(mensaje.id)"
            class="btn-toggle-respuestas"
          >
            {{ respuestasVisibles[mensaje.id] ? '▼ Ocultar respuestas' : '▶ Mostrar respuestas' }}
          </button>

          <!-- Respuestas anidadas visibles solo si se expanden -->
          <ul
            v-if="mensaje.respuestas && mensaje.respuestas.length && respuestasVisibles[mensaje.id]"
            class="respuestas-anidadas"
          >
            <li v-for="respuesta in mensaje.respuestas" :key="respuesta.id" class="respuesta-item">
              <strong>
                {{ respuesta.emisor_username === userStore.usuario.username ? 'Yo' : respuesta.emisor_username }}
                → {{ respuesta.receptor_username }}
              </strong>
              <p>{{ respuesta.contenido }}</p>
              <small>{{ new Date(respuesta.fecha_envio).toLocaleString() }}</small>
            </li>
          </ul>

          <!-- Botones -->
          <div class="botones-mensaje">
            <button @click="mostrarCajaRespuesta(mensaje.id)">💬 Responder</button>
            <button @click="eliminarMensaje(mensaje.id)">🗑️ Eliminar</button>
          </div>

          <!-- Campo de respuesta -->
          <div v-if="mensajeMostrado === mensaje.id" class="respuesta-form">
            <textarea v-model="respuestaTexto" placeholder="Escribe tu respuesta..."></textarea>
            <button @click="enviarRespuesta(mensaje)">Enviar</button>
            <button @click="cerrarRespuesta">Cancelar</button>
          </div>
        </div>
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
      respuestaTexto: '',
      mensajeMostrado: null,
      respuestasVisibles: {}
    };
  },
  // computed: {
    // mensajesRaiz() {
      // return this.mensajes.filter(m => m.mensaje_padre === null);
    // }
  // },
  methods: {
    async cargarMensajes() {
      try {
        const token = this.userStore.token;

        // Espera al usuario
        let espera = 0;
        while ((!this.userStore.usuario || !this.userStore.usuario.id) && espera < 3000) {
          await new Promise(resolve => setTimeout(resolve, 100));
          espera += 100;
        }

        if (!this.userStore.usuario || !this.userStore.usuario.id) return;

        const userId = this.userStore.usuario.id;

        const response = await axios.get('http://127.0.0.1:8000/api/mensajes/', {
          headers: { Authorization: `Bearer ${token}` }
        });

        console.log('Mensajes obtenidos:', response.data);

        const mensajesFiltrados = response.data.filter(
          m => m.receptor === userId || m.emisor === userId
        );

        this.mensajes = mensajesFiltrados;

      } catch (error) {
        console.error('Error al cargar los mensajes:', error);
      }

    },

    mostrarCajaRespuesta(mensajeId) {
      this.mensajeMostrado = this.mensajeMostrado === mensajeId ? null : mensajeId;
      this.respuestaTexto = '';
    },

    cerrarRespuesta() {
      this.mensajeMostrado = null;
      this.respuestaTexto = '';
    },

    async enviarRespuesta(mensaje) {
      try {
        const token = this.userStore.token;

        const nuevoMensaje = {
          emisor: this.userStore.usuario.id,
          receptor: mensaje.emisor === this.userStore.usuario.id ? mensaje.receptor : mensaje.emisor,
          articulo: mensaje.articulo,
          contenido: this.respuestaTexto,
          mensaje_padre: mensaje.id
        };

        await axios.post('http://127.0.0.1:8000/api/mensajes/', nuevoMensaje, {
          headers: { Authorization: `Bearer ${token}` }
        });

        alert('Mensaje enviado correctamente.');
        this.respuestaTexto = '';
        this.mensajeMostrado = null;
        this.cargarMensajes();

      } catch (error) {
        console.error('Error al enviar respuesta:', error);
        alert('Ocurrió un error al enviar el mensaje.');
      }
    },

    async eliminarMensaje(id) {
      try {
        const token = this.userStore.token;
        const confirmado = confirm('¿Estás seguro de que deseas eliminar este mensaje?');
        if (!confirmado) return;

        await axios.delete(`http://127.0.0.1:8000/api/mensajes/${id}/`, {
          headers: { Authorization: `Bearer ${token}` }
        });

        this.mensajes = this.mensajes.filter(m => m.id !== id);

      } catch (error) {
        console.error('Error al eliminar mensaje:', error);
        alert('No se pudo eliminar el mensaje.');
      }
    },

    toggleRespuestas(mensajeId) {
        this.respuestasVisibles[mensajeId] = !this.respuestasVisibles[mensajeId];
    }

  },
  async mounted() {
    this.cargarMensajes();
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
}

.mensaje-principal {
  margin-bottom: 0.5rem;
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

.botones-mensaje {
  margin-top: 0.5rem;
  display: flex;
  gap: 1rem;
}

.botones-mensaje button {
  padding: 0.4rem 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  background-color: #006400;
  color: white;
}

.botones-mensaje button:hover {
  background-color: #004d00;
}

.respuesta-form {
  margin-top: 0.5rem;
}

.respuesta-form textarea {
  width: 100%;
  height: 60px;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  border-radius: 6px;
  border: 1px solid #ccc;
  resize: vertical;
}

.respuesta-form button {
  margin-right: 0.5rem;
  padding: 0.4rem 1rem;
  background-color: #006400;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.respuesta-form button:hover {
  background-color: #004d00;
}

.empty-state {
  text-align: center;
  font-style: italic;
  color: #666;
  padding: 2rem;
}

.respuestas-anidadas {
  margin-top: 0.5rem;
  padding-left: 1.5rem;
  border-left: 3px solid #cceccc;
}

.respuesta-item {
  background-color: #f9fff9;
  margin-top: 0.5rem;
  padding: 0.5rem;
  border-radius: 6px;
}

.btn-toggle-respuestas {
  background: none;
  border: none;
  color: #006400;
  cursor: pointer;
  font-weight: bold;
  margin-bottom: 0.5rem;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.9rem;
}

.btn-toggle-respuestas:hover {
  color: #004d00;
}

</style>
