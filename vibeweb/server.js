// server.js
const express = require("express");
const cors = require("cors");
const fetch = require("node-fetch");

const app = express();
app.use(cors());
app.use(express.json());

// 1. Health-check endpoint
app.get("/hello", (req, res) => {
  res.json({ msg: "Node backend is running" });
});

// 2. Proxy /chat to the Python AI service
app.post("/chat", async (req, res) => {
  const prompt = (req.body.prompt || "").trim();
  if (!prompt) {
    return res.status(400).json({ error: "No prompt provided" });
  }

  try {
    // Forward to Flask’s /generate endpoint (running on port 5000)
    const aiResponse = await fetch("http://127.0.0.1:5000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    const json = await aiResponse.json();
    return res.json({ reply: json.generated });
  } catch (err) {
    console.error("Error calling Python AI:", err);
    return res.status(500).json({ error: "AI server error" });
  }
});

// Start the Node server on port 3000
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Node server running at http://localhost:${PORT}`);
});
