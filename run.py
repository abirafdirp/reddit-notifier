from bot import Bot
from emailhandler import EmailHandler

Bot.validate()
EmailHandler.register()
bot = Bot()
bot.run()
