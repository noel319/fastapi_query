let currentPage = 0;
const limit = 10;

async function fetchUsers(page) {
    const response = await fetch(`/users?skip=${page * limit}&limit=${limit}`);
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
        fetchUsers(currentPage);
    }
});

document.getElementById('next-btn').addEventListener('click', () => {
    currentPage++;
    fetchUsers(currentPage);
});

// Fetch the first page of users on page load
fetchUsers(currentPage);
