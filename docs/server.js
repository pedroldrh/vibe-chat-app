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

  const flaskUrl = process.env.FLASK_URL;
  if (!flaskUrl) {
    console.error("FLASK_URL is not set");
    return res.status(500).json({ error: "Server misconfigured" });
  }

  try {
    const aiResponse = await fetch(`${flaskUrl}/generate`, {
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

// Start the Node server on port 3000 (or process.env.PORT in Render)
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Node server running on port ${PORT}`);
});
