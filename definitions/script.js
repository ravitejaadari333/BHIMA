const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const stickerArea = document.getElementById('sticker-area');

window.onload = () => {
  appendMessage("👋 Hi! How can I assist you today?", "bot");
};

function appendMessage(message, sender) {
  const msg = document.createElement('div');
  msg.className = `message ${sender}`;
  msg.textContent = message;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function addSticker() {
  const stickers = ['🎉', '💬', '🤖', '✨', '👍', '🧠', '👾', '🚀', '😎', '❤️'];
  const sticker = document.createElement('div');
  sticker.className = 'sticker';
  sticker.textContent = stickers[Math.floor(Math.random() * stickers.length)];

  // Random position
  sticker.style.left = Math.random() * 90 + '%';
  sticker.style.top = Math.random() * 80 + '%';

  stickerArea.appendChild(sticker);

  // Remove after animation
  setTimeout(() => {
    sticker.remove();
  }, 3000);
}

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;
  appendMessage(message, 'user');
  userInput.value = '';
  addSticker();

  try {
    const response = await fetch('http://localhost:5000/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
    const data = await response.json();
    appendMessage(data.reply || "No response", 'bot');
  } catch (err) {
    appendMessage("⚠️ Unable to connect to server.", 'bot');
  }
}
