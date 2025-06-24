<template>
    <section class="tienda">
        <h2 class="titulo">Tienda</h2>

        <!-- Filtros -->
        <div class="filtros">
            <div class="filtro">
                <label for="categoria">Categoría:</label>
                <select id="categoria" v-model="categoriaSeleccionada">
                    <option disabled value="" style="color: gray;">-- Seleccione una categoría --</option>
                    <option v-for="categoria in categorias" :key="categoria">{{ categoria }}</option>
                </select>
            </div>

            <div class="filtro">
                <label for="condicion">Condición:</label>
                <select id="condicion" v-model="condicionSeleccionada">
                    <option disabled value="" style="color: gray;">-- Seleccione la condición --</option>
                    <option>Nuevo</option>
                    <option>Usado</option>
                    <option>Reacondicionado</option>
                </select>
            </div>

            <div class="filtro">
                <label for="estado">Estado:</label>
                <select id="estado" v-model="estadoSeleccionado">
                    <option disabled value="" style="color: gray;">-- Seleccione el estado --</option>
                    <option>Disponible</option>
                    <option>Sin stock</option>
                    <option>Próximamente</option>
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
                <div class="producto" v-for="producto in productosFiltrados" :key="producto.nombre">
                    <img :src="producto.imagen" :alt="producto.nombre" />
                    <h4>{{ producto.nombre }}</h4>
                    <p class="precio">${{ producto.precio }}</p>
                    <small>{{ producto.condicion }} - {{ producto.estado }}</small>
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
                <h3>Enviar mensaje a vendedor: <br><small>{{ productoSeleccionado.nombre }}</small></h3>

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
export default {
    name: 'PaginaTienda',
    data() {
        return {
            categoriaSeleccionada: '',
            condicionSeleccionada: '',
            estadoSeleccionado: '',
            categorias: ['Ropa', 'Electrónica', 'Hogar', 'Deportes'],
            productos: [
                { nombre: 'Remera básica', categoria: 'Ropa', precio: 2500, condicion: 'Nuevo', estado: 'Disponible', imagen: 'https://via.placeholder.com/150' },
                { nombre: 'Zapatillas running', categoria: 'Deportes', precio: 8500, condicion: 'Usado', estado: 'Disponible', imagen: 'https://via.placeholder.com/150' },
                { nombre: 'Smartphone', categoria: 'Electrónica', precio: 120000, condicion: 'Reacondicionado', estado: 'Sin stock', imagen: 'https://via.placeholder.com/150' },
                { nombre: 'Lámpara LED', categoria: 'Hogar', precio: 4300, condicion: 'Nuevo', estado: 'Disponible', imagen: 'https://via.placeholder.com/150' },
                { nombre: 'Pantalón jeans', categoria: 'Ropa', precio: 6200, condicion: 'Usado', estado: 'Próximamente', imagen: 'https://via.placeholder.com/150' },
                { nombre: 'Auriculares bluetooth', categoria: 'Electrónica', precio: 7800, condicion: 'Nuevo', estado: 'Disponible', imagen: 'https://via.placeholder.com/150' }
            ],
            mostrarModal: false,
            productoSeleccionado: null,
            mensajeSeleccionado: '',
            mensaje: ''
        };
    },
    computed: {
        productosFiltrados() {
            return this.productos.filter(producto =>
                (!this.categoriaSeleccionada || producto.categoria === this.categoriaSeleccionada) &&
                (!this.condicionSeleccionada || producto.condicion === this.condicionSeleccionada) &&
                (!this.estadoSeleccionado || producto.estado === this.estadoSeleccionado)
            );
        },
        hayFiltrosActivos() {
            return this.categoriaSeleccionada || this.condicionSeleccionada || this.estadoSeleccionado;
        }
    },
    methods: {
        limpiarFiltros() {
            this.categoriaSeleccionada = '';
            this.condicionSeleccionada = '';
            this.estadoSeleccionado = '';
        },
        abrirModal(producto) {
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
        enviarMensaje() {
            if (!this.mensaje.trim()) {
                alert('Por favor, escriba un mensaje antes de enviar.');
                return;
            }
            alert(`Mensaje enviado para "${this.productoSeleccionado.nombre}":\n\n${this.mensaje}`);
            this.cerrarModal();
        }
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
    /* verde muy claro */
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
</style>
