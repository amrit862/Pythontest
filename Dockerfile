FROM ubuntu:latest

RUN apt-get update \ 
    && apt-get install -y python3-pip python3-dev \
    && pip3 --no-cache-dir install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 install --no-cache-dir  -r requirements.txt
EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD ["Registration.py"]