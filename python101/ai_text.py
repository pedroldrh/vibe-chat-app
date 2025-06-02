from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "Once upon a vibe-filled night,"
outputs = generator(prompt, max_length=60, num_return_sequences=1)
print("=== Your GPT-2 Generated Text ===")
print(outputs[0]["generated_text"])
