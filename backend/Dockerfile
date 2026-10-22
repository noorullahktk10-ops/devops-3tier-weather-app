FROM python:3.11-alpine
WORKDIR /app
RUN adduser -D appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s CMD wget --no-verbose --tries=1 --spider http://localhost:5000/ || exit 1
CMD ["python", "app.py"]
