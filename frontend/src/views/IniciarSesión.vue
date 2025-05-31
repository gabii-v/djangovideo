<template>
    <section class="registro">
        <h2>Iniciar Sesión</h2>
        <form @submit.prevent="registrarse">
            <div class="campo">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" v-model="form.nombre" required />
            </div>

            <div class="campo">
                <label for="email">Email:</label>
                <input type="email" id="email" v-model="form.email" required />
            </div>

            <div class="campo">
                <label for="password">Contraseña:</label>
                <input type="password" id="password" v-model="form.password" required />
            </div>

            <button type="submit">Iniciar</button>
        </form>
        <p class="registro-link">
            ¿No tenés cuenta?
            <a href="#" @click.prevent="irARegistro">Registrarme</a>
        </p>
    </section>
</template>

<script>
export default {
    name: 'PaginaInicioSesion',  // Nombre multi-word para evitar warning eslint
    data() {
        return {
            form: {
                nombre: '',
                email: '',
                password: ''
            }
        };
    },
    methods: {
        registrarse() {
            console.log('Datos enviados:', this.form);
            alert('¡Inicio de sesión simulado!');
        },
        irARegistro() {
            this.$router.push('/registro'); // Navega a la ruta '/registro'
        }
    }
};
</script>

<style scoped>
.registro {
    max-width: 400px;
    margin: 2rem auto;
    padding: 2rem;
    border-radius: 12px;
    background: #f0fff0;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.registro h2 {
    text-align: center;
    margin-bottom: 1.5rem;
    color: #006400;
}

.campo {
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 0.5rem;
    font-weight: bold;
}

input {
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 6px;
}

button {
    width: 100%;
    padding: 0.75rem;
    background-color: #006400;
    color: white;
    border: none;
    border-radius: 6px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #004d00;
}

.registro-link {
    margin-top: 1rem;
    text-align: center;
}

.registro-link a {
    color: #006400;
    font-weight: bold;
    cursor: pointer;
    text-decoration: underline;
}

.registro-link a:hover {
    color: #004d00;
}
</style>
