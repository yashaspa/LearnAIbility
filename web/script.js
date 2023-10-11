document.getElementById('enterButton').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    const prompt = `Explain ${userInput} to me like I'm five?`;

    // Make a request to OpenAI API (this is a simplified example; you'll need to set up the API call properly)
    fetch('YOUR_OPENAI_API_ENDPOINT', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer YOUR_API_KEY',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt: prompt,
            max_tokens: 150
        })
    })
    .then(response => response.json())
    .then(data => {
        const answer = data.choices[0].text.trim();
        // Redirect to a new page and pass the answer as a URL parameter
        window.location.href = `answer.html?response=${encodeURIComponent(answer)}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
