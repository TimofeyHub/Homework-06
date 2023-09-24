FROM tiangolo/uwsgi-nginx-flask:python3.10

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

RUN chmod +x ./prestart-dev.sh
ENTRYPOINT ["sh", "./prestart-dev.sh"]
CMD ["python", "app.py"]