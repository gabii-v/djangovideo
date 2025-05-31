<template>
  <div id="app">
    <header class="header">
      <h1>Mi Tienda</h1>
      <hr class="divider" />
      <nav>
        <router-link to="/">Inicio</router-link>
        <router-link to="/tienda">Tienda</router-link>
        <router-link to="/contacto">Contacto</router-link>
        <router-link to="/IniciarSesión"> MiCuenta</router-link>
        <router-link to="/mensajes" class="icon-link">💬</router-link>
        <router-link to="/mis-compras" class="icon-link">🛒</router-link>
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
}

nav a {
  margin: 0 10px;
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
