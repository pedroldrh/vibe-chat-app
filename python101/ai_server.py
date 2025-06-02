from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# 1. Grab your API key from the environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment.")

# 2. Instantiate the OpenAI client
client = OpenAI(api_key=api_key)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(force=True) or {}
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # 3. Call GPT-4 via the Chat Completions API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,         # Adjust as needed
            temperature=0.9,        # Control creativity/coherence
            top_p=0.9,              # Nucleus sampling
            # You can add other params like top_k or presence_penalty here if needed
        )
        reply = response.choices[0].message.content
        return jsonify({"generated": reply})
    except Exception as e:
        # 4. If something goes wrong, return an error
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run on port 5000 so Node can proxy to it
    app.run(host="127.0.0.1", port=5000)
