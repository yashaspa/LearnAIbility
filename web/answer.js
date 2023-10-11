// Get the response from the URL parameter and display it
const urlParams = new URLSearchParams(window.location.search);
const response = urlParams.get('response');
document.getElementById('response').textContent = response;
