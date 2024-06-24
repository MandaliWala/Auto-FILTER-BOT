# Don't Remove Credit @Tonystark_botz
# Ask Doubt on telegram @Spider_Man_02
FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /Auto-FILTER-BOT
WORKDIR /Auto-FILTER-BOT
COPY . /Auto-FILTER-BOT
CMD ["python", "bot.py"]
