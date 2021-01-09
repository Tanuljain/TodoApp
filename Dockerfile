FROM python:3.7-alpine
RUN apk add --no-cache git
RUN git clone https://github.com/Tanuljain/TodoApp.git
WORKDIR TodoApp
RUN pip install -r requirements.txt
WORKDIR config
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]