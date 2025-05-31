<template>
    <div class="inicio-container">
        <section class="hero">
            <h2>Bienvenido a Mi Tienda - Página en construcción</h2>
            <p>Descubrí productos increíbles al mejor precio. ¡Tu experiencia de compra comienza aquí!</p>
            <router-link to="/tienda" class="cta-button">Ver artículos</router-link>
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
    name: 'PaginaInicio'
}
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
