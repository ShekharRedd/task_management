FROM python:latest

RUN mkdir /home/python 

WORKDIR /home/python
COPY ./static ./static

COPY ./templates ./templates 

COPY ./app.py ./app.py 

COPY ./requirements.txt ./requirements.txt 


RUN pip install -r /home/python/requirements.txt 

CMD [ "python","app.py" ]
