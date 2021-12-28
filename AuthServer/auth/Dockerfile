# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /auth/
COPY . /auth/

WORKDIR /auth
RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "auth/manage.py", "runserver", "0.0.0.0:8000"]