<template>
    <section class="registro">
        <!-- Flecha para volver -->
        <button class="btn-volver" @click="volverLogin" aria-label="Volver">
            ←
        </button>

        <h2>Registro de Usuario</h2>
        <form @submit.prevent="RegistroUsuario">
            <fieldset>
                <legend>INFORMACIÓN PERSONAL</legend>
                <div class="campo">
                    <label for="nombre">Nombre:</label>
                    <input type="text" id="nombre" v-model="form.nombre" required />
                </div>

                <div class="campo">
                    <label for="apellido">Apellido:</label>
                    <input type="text" id="apellido" v-model="form.apellido" required />
                </div>

                <div class="campo">
                    <label for="genero">Género:</label>
                    <select id="genero" v-model="form.genero" required>
                        <option value="" disabled>Seleccione...</option>
                        <option value="masculino">Masculino</option>
                        <option value="femenino">Femenino</option>
                        <option value="otro">Otro</option>
                        <option value="prefiero_no_decir">Prefiero no decir</option>
                    </select>
                </div>
            </fieldset>

            <fieldset>
                <legend>INFORMACIÓN DE INICIO DE SESIÓN</legend>
                <div class="campo">
                    <label for="email">Correo electrónico:</label>
                    <input type="email" id="email" v-model="form.email" required />
                </div>

                <div class="campo">
                    <label for="password">Contraseña:</label>
                    <input :type="mostrarContrasena ? 'text' : 'password'" id="password" v-model="form.password"
                        required />
                </div>

                <div class="campo">
                    <label for="confirmarPassword">Confirmar contraseña:</label>
                    <input :type="mostrarContrasena ? 'text' : 'password'" id="confirmarPassword"
                        v-model="form.confirmarPassword" required />
                </div>

                <div class="campo mostrar-contrasena">
                    <input type="checkbox" id="mostrarContrasena" v-model="mostrarContrasena" />
                    <label for="mostrarContrasena">Mostrar contraseña</label>
                </div>
            </fieldset>

            <button type="submit">Crear cuenta</button>
        </form>
    </section>
</template>

<script>
import { registerUser } from '@/api/usuarios';

export default {
    name: "RegistroUsuario",
    data() {
        return {
            form: {
                nombre: "",
                apellido: "",
                genero: "",
                email: "",
                password: "",
                confirmarPassword: "",
            },
            mostrarContrasena: false,
        };
    },
    methods: {
        async RegistroUsuario() {
            if (this.form.password !== this.form.confirmarPassword) {
                alert("Las contraseñas no coinciden");
                return;
            }

            try {
                await registerUser({
                    username: this.form.nombre,  // usamos 'nombre' como username
                    email: this.form.email,
                    password: this.form.password
                });

                alert("Cuenta creada con éxito. Ahora podés iniciar sesión.");
                this.$router.push("/IniciarSesión");

            } catch (error) {
                console.error(error);
                alert("Error al registrarse. Verificá los datos o probá con otro email.");
            }
        },
        volverLogin() {
            this.$router.push("/IniciarSesión");
        },
    },
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
    position: relative;
}

/* Botón flecha volver */
.btn-volver {
    position: absolute;
    top: 1rem;
    left: 1rem;
    font-size: 1.5rem;
    background: none;
    border: none;
    cursor: pointer;
    color: #006400;
    font-weight: bold;
    padding: 0;
    line-height: 1;
    user-select: none;
}

.btn-volver:hover {
    color: #004d00;
}

.registro h2 {
    text-align: center;
    margin-bottom: 1.5rem;
    color: #006400;
}

fieldset {
    border: 1px solid #ccc;
    padding: 1rem 1.5rem;
    margin-bottom: 1.5rem;
    border-radius: 8px;
}

legend {
    font-weight: bold;
    padding: 0 0.5rem;
    color: #004d00;
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

input,
select {
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

.mostrar-contrasena {
    flex-direction: row;
    align-items: center;
}

.mostrar-contrasena label {
    margin: 0 0 0 0.5rem;
    font-weight: normal;
    cursor: pointer;
}
</style>
