from dataclasses import dataclass

from environs import Env

@dataclass
class TgBot:
	token: str #bot_token
	admin_ids: list[int] #admins list

@dataclass
class Config:
	tg_bot: TgBot

#func for read .env file and return Config class object with token and admin_ids
def load_config(path: str | None = None) -> Config:
	env = Env()
	env.read_env(path)
	return Config(tg_bot=TgBot(
		token=env('BOT_TOKEN'),
		admin_ids=list(map(int, env.list('ADMIN_IDS')))
	))