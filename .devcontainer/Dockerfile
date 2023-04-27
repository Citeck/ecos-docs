FROM python:3.9-alpine

RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev git

COPY requirements.txt .
RUN pip install -r "requirements.txt"

CMD [ "cd docs && make clean && make html" ]
