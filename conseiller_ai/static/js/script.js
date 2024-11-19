document.getElementById('send-button').onclick = async function() {
    const userText = document.getElementById('user_text').value;
    
    const response = await fetch(`/detect_intent/?user_text=${encodeURIComponent(userText)}`);
    const data = await response.json();
    
    document.getElementById('response').innerText = data.response;
};
