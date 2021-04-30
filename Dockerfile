FROM python:3.8-slim

COPY . .
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["./bot.py"]
