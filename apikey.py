<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Fashion Brand Chatbot</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: #f4f6f9;
      color: #333;
      font-family: 'Segoe UI', sans-serif;
    }
    .chat-container {
      max-width: 600px;
      margin: 50px auto;
      background: white;
      border-radius: 12px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.1);
      overflow: hidden;
    }
    .chat-header {
      background: #0d6efd;
      color: white;
      padding: 15px 20px;
      font-size: 1.25rem;
    }
    .chat-box {
      height: 400px;
      overflow-y: auto;
      padding: 20px;
      background: #f9fbfc;
    }
    .chat-message {
      margin-bottom: 15px;
    }
    .chat-message.user {
      text-align: right;
      color: #0d6efd;
    }
    .chat-message.bot {
      text-align: left;
      color: #495057;
    }
    .chat-input {
      display: flex;
      border-top: 1px solid #dee2e6;
    }
    .chat-input input {
      flex: 1;
      border: none;
      padding: 15px;
      font-size: 1rem;
    }
    .chat-input button {
      background: #0d6efd;
      border: none;
      color: white;
      padding: 0 25px;
    }
    .chat-input input:focus {
      outline: none;
    }
  </style>
</head>
<body>
  <div class="chat-container">
    <div class="chat-header">Fashion Support Chatbot</div>
    <div class="chat-box" id="chat-box">
      <div class="chat-message bot">Hello! Ask me about product stock, sizes, or anything else.</div>
    </div>
    <div class="chat-input">
      <input type="text" id="user-input" placeholder="Type your question here..." />
      <button onclick="sendMessage()">Send</button>
    </div>
  </div>

  <script>
    async function sendMessage() {
      const inputField = document.getElementById("user-input");
      const chatBox = document.getElementById("chat-box");
      const message = inputField.value.trim();
      if (!message) return;

      chatBox.innerHTML += <div class='chat-message user'>${message}</div>;
      inputField.value = "";
      chatBox.scrollTop = chatBox.scrollHeight;

      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
      });

      const data = await response.json();
      chatBox.innerHTML += <div class='chat-message bot'>${data.reply}</div>;
      chatBox.scrollTop = chatBox.scrollHeight;
    }

    document.getElementById("user-input").addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        sendMessage();
      }
    });
  </script>
</body>
</html>
