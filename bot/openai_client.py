import openai
from config import config

# Укажите API-ключ
openai.api_key = config.OPENAI_API_KEY

def generate_story(task, assistant_id):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Используем модель, поддерживающую ассистентов
        messages=[
            {"role": "system", "content": f"Assistant ID: {assistant_id}"},
            {"role": "user", "content": task}
        ],
        max_tokens=1000
    )
    return response.choices[0].message['content'].strip()
