FROM python:3
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD python manage.py migrate && \
   python manage.py runserver 0.0.0.0:8080
EXPOSE 8080
