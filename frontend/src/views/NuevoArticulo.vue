<template>
    <div class="nuevo-articulo">
        <h2>Cargar Nuevo Artículo</h2>

        <form @submit.prevent="guardarArticulo">
            <div class="form-group">
                <label for="titulo">Título:</label>
                <input type="text" id="titulo" v-model="form.titulo" required>
            </div>

            <div class="form-group">
                <label for="descripcion">Descripción:</label>
                <textarea id="descripcion" v-model="form.descripcion" required></textarea>
            </div>

            <!-- Campo nuevo para PRECIO -->
            <div class="form-group">
                <label for="precio">Precio:</label>
                <input type="number" step="0.01" id="precio" v-model="form.precio" required>
            </div>

            <div class="form-group">
                <label for="categoria">Categoría:</label>
                <select id="categoria" v-model="form.categoria">
                    <option disabled value="">Seleccione una categoría</option>
                    <option value="1">Tecnología</option>
                    <option value="2">Electrónica</option>
                    <option value="3">Hogar</option>
                </select>
            </div>

            <!-- Estado -->
            <div class="form-group">
                <label for="estado">Estado:</label>
                <select id="estado" v-model="form.estado">
                    <option disabled value="">Seleccione un estado</option>
                    <option v-for="est in estados" :key="est.id" :value="est.id">
                        {{ est.descripcion }}
                    </option>
                </select>
            </div>

            <!-- Condición -->
            <div class="form-group">
                <label for="condicion">Condición:</label>
                <select id="condicion" v-model="form.condicion">
                    <option disabled value="">Seleccione una condición</option>
                    <option v-for="cond in condiciones" :key="cond.id" :value="cond.id">
                        {{ cond.descripcion }}
                    </option>
                </select>
            </div>

            <!-- Nuevo campo para subir fotos -->
            <div class="form-group">
                <label for="fotos">Subir fotos:</label>
                <input type="file" id="fotos" multiple @change="manejarFotos">
            </div>

            <button type="submit">Guardar Artículo</button>
        </form>

        <div v-if="mensaje" class="mensaje">
            {{ mensaje }}
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
    name: 'NuevoArticulo',
    data() {
        return {
            form: {
                titulo: '',
                descripcion: '',
                precio: '',
                categoria: '',
                estado: '',
                condicion: '',
                fotos: []
            },
            estados: [],
            condiciones: [],
            mensaje: ''
        };
    },

    async mounted() {
    await this.cargarEstados();
    await this.cargarCondiciones();
    },

    methods: {
        manejarFotos(event) {
            this.form.fotos = Array.from(event.target.files);
        },
        async cargarEstados() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/estados/');
                this.estados = response.data;
            } catch (error) {
                console.error('Error al cargar estados', error);
            }
        },
        async cargarCondiciones() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/condiciones/');
                this.condiciones = response.data;
            } catch (error) {
                console.error('Error al cargar condiciones', error);
            }
        },
        async guardarArticulo() {
            try {
                const userStore = useUserStore();
                const token = userStore.token;

                const formData = new FormData();
                formData.append('titulo', this.form.titulo);
                formData.append('descripcion', this.form.descripcion);
                formData.append('precio', this.form.precio);
                formData.append('categoria', this.form.categoria);
                formData.append('estado', this.form.estado);
                formData.append('condicion', this.form.condicion);

                // Si usás usuario autenticado en el serializer, no hace falta enviar el ID del usuario
                this.form.fotos.forEach((foto) => {
                    formData.append(`fotos`, foto);
                });

                await axios.post('http://127.0.0.1:8000/api/articulos/', formData, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                        'Content-Type': 'multipart/form-data'
                    }
                });

                this.mensaje = 'Artículo cargado correctamente';
                this.$router.push('/tienda'); // Redirige automáticamente

            } catch (error) {
                console.error(error);
                this.mensaje = 'Error al guardar el artículo';
            }
        }
    }
};
</script>


<style scoped>
.nuevo-articulo {
    max-width: 600px;
    margin: 0 auto;
    padding: 1rem;
}

.form-group {
    margin-bottom: 1rem;
}

label {
    display: block;
    margin-bottom: 0.3rem;
    font-weight: bold;
}

input,
textarea,
select {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}

input[type="file"] {
    padding: 0.3rem;
}

button {
    padding: 0.5rem 1.5rem;
    background-color: #006400;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #004d00;
}

.mensaje {
    margin-top: 1rem;
    color: green;
    font-weight: bold;
}
</style>
