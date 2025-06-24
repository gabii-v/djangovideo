<template>
    <div class="usuario-container">
        <h2>Información del Usuario</h2>

        <!-- Foto de perfil -->
        <div class="foto-perfil">
            <img :src="usuario.foto || defaultImage" alt="Foto de perfil" />
        </div>

        <div class="datos-usuario">
            <p><strong>Nombre:</strong> {{ usuario.nombreCompleto }}</p>
            <p><strong>Email:</strong> {{ usuario.email }}</p>
            <p><strong>Teléfono:</strong> {{ usuario.telefono }}</p>
            <p><strong>Localidad:</strong> {{ usuario.localidad }}</p>
            <p><strong>Dirección:</strong> {{ usuario.direccion }}</p>
            <p><strong>Fecha de registro:</strong> {{ usuario.fechaRegistro }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'UsuarioView',  // nombre multi-word para ESLint
    data() {
        return {
            defaultImage: 'https://via.placeholder.com/150',
            usuario: {
                foto: '',  // Aquí puede ir la URL o base64 de la foto
                nombreCompleto: 'Juan Pérez',
                email: 'juan.perez@gmail.com',
                telefono: '1123456789',
                localidad: 'Buenos Aires',
                direccion: 'Calle Falsa 123',
                fechaRegistro: '01/01/2024'
            }
        };
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
