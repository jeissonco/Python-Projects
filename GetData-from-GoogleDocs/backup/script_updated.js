// frontend/script.js

// Función para obtener los trabajos de la API
async function get_data() {
    try {
        const response = await fetch('http://127.0.0.1:5500/api/data');
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

        const job = document.createElement('h2');
        job.textContent = `JOB: ${trabajo.job}`;

        const office_notes = document.createElement('p');
        office_notes.textContent = `OFFICE NOTES: ${trabajo.office_notes}`;

        const business_name = document.createElement('p');
        business_name.textContent = `BUSINESS/NAME: ${trabajo.business_name}`;

        const unit = document.createElement('p');
        unit.textContent = `UNIT: ${trabajo.unit}`;

        const location = document.createElement('p');
        location.textContent = `LOCATION: ${trabajo.location}`;

        const suburb = document.createElement('p');
        suburb.textContent = `SUBURB: ${trabajo.suburb}`;

        const contact = document.createElement('p');
        contact.textContent = `CONTACT: ${trabajo.contact}`;

        const box_size = document.createElement('p');
        box_size.textContent = `BOX SIZE: ${trabajo.box_size}`;

        const quantity = document.createElement('p');
        quantity.textContent = `# DROPPED: ${trabajo.quantity}`;

        const dropped = document.createElement('p');
        dropped.textContent = `DROPPED: ${trabajo.dropped}`;

        const picked_up = document.createElement('p');
        picked_up.textContent = `PICKED UP: ${trabajo.picked_up}`;

        const units_picked = document.createElement('p');
        units_picked.textContent = `# PICKED UP : ${trabajo.units_picked}`;

        const notes_job = document.createElement('p');
        notes_job.textContent = `NOTES: ${trabajo.notes_job}`;

        div.appendChild(destino);
        div.appendChild(hora);
        div.appendChild(descripcion);

        lista.appendChild(div);
    });
}

// Llamar a la función para obtener y mostrar los trabajos al cargar la página
get_data();
