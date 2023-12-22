# FROM python:3.8

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# # Install SonarQube Scanner
# RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-<version>.zip && \
#     unzip sonar-scanner-cli-<version>.zip && \
#     rm sonar-scanner-cli-<version>.zip

# ENV PATH="/app/sonar-scanner-cli-<version>/bin:${PATH}"

# CMD ["sonar-scanner", "-X"]


FROM python:latest

RUN mkdir /home/python 

WORKDIR /home/python
COPY ./static ./static

COPY ./templates ./templates 

COPY ./app.py ./app.py 

COPY ./requirements.txt ./requirements.txt 


RUN pip install -r /home/python/requirements.txt 

CMD [ "python","app.py" ]
