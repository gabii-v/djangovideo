<template>
  <section class="detalle-articulo">
    <!-- Botón Volver -->
    <button @click="$router.push('/tienda')" class="btn-mensaje btn-volver">⬅ Volver a la tienda</button>

    <!-- Mensajes de carga o error -->
    <div v-if="cargando">Cargando artículo...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else-if="articulo">
      <!-- Galería de fotos -->
      <div class="galeria" v-if="articulo.fotos.length">
        <button @click="fotoAnterior" class="btn-flecha">⬅</button>
        <img :src="articulo.fotos[indiceFoto].imagen" alt="Foto del artículo" class="foto-articulo" />
        <button @click="fotoSiguiente" class="btn-flecha">➡</button>
      </div>

      <!-- Detalles del artículo centrados -->
      <div class="detalle-centro">
        <h2>{{ articulo.titulo }}</h2>
        <p><strong>Descripción:</strong> {{ articulo.descripcion }}</p>
        <p><strong>Precio:</strong> ${{ articulo.precio }}</p>
        <p><strong>Categoría:</strong> {{ articulo.categoria.nombre || articulo.categoria }}</p>
        <p><strong>Estado:</strong> {{ articulo.estado.descripcion || articulo.estado }}</p>
        <p><strong>Condición:</strong> {{ articulo.condicion.descripcion || articulo.condicion }}</p>
        <p><strong>Vendedor:</strong> {{ articulo.usuario.username }}</p>

        <!-- Botón Enviar mensaje -->
        <button class="btn-mensaje" @click="abrirModal">
          💬 Enviar mensaje al vendedor
        </button>
      </div>
    </div>

    <!-- Modal para enviar mensaje -->
    <div v-if="mostrarModal" class="modal-overlay" @click.self="cerrarModal">
      <div class="modal-content">
        <h3>Enviar mensaje a vendedor:<br><small>{{ articulo.titulo }}</small></h3>

        <label>Mensajes rápidos:</label>
        <select v-model="mensajeSeleccionado" @change="actualizarMensaje">
          <option disabled value="">-- Seleccione un mensaje --</option>
          <option>Hola. ¿Sigue estando disponible?</option>
          <option>¿Podrías darme más detalles?</option>
          <option>¿Aceptas cambio?</option>
          <option>Estoy interesado, ¿cómo puedo pagar?</option>
        </select>

        <label style="margin-top: 1rem;">O escriba su mensaje:</label>
        <textarea v-model="mensaje" rows="4" placeholder="Escribe tu mensaje aquí..."></textarea>

        <div class="modal-botones">
          <button @click="enviarMensaje">Enviar</button>
          <button @click="cerrarModal" class="btn-cancelar">Cancelar</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
  name: 'ArticuloDetalle',
  data() {
    return {
      articulo: null,
      cargando: true,
      error: null,
      indiceFoto: 0,
      mostrarModal: false,
      mensajeSeleccionado: '',
      mensaje: '',
    };
  },
  mounted() {
    const id = this.$route.params.id;
    this.cargarArticulo(id);
  },
  methods: {
    async cargarArticulo(id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/articulos/${id}/`);
        this.articulo = response.data;
      } catch (err) {
        this.error = 'No se pudo cargar el artículo.';
      } finally {
        this.cargando = false;
      }
    },
    fotoAnterior() {
      if (this.indiceFoto > 0) this.indiceFoto--;
    },
    fotoSiguiente() {
      if (this.indiceFoto < this.articulo.fotos.length - 1) this.indiceFoto++;
    },
    abrirModal() {
      const userStore = useUserStore();
      if (!userStore.isLoggedIn) {
        alert('Necesitás iniciar sesión para enviar mensajes.');
        return;
      }
      this.mostrarModal = true;
      this.mensajeSeleccionado = '';
      this.mensaje = '';
    },
    cerrarModal() {
      this.mostrarModal = false;
    },
    actualizarMensaje() {
      if (this.mensajeSeleccionado) this.mensaje = this.mensajeSeleccionado;
    },
    async enviarMensaje() {
      if (!this.mensaje.trim()) {
        alert('Por favor, escriba un mensaje antes de enviar.');
        return;
      }

      try {
        const userStore = useUserStore();
        const token = userStore.token;

        const payload = {
          receptor: this.articulo.usuario.id,
          articulo: this.articulo.id,
          contenido: this.mensaje,
        };

        await axios.post('http://127.0.0.1:8000/api/mensajes/', payload, {
          headers: { Authorization: `Bearer ${token}` },
        });

        alert('Mensaje enviado con éxito.');
        this.cerrarModal();
      } catch (error) {
        console.error('Error al enviar mensaje:', error);
        if (error.response && error.response.data) {
          const errores = error.response.data;
          const mensajeError = Object.values(errores).flat()[0];
          alert(`Error: ${mensajeError}`);
        } else {
          alert('Ocurrió un error al enviar el mensaje.');
        }
      }
    },
  },
};
</script>

<style scoped>
.detalle-articulo {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1rem;
  font-family: sans-serif;
  text-align: center; /* centro todo */
}

.btn-mensaje {
  display: inline-block;
  margin-top: 1rem;
  margin-right: 1rem;
  padding: 0.5rem 1rem;
  background-color: #006400;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.btn-mensaje:hover {
  background-color: #004d00;
}

.btn-volver {
  background-color: #006400;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  margin-bottom: 1rem;
}

.galeria {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-bottom: 1rem;
}

.foto-articulo {
  max-width: 300px;
  max-height: 300px;
  border-radius: 10px;
  box-shadow: 0 0 5px rgba(0,0,0,0.3);
}

.btn-flecha {
  background-color: transparent;
  border: none;
  font-size: 2rem;
  cursor: pointer;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.modal-content {
  background: white;
  padding: 1.5rem 2rem;
  border-radius: 12px;
  max-width: 400px;
  width: 90%;
  text-align: left;
}
.modal-content h3 {
  margin-bottom: 1rem;
  color: #006400;
}
.modal-content label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.3rem;
}
.modal-content select,
.modal-content textarea {
  width: 100%;
  padding: 0.5rem;
  border: 2px solid #006400;
  border-radius: 6px;
  font-size: 1rem;
  color: #333;
  resize: vertical;
}
.modal-botones {
  margin-top: 1rem;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}
.modal-botones button {
  padding: 0.5rem 1.2rem;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
}
.modal-botones button:first-child {
  background-color: #006400;
  color: white;
}
.modal-botones .btn-cancelar {
  background-color: #ccc;
  color: #333;
}
</style>
