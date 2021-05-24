from telegram.ext import *
import json
class TelegramBot():

    def __init__(self):

        # generate the update handler and dispatcher
        self.setup()

        # load user-defined commands iteratively
        self.load_commands()

        # load user-defined functions iteratively
        self.load_functions()

    def setup(self):
        
        with open("config.json", 'r') as file:
            cfg = json.load(file)

        self.updater = Updater(cfg["API KEY"])
        self.dp = self.updater.dispatcher
        
        # create dictionaries to store function pointers and their filters.
        self.commands = {}
        self.functions = {}

        self.commands["start_command"] = ["start", self.start_command]
        self.commands["help_command"]  = ["help", self.help_command]

        self.functions["custom_response"] = [Filters.text, self.custom_response]

    # load all functions
    def load_functions(self):
        for name, function in self.functions.items():
            filter = function[0]
            func   = function[1]
            self.dp.add_handler(MessageHandler(filter, func))
            print(f'added handler for function name: {name}')

    # load all commands
    def load_commands(self):
        for name, command in self.commands.items():
            cmd_name = command[0]
            cmd   = command[1]
            self.dp.add_handler(CommandHandler(cmd_name, cmd))
            print(f'added handler for command name: {name}')

    # in Telegram, commands begin with a /
    def start_command(self, updater, context):
        print("start command issued")
        updater.message.reply_text("Type something to get started!")

    def help_command(self, updater, context):
        updater.message.reply_text("You have requested the help page!")

    def custom_response(self, updater, context):
        print("custom_response")
        if updater.message.text in ("hello", "hi"):
            updater.message.reply_text("hello")
            return
        else:
            updater.message.reply_text("hmm?")

    def catch_error(self, updater, context):
        updater.message.reply_text("Didn't catch that")

    def run(self):
        print("Bot started...")
        self.updater.start_polling(1)
        self.updater.idle()

if __name__=='__main__':
    t = TelegramBot()
    t.run()