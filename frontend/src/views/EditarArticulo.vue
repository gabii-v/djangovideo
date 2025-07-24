<template>
  <div class="detalle-container" v-if="articulo && Object.keys(articulo).length > 0">
    <div class="imagenes">
      <img :src="fotos[fotoActual]" alt="Foto del artículo" />
      <div class="controles">
        <button @click="anterior" :disabled="fotoActual === 0">⬅️</button>
        <button @click="siguiente" :disabled="fotoActual === fotos.length - 1">➡️</button>
      </div>
    </div>
    <div class="informacion">
      <h2>{{ articulo.titulo }}</h2>
      <p><strong>Vendedor:</strong> {{ articulo.usuario?.username || 'Desconocido' }}</p>
      <p><strong>Descripción:</strong> {{ articulo.descripcion }}</p>
      <p><strong>Precio:</strong> ${{ articulo.precio }}</p>
      <button @click="enviarMensaje">Enviar mensaje al vendedor</button>
    </div>
  </div>

  <div v-else>
    <p>Cargando detalles del artículo...</p>
  </div>
</template>

<script>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { ref } from 'vue';

export default {
  name: 'ArticuloDetalle',
  setup() {
    const route = useRoute();
    const id = route.params.id;

    const articulo = ref({});
    const fotos = ref([]);
    const fotoActual = ref(0);

    axios.get(`http://127.0.0.1:8000/api/articulos/${id}/`).then(res => {
      articulo.value = res.data;
      fotos.value = res.data.fotos || [];
    }).catch(error => {
      console.error("Error al cargar el artículo:", error);
    });

    const anterior = () => {
      if (fotoActual.value > 0) fotoActual.value--;
    };

    const siguiente = () => {
      if (fotoActual.value < fotos.value.length - 1) fotoActual.value++;
    };

    const enviarMensaje = () => {
      alert("Acá iría la lógica para enviar el mensaje al vendedor.");
    };

    return { articulo, fotos, fotoActual, anterior, siguiente, enviarMensaje };
  }
};
</script>

<style scoped>
.detalle-container {
  display: flex;
  gap: 20px;
  padding: 20px;
}
.imagenes {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.imagenes img {
  max-width: 100%;
  height: auto;
}
.controles {
  margin-top: 10px;
}
.informacion {
  flex: 1;
}
</style>
