// src/api/auth.js
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/auth';



export async function loginUser(username, password) {
    const response = await axios.post(`${API_URL}/login/`, {
        username,
        password
    });
    return response.data;
}
