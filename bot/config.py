from pydantic import BaseSettings


class BotConfig(BaseSettings):
    token: str
