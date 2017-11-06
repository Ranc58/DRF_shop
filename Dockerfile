 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /dj_shop
 WORKDIR /dj_shop
 ADD requirements.txt /dj_shop/
 RUN pip3 install -r requirements.txt
 ADD . /dj_shop/