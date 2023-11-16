FROM python:3.9

RUN mkdir /home/python

WORKDIR /home/python/

COPY ./requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application files
COPY ./templates/ ./templates/
COPY ./static/ ./static/
COPY ./app.py .

CMD ["python", "app.py"]
