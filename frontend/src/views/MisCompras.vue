<template>
  <section class="compras">
    <h2>Mis publicaciones</h2>

    <div class="cuadro">
      <h3>Artículos Publicados</h3>
      <div v-if="articulosPublicados.length === 0" class="empty-state">
        <p>No has publicado artículos aún.</p>
      </div>
      <table v-else class="tabla-compras">
        <thead>
          <tr>
            <th>Título</th>
            <th>Precio</th>
            <th>Fecha</th>
            <th>Estado</th>
            <th>Vendido</th>
            <th>Acción</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="articulo in articulosPublicados" :key="articulo.id">
            <td>{{ articulo.titulo }}</td>
            <td>{{ formatearMoneda(articulo.precio) }}</td>
            <td>{{ new Date(articulo.fecha_publicacion).toLocaleDateString() }}</td>
            <td>{{ articulo.esta_activo ? 'Publicado' : 'Oculto' }}</td>
            <!-- <td>{{ estaVendido(articulo) ? 'Sí' : 'No' }}</td> -->
            <td>{{ articulo.vendido ? 'Sí' : 'No' }} <button @click="alternarVendido(articulo)" title="Marcar como vendido" class="btn-vendido">🔽</button></td>

            <td class="acciones">
              <button @click="alternarVisibilidad(articulo)">
                {{ articulo.esta_activo ? 'Ocultar' : 'Publicar' }}
              </button>
              <button @click="mostrarDetalle(articulo)">🔍 Detalle</button>
              <button @click="irAEditar(articulo)">✏️</button>
              <button @click="eliminarArticulo(articulo)">🗑️</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal Detalle -->
    <div v-if="detalleVisible" class="modal-overlay" @click.self="cerrarDetalle">
      <div class="modal-content">
        <h3>Detalle del artículo: <small>{{ articuloDetalle.titulo }}</small></h3>
        <p>{{ articuloDetalle.descripcion }}</p>
        <button @click="cerrarDetalle">Cerrar</button>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
  name: 'MisCompras',
  data() {
    return {
      compras: [],
      articulos: [],
      detalleVisible: false,
      articuloDetalle: null,
    };
  },
  computed: {
    userStore() {
      return useUserStore();
    },
    comprasVendidas() {
      return this.compras.filter(c => c.tipo === 'Venta');
    },
    articulosPublicados() {
      return this.articulos.filter(a => {
        const usuarioId = typeof a.usuario === 'object' ? a.usuario.id : a.usuario;
        return usuarioId === this.userStore.usuario.id;
      });
    }
  },
  methods: {
    formatearMoneda(valor) {
      return `$ ${valor.toLocaleString('es-AR', { minimumFractionDigits: 2 })}`;
    },
    estaVendido(articulo) {
      return this.comprasVendidas.some(c => c.producto === articulo.titulo);
    },
    async alternarVisibilidad(articulo) {
      try {
        const token = this.userStore.token;

        const updated = {
          esta_activo: !articulo.esta_activo
        };

        await axios.patch(`http://127.0.0.1:8000/api/articulos/${articulo.id}/`, updated, {
          headers: { Authorization: `Bearer ${token}` }
        });

        articulo.esta_activo = !articulo.esta_activo;
      } catch (error) {
        console.error('Error al cambiar visibilidad:', error);
      }
    },
    mostrarDetalle(articulo) {
      this.articuloDetalle = articulo;
      this.detalleVisible = true;
    },
    cerrarDetalle() {
      this.detalleVisible = false;
      this.articuloDetalle = null;
    },
    irAEditar(articulo) {
      this.$router.push(`/editar-articulo/${articulo.id}`);
    },
    async eliminarArticulo(articulo) {
      if (!confirm(`¿Estás seguro de que querés eliminar "${articulo.titulo}"?`)) return;

      try {
        const token = this.userStore.token;

        await axios.delete(`http://127.0.0.1:8000/api/articulos/${articulo.id}/`, {
          headers: { Authorization: `Bearer ${token}` }
        });

        // Eliminar de la lista local
        this.articulos = this.articulos.filter(a => a.id !== articulo.id);
        alert('Artículo eliminado con éxito.');
      } catch (error) {
        console.error('Error al eliminar artículo:', error);
        alert('Hubo un problema al eliminar el artículo.');
      }
    },
    async alternarVendido(articulo) {
        try {
            const token = this.userStore.token;

            const actualizado = { vendido: !articulo.vendido };

            await axios.patch(`http://127.0.0.1:8000/api/articulos/${articulo.id}/`, actualizado, {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            });

            articulo.vendido = !articulo.vendido; // lo actualizo localmente
        } catch (error) {
            console.error('Error al actualizar vendido:', error);
            alert('Ocurrió un error al marcar como vendido.');
        }
    }

  },
  async mounted() {
    try {
      const token = this.userStore.token;

      this.compras = [
        { id: 1, producto: 'Auriculares Bluetooth', tipo: 'Compra', fecha: '2025-05-15', precio: 1500, estado: 'Entregado' },
        { id: 2, producto: 'Camiseta Deportiva', tipo: 'Venta', fecha: '2025-05-20', precio: 800, estado: 'Entregado' }
      ];

      const response = await axios.get('http://127.0.0.1:8000/api/articulos/', {
        headers: { Authorization: `Bearer ${token}` }
      });

      this.articulos = response.data;
    } catch (error) {
      console.error('Error al cargar datos:', error);
    }
  }
};
</script>

<style scoped>
.compras {
  max-width: 900px;
  margin: 2rem auto;
  padding: 2rem;
  background: #f0fff0;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.compras h2 {
  color: #006400;
  text-align: center;
  margin-bottom: 2rem;
}

.cuadro {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.06);
  text-align: center;
}

.tabla-compras {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

.tabla-compras thead {
  background-color: #006400;
  color: white;
}

.tabla-compras th,
.tabla-compras td {
  padding: 0.75rem 1rem;
  border: 1px solid #ccc;
  text-align: center;
}

.tabla-compras tbody tr:hover {
  background-color: #e6ffe6;
}

.empty-state {
  text-align: center;
  font-style: italic;
  color: #666;
  padding: 2rem;
}

.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex; justify-content: center; align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 1.5rem 2rem;
  border-radius: 12px;
  max-width: 500px;
  width: 90%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  text-align: left;
}

.modal-content h3 {
  margin-bottom: 1rem;
  color: #006400;
}

.modal-content button {
  margin-top: 1rem;
  background-color: #006400;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
}

.modal-content button:hover {
  background-color: #004d00;
}

.acciones button {
  margin: 0 0.2rem;
  padding: 0.3rem 0.6rem;
  font-size: 0.9rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #eee;
  transition: background-color 0.2s ease;
}

.acciones button:hover {
  background-color: #ddd;
}

.btn-vendido {
  margin-left: 0.5rem;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  transition: transform 0.2s ease;
}
.btn-vendido:hover {
  transform: scale(1.2);
}

</style>
