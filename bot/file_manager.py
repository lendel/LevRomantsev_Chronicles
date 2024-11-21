import os
from datetime import datetime

def save_to_file(task, content):
    directory = "storage/responses/"
    os.makedirs(directory, exist_ok=True)
    filename = f"{directory}{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"# Задача:\n{task}\n\n# Ответ:\n{content}")
    return filename
