import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Чтение почты из файла .env
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
FIO = os.getenv("FIO")

if not USERNAME or not PASSWORD:
    raise ValueError("dotEnv variables missing")