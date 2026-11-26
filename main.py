import os
from dotenv import load_dotenv

load_dotenv()

print('Халуа')

def print_author():
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()
