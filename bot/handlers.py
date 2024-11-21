from bot.openai_client import generate_story
from bot.file_manager import save_to_file
from bot.github_client import upload_to_github

async def handle_message(update, context):
    from config import config

    user_id = str(update.effective_user.id)
    if user_id != config.ADMIN_ID:
        await update.message.reply_text("Access denied. This bot is for the administrator only.")
        return

    task = update.message.text
    await update.message.reply_text(f"Задача принята: {task}")

    # Взаимодействие с OpenAI
    story = generate_story(task)

    # Сохранение в файл
    filename = save_to_file(task, story)

    # Загрузка на GitHub
    upload_to_github(filename)

    # Отправка ответа
    await update.message.reply_text(f"Ответ:\n{story}")
    await update.message.reply_document(open(filename, 'rb'))
