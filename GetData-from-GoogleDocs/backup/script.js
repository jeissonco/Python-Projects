// frontend/script.js

// Función para obtener los trabajos de la API
async function get_data() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/data');
        const data = await response.json();
        mostrarTrabajos(data);
    } catch (error) {
        console.error('Error al obtener los trabajos:', error);
    }
}

// Función para mostrar los trabajos en la página
function mostrarTrabajos(trabajos) {
    const lista = document.getElementById('lista-trabajos');
    lista.innerHTML = ''; // Limpiar contenido previo

    trabajos.forEach(trabajo => {
        const div = document.createElement('div');
        div.className = 'trabajo';

        const destino = document.createElement('h2');
        destino.textContent = `Destino: ${trabajo.destino}`;

        const hora = document.createElement('p');
        hora.textContent = `Hora: ${trabajo.hora}`;

        const descripcion = document.createElement('p');
        descripcion.textContent = `Descripción: ${trabajo.descripcion}`;

        div.appendChild(destino);
        div.appendChild(hora);
        div.appendChild(descripcion);

        lista.appendChild(div);
    });
}

// Llamar a la función para obtener y mostrar los trabajos al cargar la página
get_data();
