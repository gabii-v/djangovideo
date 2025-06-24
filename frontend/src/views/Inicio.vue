<template>
    <div class="inicio-container">
        <section class="hero">
            <h2>Bienvenido a Mi Tienda</h2>
            <p>Descubrí productos increíbles al mejor precio. ¡Tu experiencia de compra comienza aquí!</p>
            <router-link to="/tienda" class="cta-button">Ver artículos</router-link>
        </section>

        <section class="galeria-imagenes" ref="galeria" @mousemove="moverScroll" @mouseleave="detenerScroll">
            <div v-for="(img, index) in imagenes.slice(0, 4)" :key="index" class="imagen-container"
                :class="{ activo: index === indiceActivo }" @mouseenter="indiceActivo = index"
                @mouseleave="indiceActivo = null">
                <img :src="img" alt="Imagen del producto" />
            </div>

            <div class="imagen-container ver-mas" @click="irATienda">
                <span>Ver más ➔</span>
            </div>
        </section>

        <section class="features">
            <div class="feature">
                <h3>🚚 Envíos rápidos</h3>
                <p>Recibí tus productos en tiempo récord.</p>
            </div>
            <div class="feature">
                <h3>💳 Pagos seguros</h3>
                <p>Tu información protegida.</p>
            </div>
            <div class="feature">
                <h3>⭐ Productos seleccionados</h3>
                <p>Una tienda curada con los mejores artículos para vos.</p>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    name: "PaginaInicio",
    data() {
        return {
            imagenes: [
                "https://via.placeholder.com/300x200?text=Producto+1",
                "https://via.placeholder.com/300x200?text=Producto+2",
                "https://via.placeholder.com/300x200?text=Producto+3",
                "https://via.placeholder.com/300x200?text=Producto+4",
                "https://via.placeholder.com/300x200?text=Producto+5",
            ],
            indiceActivo: null,
            scrollInterval: null,
        };
    },
    methods: {
        moverScroll(event) {
            const galeria = this.$refs.galeria;
            const rect = galeria.getBoundingClientRect();
            const mouseX = event.clientX - rect.left;
            const ancho = galeria.clientWidth;

            const porcentaje = mouseX / ancho;
            const maxScroll = galeria.scrollWidth - galeria.clientWidth;
            const scrollPos = porcentaje * maxScroll;

            galeria.scrollTo({
                left: scrollPos,
                behavior: "smooth",
            });
        },
        detenerScroll() {
            // No hace nada
        },
        irATienda() {
            this.$router.push("/tienda");
        },
    },
};
</script>

<style scoped>
.inicio-container {
    max-width: 960px;
    margin: 2rem auto;
    padding: 2rem;
    text-align: center;
}

.hero {
    background-color: #e8f5e9;
    padding: 2rem;
    border-radius: 10px;
    margin-bottom: 2rem;
}

.hero h2 {
    font-size: 2rem;
    color: #006400;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.2rem;
    color: #333;
    margin-bottom: 1.5rem;
}

.cta-button {
    display: inline-block;
    background-color: #006400;
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
    transition: background-color 0.3s ease;
}

.cta-button:hover {
    background-color: #004d00;
}

.galeria-imagenes {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: nowrap;
    overflow-x: auto;
    padding-bottom: 10px;

    scrollbar-width: none;
    -ms-overflow-style: none;
}

.galeria-imagenes::-webkit-scrollbar {
    display: none;
}

.imagen-container {
    overflow: hidden;
    border-radius: 10px;
    width: 300px;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 3px solid #006400;
    box-shadow: 0 2px 8px rgba(0, 100, 0, 0.3);
    flex-shrink: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    transform: scale(1);
}

.imagen-container.activo {
    transform: scale(1.3);
    box-shadow: 0 6px 15px rgba(0, 100, 0, 0.6);
}

.imagen-container img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    transition: transform 0.3s ease;
    display: block;
    transform: scale(1);
}

.imagen-container.activo img {
    transform: scale(1.3);
}

.ver-mas {
    border: 3px dashed #006400;
    font-weight: bold;
    font-size: 1.3rem;
    color: #006400;
    cursor: pointer;
    user-select: none;
    transition: background-color 0.3s ease, color 0.3s ease;
    display: flex;
    justify-content: center;
    align-items: center;
}

.ver-mas:hover {
    background-color: #006400;
    color: white;
    border-color: #004d00;
}

.features {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 1rem;
}

.feature {
    flex: 1 1 250px;
    background-color: #f9f9f9;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.feature h3 {
    color: #006400;
    margin-bottom: 0.5rem;
}
</style>
