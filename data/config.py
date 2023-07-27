from environs import Env

# to activate Env
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
API_OPENAI = env.str("API_OPENAI")
API_SCAN = env.str("API_SCAN")