<template>
    <div class="usuario-container">
        <h2>Información del Usuario</h2>

        <!-- Foto de perfil -->
        <div class="foto-perfil">
            <img :src="usuario.foto || defaultImage" alt="Foto de perfil" />
        </div>

        <div class="datos-usuario" v-if="!editando">
            <p><strong>Nombre:</strong> {{ usuario.nombreCompleto || '-' }}</p>
            <p><strong>Email:</strong> {{ usuario.email }}</p>
            <p><strong>Teléfono:</strong> {{ usuario.telefono || '-' }}</p>
            <p><strong>Localidad:</strong> {{ usuario.localidad || '-' }}</p>
            <p><strong>Dirección:</strong> {{ usuario.direccion || '-' }}</p>
            <p><strong>Fecha de registro:</strong> {{ usuario.fechaRegistro || '-' }}</p>

            <button @click="editar">Editar perfil</button>
        </div>

        <div class="formulario-edicion" v-else>
            <div class="form-group">
                <label>Nombre completo:</label>
                <input v-model="form.nombreCompleto" type="text" />
            </div>
            <div class="form-group">
                <label>Teléfono:</label>
                <input v-model="form.telefono" type="text" />
            </div>
            <div class="form-group">
                <label>Localidad:</label>
                <input v-model="form.localidad" type="text" />
            </div>
            <div class="form-group">
                <label>Dirección:</label>
                <input v-model="form.direccion" type="text" />
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

export default {
    name: 'UsuarioView',
    data() {
        return {
            editando: false,
            form: {
                nombreCompleto: '',
                telefono: '',
                localidad: '',
                direccion: ''
            }
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
            this.form = {
                nombreCompleto: this.usuario.nombreCompleto || '',
                telefono: this.usuario.telefono || '',
                localidad: this.usuario.localidad || '',
                direccion: this.usuario.direccion || ''
            };
        },
        cancelar() {
            this.editando = false;
        },
        async guardar() {
            try {
                const response = await axios.put('http://127.0.0.1:8000/api/usuarios/me/', this.form, {
                    headers: {
                        Authorization: `Bearer ${this.token}`
                    }
                });
                alert('Perfil actualizado');
                this.editando = false;

                // Recargar usuario desde respuesta
                this.$patchUser(response.data);  // si usás un método así en store
                location.reload(); // o podés recargar la página
            } catch (error) {
                console.error('Error al guardar perfil', error);
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

.foto-perfil img {
    width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 50%;
    border: 2px solid #006400;
    margin-bottom: 1rem;
    display: inline-block;
}

.datos-usuario {
    text-align: left;
    font-size: 1.1rem;
    padding-left: 0.5rem;
}

.datos-usuario p {
    margin: 0.5rem 0;
}
</style>
