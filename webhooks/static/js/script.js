document.addEventListener('DOMContentLoaded', function() {
    fetch('/webhook-data')
        .then(response => response.json())
        .then(data => {
            const webhookDataDiv = document.getElementById('webhook-data');
            webhookDataDiv.innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error fetching webhook data:', error));
});
