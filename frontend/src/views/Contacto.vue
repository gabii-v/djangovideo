<template>
    <div class="contact-container">
        <h2>Contáctanos - Página en construcción</h2>
        <p>¿Tienes alguna pregunta o sugerencia? Completa el siguiente formulario y te responderemos lo antes posible.
        </p>

        <form @submit.prevent="enviarFormulario">
            <div class="form-group">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" v-model="form.nombre" required />
            </div>

            <div class="form-group">
                <label for="email">Correo electrónico:</label>
                <input type="email" id="email" v-model="form.email" required />
            </div>

            <div class="form-group">
                <label for="asunto">Asunto:</label>
                <input type="text" id="asunto" v-model="form.asunto" required />
            </div>

            <div class="form-group">
                <label for="mensaje">Mensaje:</label>
                <textarea id="mensaje" v-model="form.mensaje" required></textarea>
            </div>

            <button type="submit">Enviar</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'PaginaContacto',
    data() {
        return {
            form: {
                nombre: '',
                email: '',
                asunto: '',
                mensaje: ''
            }
        }
    },
    methods: {
        enviarFormulario() {
            // Por ahora solo mostramos los datos en consola
            console.log("Formulario enviado:", this.form);
            alert("¡Gracias por tu mensaje! Nos pondremos en contacto pronto.");

            // Reinicia el formulario
            this.form = {
                nombre: '',
                email: '',
                asunto: '',
                mensaje: ''
            };
        }
    }
}
</script>

<style scoped>
.contact-container {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

h2 {
    color: #006400;
    margin-bottom: 0.5rem;
    text-align: center;
}

p {
    text-align: center;
    margin-bottom: 2rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

label {
    display: block;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

input,
textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    resize: vertical;
}

button {
    background-color: #006400;
    color: white;
    padding: 0.75rem 2rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    width: 100%;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #228B22;
}
</style>
