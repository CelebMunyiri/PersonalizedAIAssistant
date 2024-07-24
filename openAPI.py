from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.9,
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "What is the sentiment of the following review: 'The movie was excellent. I loved every moment.'",
        }
    ],
)

