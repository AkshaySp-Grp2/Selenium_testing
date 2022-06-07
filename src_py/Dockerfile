FROM python:3.6
##make directory 
RUN mkdir -p /test/src 


#Work directory 
WORKDIR /test/src

#install dependencies
COPY requirements.txt /test/src
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt 


#COPY to conatiner

COPY . /test/src

ENV APP_ENV development 

#exposing port 

EXPOSE 5035 

VOLUME [ "/app-data" ] 

CMD [ "python", "main.py"]





