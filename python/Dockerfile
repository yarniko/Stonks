FROM python:3
WORKDIR /usr/src/app

COPY ./requirements.txt .
COPY ./main.py .
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "./main.py" ]