# Dockerfile для запуска FastAPI приложения

# Как запустить контейнер:
# docker build -t hw3 .
# docker run -d -p 8000:8000 hw3

# Используем образ Python 3.11 в качестве основы, slim - легковесный
FROM python:3.11-slim

LABEL authors="k4n3"

# Устанавливаем рабочую директорию внутри контейнера (usual 'app')
WORKDIR /applic

# Копируем файл requirements.txt (если он есть)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все модули приложения
COPY . .

#Команда EXPOSE в Dockerfile не открывает порт, а только документирует, что контейнер использует этот порт. Это просто метка для других разработчиков и оркестраторов контейнеров (например, Docker Compose или Kubernetes).
EXPOSE 8000

# Запускаем Uvicorn сервер
# слушать на всех сетевых интерфейсах. Чтобы сервер был доступен из любой сети (например, внутри Docker-контейнера или локальной сети).
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
