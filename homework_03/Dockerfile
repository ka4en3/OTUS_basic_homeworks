FROM python:3.11-slim
LABEL authors="k4n3"

WORKDIR /applic

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app/main.py"]

#ENTRYPOINT ["top", "-b"]