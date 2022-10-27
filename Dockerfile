FROM python:3.8-slim-buster

WORKDIR /app_docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV APP_PORT=3000

EXPOSE $APP_PORT

CMD ["python3", "app.py" ]



# Obs: não recomendado para produção
# mais informações: https://flask.palletsprojects.com/en/2.2.x/deploying/