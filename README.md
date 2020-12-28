# superbot
---
## Set up the Docker container
Prerequisites:

* superbot repo cloned
* Discord bot created (check this: https://discordpy.readthedocs.io/en/latest/discord.html)
* docker installed (check with **docker** or **docker --version**)

In order to start your superbot, you need to follow several steps:
1. build a Docker image using the Dockerfile from this repo

```docker build -t <image_name> .```

**you can replace <image_name> with any image name you want** (e.g. docker build -t superbot_image)

2. create a Docker container with the built image

```docker run --env BOT_TOKEN=<your_bot_token> --detach --name <container_name> <image_name>```

**you can replace <container_name> and <image_name> with any names you want** (e.g. docker run -d --name superbot_container superbot_image)

**<your_bot_token> needs to be replaced with the bot token generated when you created your Discord bot** (check this: https://discord.com/developers/applications)

**IMPORTANT**: keep in mind that you need to use the same image name when running both **docker build** and **docker run** commands!
