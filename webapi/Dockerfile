FROM python:3.8.0-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
COPY src/apitest.py /dist/
COPY src/db_controller.py /dist/

WORKDIR /dist/

CMD ["python", "apitest.py"]