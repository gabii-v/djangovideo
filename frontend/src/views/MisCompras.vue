<template>
    <section class="compras">
        <h2>Mis Compras y Ventas</h2>

        <div class="cuadros">
            <div class="cuadro">
                <h3>Artículos Comprados</h3>
                <div v-if="comprasCompradas.length === 0" class="empty-state">
                    <p>No has comprado artículos aún.</p>
                </div>
                <table v-else class="tabla-compras">
                    <thead>
                        <tr>
                            <th>Producto</th>
                            <th>Fecha</th>
                            <th>Precio</th>
                            <th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="compra in comprasCompradas" :key="compra.id">
                            <td>{{ compra.producto }}</td>
                            <td>{{ compra.fecha }}</td>
                            <td>{{ formatearMoneda(compra.precio) }}</td>
                            <td>{{ compra.estado }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="cuadro">
                <h3>Artículos Vendidos</h3>
                <div v-if="comprasVendidas.length === 0" class="empty-state">
                    <p>No has vendido artículos aún.</p>
                </div>
                <table v-else class="tabla-compras">
                    <thead>
                        <tr>
                            <th>Producto</th>
                            <th>Fecha</th>
                            <th>Precio</th>
                            <th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="compra in comprasVendidas" :key="compra.id">
                            <td>{{ compra.producto }}</td>
                            <td>{{ compra.fecha }}</td>
                            <td>{{ formatearMoneda(compra.precio) }}</td>
                            <td>{{ compra.estado }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'MisCompras',
    data() {
        return {
            compras: [
                {
                    id: 1,
                    producto: 'Auriculares Bluetooth',
                    tipo: 'Compra',
                    fecha: '2025-05-15',
                    precio: 1500,
                    estado: 'Entregado',
                },
                {
                    id: 2,
                    producto: 'Camiseta Deportiva',
                    tipo: 'Venta',
                    fecha: '2025-05-20',
                    precio: 800,
                    estado: 'Entregado',
                },
            ],
        };
    },
    computed: {
        comprasCompradas() {
            return this.compras.filter(c => c.tipo === 'Compra');
        },
        comprasVendidas() {
            return this.compras.filter(c => c.tipo === 'Venta');
        },
    },
    methods: {
        formatearMoneda(valor) {
            return `$ ${valor.toLocaleString('es-AR', { minimumFractionDigits: 2 })}`;
        },
    },
};
</script>

<style scoped>
.compras {
    max-width: 900px;
    margin: 2rem auto;
    padding: 2rem;
    background: #f0fff0;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.compras h2 {
    color: #006400;
    text-align: center;
    margin-bottom: 2rem;
}

.cuadros {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
    justify-content: center;
}

.cuadro {
    flex: 1 1 400px;
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.06);
}

.cuadro h3 {
    color: #006400;
    margin-bottom: 1rem;
    text-align: center;
}

.tabla-compras {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
}

.tabla-compras thead {
    background-color: #006400;
    color: white;
}

.tabla-compras th,
.tabla-compras td {
    padding: 0.75rem 1rem;
    border: 1px solid #ccc;
    text-align: center;
}

.tabla-compras tbody tr:hover {
    background-color: #e6ffe6;
}

.empty-state {
    text-align: center;
    font-style: italic;
    color: #666;
    padding: 2rem;
}
</style>
