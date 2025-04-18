FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt


RUN pip install fastapi uvicorn

ENV LITELLM_PROVIDER=openrouter
ENV LITELLM_DEBUG=True

EXPOSE 8000

CMD ["uvicorn", "chat_api:app", "--host", "0.0.0.0", "--port", "8000"]
