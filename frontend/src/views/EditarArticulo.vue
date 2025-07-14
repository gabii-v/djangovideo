<template>
  <section class="editar-articulo">
    <h2>Editar Artículo</h2>

    <form @submit.prevent="guardarCambios">
      <label for="titulo">Título:</label>
      <input type="text" id="titulo" v-model="articulo.titulo" required>

      <label for="descripcion">Descripción:</label>
      <textarea id="descripcion" v-model="articulo.descripcion" rows="4"></textarea>

      <label for="precio">Precio:</label>
      <input type="number" id="precio" v-model="articulo.precio" required>

      <label for="categoria">Categoría:</label>
      <select id="categoria" v-model="articulo.categoria">
        <option v-for="cat in categorias" :key="cat.id" :value="cat.id">{{ cat.nombre }}</option>
      </select>

      <label for="condicion">Condición:</label>
      <select id="condicion" v-model="articulo.condicion">
        <option v-for="cond in condiciones" :key="cond.id" :value="cond.id">{{ cond.descripcion }}</option>
      </select>

      <label for="estado">Estado:</label>
      <select id="estado" v-model="articulo.estado">
        <option v-for="est in estados" :key="est.id" :value="est.id">{{ est.descripcion }}</option>
      </select>

      <label for="imagen">URL de Imagen:</label>
      <input type="text" id="imagen" v-model="articulo.imagen">

      <div class="acciones">
        <button type="submit">💾 Guardar</button>
        <button type="button" @click="$router.back()">Cancelar</button>
      </div>
    </form>
  </section>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
  name: 'EditarArticulo',
  data() {
    return {
      articulo: {
        titulo: '',
        descripcion: '',
        precio: 0,
        categoria: '',
        condicion: '',
        estado: '',
        imagen: ''
      },
      categorias: [],
      condiciones: [],
      estados: []
    };
  },
  async created() {
    const token = useUserStore().token;
    const id = this.$route.params.id;

    try {
      const [articuloRes, categoriasRes, condicionesRes, estadosRes] = await Promise.all([
        axios.get(`http://127.0.0.1:8000/api/articulos/${id}/`, { headers: { Authorization: `Bearer ${token}` } }),
        axios.get(`http://127.0.0.1:8000/api/categorias/`),
        axios.get(`http://127.0.0.1:8000/api/condiciones/`),
        axios.get(`http://127.0.0.1:8000/api/estados/`)
      ]);

      this.articulo = {
        ...articuloRes.data,
        categoria: articuloRes.data.categoria.id,
        condicion: articuloRes.data.condicion.id,
        estado: articuloRes.data.estado.id
      };
      this.categorias = categoriasRes.data;
      this.condiciones = condicionesRes.data;
      this.estados = estadosRes.data;

    } catch (err) {
      console.error('Error al cargar datos:', err);
      alert('No se pudo cargar el artículo');
    }
  },
  methods: {
    async guardarCambios() {
      const token = useUserStore().token;
      const id = this.$route.params.id;

      try {
        await axios.patch(`http://127.0.0.1:8000/api/articulos/${id}/`, this.articulo, {
          headers: { Authorization: `Bearer ${token}` }
        });

        alert('Cambios guardados correctamente.');
        this.$router.push('/mis-compras'); // o a donde quieras redirigir

      } catch (error) {
        console.error('Error al guardar cambios:', error);
        alert('Error al guardar. Verifique los datos.');
      }
    }
  }
};
</script>

<style scoped>
.editar-articulo {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #f9fff9;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

h2 {
  color: #006400;
  text-align: center;
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input, textarea, select {
  padding: 0.6rem;
  border: 2px solid #ccc;
  border-radius: 6px;
  font-size: 1rem;
}

input:focus, textarea:focus, select:focus {
  border-color: #228B22;
  outline: none;
  box-shadow: 0 0 5px rgba(0, 100, 0, 0.3);
}

.acciones {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 1rem;
}

.acciones button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
}

.acciones button:first-child {
  background-color: #006400;
  color: white;
}

.acciones button:last-child {
  background-color: #ccc;
}
</style>
