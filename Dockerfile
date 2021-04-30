FROM python:3.8-slim
org.opencontainers.image.source = "https://github.com/ds3002/discord-bot"

COPY . .
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["./bot.py"]
