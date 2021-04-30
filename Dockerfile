FROM python:3.8-slim

WORKDIR ["/"]
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY bot.py bot.py
RUN chmod 755 bot.py

ENTRYPOINT ["./bot.py"]
