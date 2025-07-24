<template>
    <section class="tienda">
        <h2 class="titulo">Tienda</h2>

        <!-- Botón para publicar artículo -->
        <div class="publicar-articulo">
            <button @click="irAPublicarArticulo" class="btn-publicar">
                📤 Publicar artículo
            </button>
        </div>

        <!-- Filtros -->
        <div class="filtros">
            <div class="filtro">
                <label for="categoria">Categoría:</label>
                <select id="categoria" v-model="categoriaSeleccionada">
                    <option disabled value="" style="color: gray;">-- Seleccione una categoría --</option>
                    <option v-for="categoria in categorias" :key="categoria.id" :value="categoria.id" >{{ categoria.nombre }}</option>
                </select>
            </div>

            <!-- CONDICIÓN -->
            <div class="filtro">
                <label for="condicion">Condición:</label>
                <select id="condicion" v-model="condicionSeleccionada">
                    <option disabled value="" style="color: gray;">-- Seleccione la condición --</option>
                    <option v-for="cond in condiciones" :key="cond.id" :value="cond.id">
                    {{ cond.descripcion }}
                    </option>
                </select>
            </div>

            <!-- ESTADO -->
            <div class="filtro">
                <label for="estado">Estado:</label>
                <select id="estado" v-model="estadoSeleccionado">
                    <option disabled value="" style="color: gray;">-- Seleccione el estado --</option>
                    <option v-for="est in estados" :key="est.id" :value="est.id">
                    {{ est.descripcion }}
                    </option>
                </select>
            </div>
        </div>

        <!-- Botón limpiar filtros -->
        <div v-if="hayFiltrosActivos" class="limpiar-filtros">
            <button @click="limpiarFiltros">Limpiar filtros</button>
        </div>

        <!-- Productos filtrados -->
        <div v-if="productosFiltrados.length" class="productos">
            <h3>Resultados:</h3>
            <div class="grid">
                <div class="producto" v-for="producto in articulosActivos" :key="producto.id">
                    <!-- Botón círculo con + arriba derecha -->
                    <button class="btn-circulo" @click="accionDelBoton(producto)">+</button>

                    <img
                        v-if="producto.fotos.length > 0"
                        :src="producto.fotos[0].imagen"
                        alt="Imagen del artículo"
                    >
                    <img
                        v-else
                        src="https://via.placeholder.com/150"
                        alt="Imagen de ejemplo"
                    >

                    <h4>{{ producto.titulo }}</h4>
                    <p v-if="producto.vendido" class="vendido-etiqueta">VENDIDO</p>
                    <p class="precio">${{ producto.precio || 'N/A' }}</p>
                    <small>{{ producto.condicion.descripcion }} - {{ producto.estado.descripcion }}</small>
                    <div class="boton-mensaje-container">
                        <button class="btn-mensaje" @click="abrirModal(producto)">
                            📩 Enviar mensaje al vendedor
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div v-else class="no-resultados">
            <p>No hay productos que coincidan con los filtros seleccionados.</p>
        </div>

        <!-- Modal para enviar mensaje -->
        <div v-if="mostrarModal" class="modal-overlay" @click.self="cerrarModal">
            <div class="modal-content">
                <h3>Enviar mensaje a vendedor: <br><small>{{ productoSeleccionado.titulo }}</small></h3>

                <label>Mensajes rápidos:</label>
                <select v-model="mensajeSeleccionado" @change="actualizarMensaje">
                    <option disabled value="">-- Seleccione un mensaje --</option>
                    <option>Hola. ¿Sigue estando disponible?</option>
                    <option>¿Podrías darme más detalles?</option>
                    <option>¿Aceptas cambio?</option>
                    <option>Estoy interesado, ¿cómo puedo pagar?</option>
                </select>

                <label for="mensajePersonalizado" style="margin-top: 1rem;">O escriba su mensaje:</label>
                <textarea id="mensajePersonalizado" v-model="mensaje" rows="4"
                    placeholder="Escribe tu mensaje aquí..."></textarea>

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
    name: 'PaginaTienda',
    data() {
        return {
            categoriaSeleccionada: '',
            condicionSeleccionada: '',
            estadoSeleccionado: '',
            categorias: [],
            condiciones: [],   
            estados: [],       
            productos: [],
            mostrarModal: false,
            productoSeleccionado: null,
            mensajeSeleccionado: '',
            mensaje: ''
        };
    },
    computed: {
        productosFiltrados() {
            return this.productos.filter(producto =>
                (!this.categoriaSeleccionada || producto.categoria.id == this.categoriaSeleccionada) &&
                (!this.condicionSeleccionada || producto.condicion.id == this.condicionSeleccionada) &&
                (!this.estadoSeleccionado || producto.estado.id == this.estadoSeleccionado)
            );
        },
        hayFiltrosActivos() {
            return this.categoriaSeleccionada || this.condicionSeleccionada || this.estadoSeleccionado;
        },
        articulosActivos() {
            return this.productos.filter(a => a.esta_activo === true);
        }
    },
    mounted() {
        this.cargarProductos();
        this.cargarCategorias();
        this.cargarCondiciones(); 
        this.cargarEstados();     
    },
    methods: {
        async cargarProductos() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/articulos/');
                this.productos = response.data;
            } catch (error) {
                console.error('Error al cargar productos', error);
            }
        },
        async cargarCategorias() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/categorias/');
                this.categorias = response.data;
            } catch (error) {
                console.error('Error al cargar categorías', error);
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
        async cargarEstados() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/estados/');
                this.estados = response.data;
            } catch (error) {
                console.error('Error al cargar estados', error);
            }
        },
        limpiarFiltros() {
            this.categoriaSeleccionada = '';
            this.condicionSeleccionada = '';
            this.estadoSeleccionado = '';
        },
        abrirModal(producto) {
            const userStore = useUserStore();
            if (!userStore.isLoggedIn) {
                alert('Necesitás iniciar sesión para enviar mensajes.');
                return;
            }
            this.productoSeleccionado = producto;
            this.mostrarModal = true;
            this.mensajeSeleccionado = '';
            this.mensaje = '';
        },
        cerrarModal() {
            this.mostrarModal = false;
            this.productoSeleccionado = null;
        },
        actualizarMensaje() {
            if (this.mensajeSeleccionado) {
                this.mensaje = this.mensajeSeleccionado;
            }
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
                    receptor: this.productoSeleccionado.usuario.id,
                    articulo: this.productoSeleccionado.id,
                    contenido: this.mensaje
                };

                console.log('Payload:', payload);
                await axios.post('http://127.0.0.1:8000/api/mensajes/', payload, {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
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
        irAPublicarArticulo() {
            const userStore = useUserStore();
            if (!userStore.isLoggedIn) {
                alert('Necesitás iniciar sesión para publicar un artículo.');
                return;
            }
            this.$router.push('/nuevo-articulo');
        },
        accionDelBoton(producto) {
            this.$router.push({ name: 'ArticuloDetalle', params: { id: producto.id } });
        },
    }
};
</script>

