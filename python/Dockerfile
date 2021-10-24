# FROM python:3.9
# COPY main.py .
# COPY requirements.txt . 
# CMD [ "python3 main.py" ]


FROM python:3
WORKDIR /usr/src/app

## Un-comment below lines to install dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
ENTRYPOINT [ "python3", "./main.py" ]