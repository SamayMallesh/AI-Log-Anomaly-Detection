import openai

openai.api_key = "YOUR_API_KEY"

def generate_summary(logs):
    prompt = f"Summarize these logs and find possible root causes:\n{logs}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    sample_logs = [
        "ERROR: Failed to connect to database",
        "WARN: High memory usage detected"
    ]
    summary = generate_summary(sample_logs)
    print(summary)
