<template>
  <div class="usuario-container">
    <h2>Información del Usuario</h2>

    <div v-if="!editando" class="datos-usuario">
      <div class="foto-perfil">
        <img :src="usuario.foto || defaultImage" alt="Foto de perfil" />
      </div>

      <p><strong>Usuario:</strong> {{ usuario.username }}</p>
      <p><strong>Email:</strong> {{ usuario.email }}</p>
      <p><strong>Teléfono:</strong> {{ usuario.telefono || '-' }}</p>
      <p><strong>Localidad:</strong> {{ usuario.localidad || '-' }}</p>

      <button @click="editar">Editar perfil</button>
    </div>

    <div v-else class="formulario-edicion">
      <div class="form-group">
        <label>Foto de perfil:</label>
        <input type="file" @change="handleFileChange" />
        <div v-if="previewFoto" class="preview-foto">
          <img :src="previewFoto" alt="Foto previa" />
        </div>
      </div>

      <div class="form-group">
        <label>Teléfono:</label>
        <input v-model="form.telefono" type="text" />
      </div>

      <div class="form-group">
        <label>Localidad:</label>
        <input v-model="form.localidad" type="text" />
      </div>

      <button @click="guardar">Guardar cambios</button>
      <button @click="cancelar">Cancelar</button>
    </div>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/user';
import { mapState } from 'pinia';
import axios from 'axios';
import { getUsuarioAutenticado } from '@/api/usuarios';

export default {
  name: 'UsuarioView',
  data() {
    return {
      editando: false,
      form: {
        telefono: '',
        localidad: '',
      },
      archivoFoto: null,
      previewFoto: null,
    };
  },
  computed: {
    ...mapState(useUserStore, ['usuario', 'token']),
    defaultImage() {
      return 'https://via.placeholder.com/150';
    }
  },
  methods: {
    editar() {
      this.editando = true;
      this.form.telefono = this.usuario.telefono || '';
      this.form.localidad = this.usuario.localidad || '';
      this.previewFoto = this.usuario.foto || null;
      this.archivoFoto = null;
    },
    cancelar() {
      this.editando = false;
      this.previewFoto = null;
      this.archivoFoto = null;
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.archivoFoto = file;
        this.previewFoto = URL.createObjectURL(file);
      } else {
        this.archivoFoto = null;
        this.previewFoto = null;
      }
    },
    async guardar() {
      try {
        const formData = new FormData();
        formData.append('telefono', this.form.telefono);
        formData.append('localidad', this.form.localidad);

        if (this.archivoFoto) {
          formData.append('foto', this.archivoFoto);
        }

        const config = {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `Bearer ${this.token}`
          }
        };

        await axios.put('http://127.0.0.1:8000/api/usuarios/me/', formData, config);

        alert('Perfil actualizado');
        this.editando = false;

        // Recargar usuario actualizado completo desde API
        const userStore = useUserStore();
        const usuarioActualizado = await getUsuarioAutenticado(this.token);
        userStore.usuario = usuarioActualizado;

        // Actualizar preview y limpiar archivo seleccionado
        this.previewFoto = userStore.usuario.foto || null;
        this.archivoFoto = null;

      } catch (error) {
        console.error('Error al guardar perfil:', error);
        alert('No se pudo guardar el perfil');
      }
    }
  }
};
</script>

<style scoped>
.usuario-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9fff9;
  box-shadow: 0 0 10px rgba(0, 100, 0, 0.2);
  text-align: center;
  color: #006400;
}

.usuario-container h2 {
  margin-bottom: 1.5rem;
}

.foto-perfil img, .preview-foto img {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid #006400;
  margin-bottom: 1rem;
  display: inline-block;
}

.formulario-edicion {
  text-align: left;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.3rem;
}

.form-group input[type="text"],
.form-group input[type="file"] {
  width: 100%;
  padding: 0.4rem;
  font-size: 1rem;
  border: 2px solid #006400;
  border-radius: 6px;
  background-color: #f0fff0;
  color: #333;
  transition: border-color 0.3s ease;
}

.form-group input[type="text"]:focus,
.form-group input[type="file"]:focus {
  border-color: #228B22;
  outline: none;
  box-shadow: 0 0 5px rgba(0, 100, 0, 0.3);
}

button {
  background-color: #006400;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  margin-right: 0.5rem;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #004d00;
}
</style>
