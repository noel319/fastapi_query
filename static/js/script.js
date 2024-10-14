let currentPage = 0;
const limit = 10;

async function fetchUsers(page, filters = {}) {
    const { name, email, phone_number } = filters;
    let query = `/users?skip=${page * limit}&limit=${limit}`;
    
    if (name) query += `&name=${encodeURIComponent(name)}`;
    if (email) query += `&email=${encodeURIComponent(email)}`;
    if (phone_number) query += `&phone_number=${encodeURIComponent(phone_number)}`;

    const response = await fetch(query);
    const users = await response.json();
    displayUsers(users);
}

function displayUsers(users) {
    const tableBody = document.getElementById('user-table-body');
    tableBody.innerHTML = '';  // Clear the table

    users.forEach(user => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${user.name}</td>
            <td>${user.email}</td>
            <td>${user.phone_number}</td>
        `;
        tableBody.appendChild(row);
    });
}

document.getElementById('prev-btn').addEventListener('click', () => {
    if (currentPage > 0) {
        currentPage--;
        fetchUsers(currentPage, getSearchFilters());
    }
});

document.getElementById('next-btn').addEventListener('click', () => {
    currentPage++;
    fetchUsers(currentPage, getSearchFilters());
});

document.getElementById('search-btn').addEventListener('click', () => {
    currentPage = 0; // Reset to first page on new search
    fetchUsers(currentPage, getSearchFilters());
});

function getSearchFilters() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone_number = document.getElementById('phone_number').value;
    return { name, email, phone_number };
}

// Fetch the first page of users on page load
fetchUsers(currentPage);
