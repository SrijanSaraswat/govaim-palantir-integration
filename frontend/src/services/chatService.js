export async function sendChatQuery(queryText) {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/chat/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query: queryText })
    });

    const data = await response.json();
    return data.reply;
  } catch (error) {
    console.error("Chat API error:", error);
    return "Server error.";
  }
}
