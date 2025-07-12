// src/api/usuarios.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

export async function registerUser({ username, email, password }) {
    const response = await axios.post(`${API_URL}/auth/register/`, {
        username,
        email,
        password
    });
    return response.data;
}

export async function loginUser({ username, password }) {
    try {
        const response = await axios.post(`${API_URL}/auth/login/`, {
            username,
            password
        });
        return response.data; // debe incluir { access, refresh }
    } catch (error) {
        console.error('Error login:', error.response?.data || error.message);
        throw error;
    }
}

// ✅ Obtener usuario autenticado con token
export async function getUsuarioAutenticado(token) {
    try {
        const response = await axios.get(`${API_URL}/usuarios/me/`, {
            headers: {
                Authorization: `Bearer ${token}`
            }
        });
        return response.data; // debe traer el username, email, etc.
    } catch (error) {
        console.error('Error al obtener usuario autenticado:', error.response?.data || error.message);
        throw error;
    }
}
