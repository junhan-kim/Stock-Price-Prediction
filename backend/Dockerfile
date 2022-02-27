FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
RUN apt-get install -y python3-psycopg2
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

ENV DATABASE_URL postgresql://postgres:940416@db/main
ENV SECRET_KEY secret
ENV EXEC_ENV dev
ENV WHITE_LISTS '["http://localhost:3001"]'

WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["./entrypoint.sh"]