<style scoped>
.tienda {
    max-width: 960px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #f9f9f9;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    text-align: center;
}

.titulo {
    font-size: 2rem;
    margin-bottom: 2rem;
    color: #006400;
}

.filtros {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1.5rem;
    margin-bottom: 1rem;
}

.filtro {
    display: flex;
    flex-direction: column;
    min-width: 200px;
}

label {
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: #333;
}

select {
    padding: 0.5rem;
    font-size: 1rem;
    border: 2px solid #006400;
    border-radius: 6px;
    background-color: #f0fff0;
    color: #333;
    transition: border-color 0.3s, background-color 0.3s;
}

select:focus {
    border-color: #228B22;
    outline: none;
    background-color: #e6ffe6;
    box-shadow: 0 0 5px rgba(0, 100, 0, 0.3);
}

/* Botón limpiar filtros */
.limpiar-filtros {
    margin-bottom: 1.5rem;
}

.limpiar-filtros button {
    background-color: #d9534f;
    color: white;
    border: none;
    padding: 0.5rem 1.2rem;
    font-size: 1rem;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.limpiar-filtros button:hover {
    background-color: #c9302c;
}

.productos {
    margin-top: 2rem;
}

.grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1.5rem;
}

.producto {
    position: relative; /* para posicionar el botón + */
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 1rem;
    width: 200px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s;
}

.producto:hover {
    transform: scale(1.03);
}

.producto img {
    width: 100%;
    height: auto;
    border-radius: 4px;
}

.precio {
    margin-top: 0.5rem;
    font-weight: bold;
    color: #006400;
}

.no-resultados {
    margin-top: 2rem;
    color: #999;
}

/* Botón mensaje */
.boton-mensaje-container {
    margin-top: 0.8rem;
    display: flex;
    justify-content: center;
}

.btn-mensaje {
    background-color: #006400;
    color: white;
    border: none;
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn-mensaje:hover {
    background-color: #004d00;
}

/* Modal estilos */
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
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
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
    transition: border-color 0.3s ease;
}

.modal-content select:focus,
.modal-content textarea:focus {
    border-color: #228B22;
    outline: none;
    box-shadow: 0 0 5px rgba(0, 100, 0, 0.3);
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
    transition: background-color 0.3s ease;
}

.modal-botones button:first-child {
    background-color: #006400;
    color: white;
}

.modal-botones button:first-child:hover {
    background-color: #004d00;
}

.modal-botones .btn-cancelar {
    background-color: #ccc;
    color: #333;
}

.modal-botones .btn-cancelar:hover {
    background-color: #aaa;
}

.publicar-articulo {
    margin-bottom: 1.5rem;
    text-align: center;
}

.btn-publicar {
    background-color: #228B22;
    color: white;
    padding: 0.5rem 1.2rem;
    border-radius: 8px;
    font-weight: bold;
    text-decoration: none;
    transition: background-color 0.3s ease;
}

.btn-publicar:hover {
    background-color: #006400;
}

.vendido-etiqueta {
  color: red;
  font-weight: bold;
  margin-top: 0.3rem;
  font-size: 0.9rem;
  text-transform: uppercase;
}

/* NUEVO: Botón círculo con + arriba derecha */
.btn-circulo {
    position: absolute;
    top: 8px;
    right: 8px;
    width: 28px;
    height: 28px;
    background-color: #228B22;
    color: white;
    border: none;
    border-radius: 50%;
    font-weight: bold;
    font-size: 20px;
    line-height: 28px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}

.btn-circulo:hover {
    background-color: #006400;
}

</style>