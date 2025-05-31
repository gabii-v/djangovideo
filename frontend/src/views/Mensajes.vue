<template>
    <section class="mensajes">
        <h2>Mis Mensajes</h2>

        <div v-if="mensajes.length === 0" class="empty-state">
            <p>No tienes mensajes nuevos.</p>
        </div>

        <ul v-else class="lista-mensajes">
            <li v-for="mensaje in mensajes" :key="mensaje.id" class="mensaje-item">
                <strong>{{ mensaje.remitente }}</strong>
                <p>{{ mensaje.texto }}</p>
                <small>{{ mensaje.fecha }}</small>
            </li>
        </ul>
    </section>
</template>

<script>
export default {
    name: 'MisMensajes',
    data() {
        return {
            mensajes: [
                {
                    id: 1,
                    remitente: 'Juan Pérez',
                    texto: 'Hola, ¿todavía está disponible el producto?',
                    fecha: '2025-05-28 14:32',
                },
                {
                    id: 2,
                    remitente: 'Ana Gómez',
                    texto: 'Gracias por tu compra, ¿cómo fue tu experiencia?',
                    fecha: '2025-05-27 10:15',
                },
            ],
        };
    },
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
    transition: background-color 0.2s ease;
}

.mensaje-item:hover {
    background-color: #e6ffe6;
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

.empty-state {
    text-align: center;
    font-style: italic;
    color: #666;
    padding: 2rem;
}
</style>
