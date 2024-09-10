document.getElementById('product-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const price = document.getElementById('price').value;

    fetch('/api/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, description, price }),
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => { throw data; });
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        fetchProducts();
        document.getElementById('error-message').innerHTML = ''; // Clear error message
    })
    .catch((error) => {
        console.error('Error:', error);
        displayErrors(error);
    });
});

function displayErrors(errors) {
    const errorMessageDiv = document.getElementById('error-message');
    errorMessageDiv.innerHTML = ''; // Clear previous errors

    const ul = document.createElement('ul');
    for (const [field, messages] of Object.entries(errors)) {
        if (Array.isArray(messages)) {
            messages.forEach(message => {
                const li = document.createElement('li');
                li.innerText = `${field}: ${message}`;
                ul.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.innerText = `${field}: ${messages}`;
            ul.appendChild(li);
        }
    }
    errorMessageDiv.appendChild(ul);
}


function fetchProducts() {
    fetch('/api/products/')
    .then(response => response.json())
    .then(data => {
        const tbody = document.getElementById('product-table').getElementsByTagName('tbody')[0];
        tbody.innerHTML = '';
        data.forEach(product => {
            const row = tbody.insertRow();
            row.insertCell(0).innerText = product.name;
            row.insertCell(1).innerText = product.description;
            row.insertCell(2).innerText = product.price;
        });
    });
}

fetchProducts();
