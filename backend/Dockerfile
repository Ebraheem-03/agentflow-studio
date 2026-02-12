FROM python:3.12‑slim
WORKDIR /app
COPY uv.toml .
RUN pip install uv && uv sync && uv install
COPY app/ ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

