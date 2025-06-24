<template>
  <div id="app">
    <header class="header">
      <h1>Mi Tienda</h1>
      <hr class="divider" />
      <nav>
        <router-link to="/">Inicio</router-link>
        <router-link to="/tienda">Tienda</router-link>
        <router-link to="/contacto">Contacto</router-link>
        <router-link to="/IniciarSesión">MiCuenta</router-link>
        <router-link to="/mensajes" class="icon-link">💬</router-link>
        <router-link to="/mis-compras" class="icon-link">🛒</router-link>

        <!-- Menú desplegable de usuario -->
        <div class="dropdown" @mouseleave="mostrarMenu = false">
          <button @click="mostrarMenu = !mostrarMenu" class="dropdown-btn icon-link" aria-label="Usuario">
            👤
          </button>
          <div v-if="mostrarMenu" class="dropdown-menu">
            <router-link to="/usuario" @click="mostrarMenu = false">Información de Usuario</router-link>
            <button @click="cerrarSesion">Cerrar sesión</button>
          </div>
        </div>
      </nav>
    </header>

    <main class="main">
      <router-view />
    </main>

    <footer class="footer">
      <p>&copy; 2025 Mi Tienda - Todos los derechos reservados</p>
      <div class="redes">
        <a href="https://www.instagram.com" target="_blank" aria-label="Instagram">
          <i class="fab fa-instagram"></i>
        </a>
        <a href="https://wa.me/5491123456789" target="_blank" aria-label="WhatsApp">
          <i class="fab fa-whatsapp"></i>
        </a>
        <a href="https://www.facebook.com" target="_blank" aria-label="Facebook">
          <i class="fab fa-facebook-f"></i>
        </a>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mostrarMenu: false
    };
  },
  methods: {
    cerrarSesion() {
      alert("Sesión cerrada");
      this.$router.push("/IniciarSesión");
    }
  }
};
</script>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css');

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main {
  flex: 1;
}

.header {
  background-color: #90ee90;
  padding: 1rem;
  text-align: center;
}

.divider {
  border: none;
  border-top: 2px solid #006400;
  margin: 1rem auto;
  width: 60%;
}

nav {
  margin-top: 1rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}

nav a {
  text-decoration: none;
  color: #000;
  font-weight: bold;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.router-link-exact-active {
  color: white;
  background-color: #006400;
  padding: 5px 10px;
  border-radius: 5px;
}

/* Iconos */
.icon-link {
  font-size: 1.4rem;
  display: inline-block;
  line-height: 1.4;
}

/* Dropdown usuario */
.dropdown {
  position: relative;
}

.dropdown-btn {
  background: none;
  border: none;
  cursor: pointer;
}

.dropdown-menu {
  position: absolute;
  top: 2rem;
  right: 0;
  background: white;
  border: 1px solid #ccc;
  padding: 0.5rem;
  z-index: 10;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  min-width: 160px;
}

.dropdown-menu a,
.dropdown-menu button {
  text-align: left;
  padding: 8px 12px;
  background: none;
  border: none;
  color: #333;
  font-size: 1rem;
  font-weight: normal;
  cursor: pointer;
  text-decoration: none;
  width: 100%;
}

.dropdown-menu a:hover,
.dropdown-menu button:hover {
  background-color: #eee;
}

.footer {
  background-color: #90ee90;
  padding: 1rem;
  text-align: center;
  border-top: 2px solid #006400;
  font-size: 0.9rem;
  color: #333;
}

.footer .redes {
  margin-top: 0.5rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.footer .redes a {
  color: #333;
  font-size: 1.4rem;
  transition: color 0.3s;
}

.footer .redes a:hover {
  color: #006400;
}
</style>
