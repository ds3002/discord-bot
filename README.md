# Discord Bot

A simple Discord bot for future projects.

Build the container:

    docker build -t discord-bot .

Create a Discord Bot and generate its token. Pass that into the container at runtime:

    docker run -it -e TOKEN="ODMxxxxxxxxxxxxxx0.YxxxxxxQ.Nxxxxxxxxxxxxxxxxxxxxxxx" discord-bot

To launch your bot and keep it alive, you'll need the services of a container orchestrator:

- AWS Lightsail / ECS / EC2, etc.
- Kubernetes
- DCOS