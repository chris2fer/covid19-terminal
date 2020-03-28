FROM python3

RUN pip install -r requirements.txt

COPY ./src /src

