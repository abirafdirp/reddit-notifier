from bot import Bot
from emailhandler import EmailHandler

EmailHandler.register()
bot = Bot()
bot.validate()
bot.run()
