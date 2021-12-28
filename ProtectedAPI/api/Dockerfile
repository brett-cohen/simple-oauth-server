# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /api/
COPY . /api/

WORKDIR /api
RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "api/manage.py", "runserver", "0.0.0.0:8001"]