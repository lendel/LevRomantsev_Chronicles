from github import Github
from config import config

def upload_to_github(filepath):
    g = Github(config.GITHUB_TOKEN)
    repo = g.get_repo(config.GITHUB_REPO)

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    filename = filepath.split("/")[-1]
    repo.create_file(f"responses/{filename}", f"Добавлен {filename}", content)
