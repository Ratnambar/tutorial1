FROM python:3.13.16-slim-bookworm

WORKDIR /tutorial-django

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
# ✅ Correct - sh interprets && properly
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]