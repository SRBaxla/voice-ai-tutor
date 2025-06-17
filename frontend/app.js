// Simple Vanilla JS for demo; replace with React as needed
const micBtn = document.getElementById('mic-btn');
const transcriptDiv = document.getElementById('transcript');
const responseDiv = document.getElementById('response');

micBtn.onclick = async () => {
    transcriptDiv.textContent = 'Listening... (not implemented)';
    // TODO: Implement Web Speech API or audio recording
    // For now, prompt for text
    const userText = prompt('Say something (type for now):');
    transcriptDiv.textContent = userText;
    const res = await fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: 'demo', text: userText })
    });
    const data = await res.json();
    responseDiv.textContent = data.response;
    // TODO: Add TTS playback
};
