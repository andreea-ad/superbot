import datetime
import pytz

class BotLogger:
  def __init__(self):
    pass
  
  def error(self, message):
    self.log("ERROR", message)

  def warning(self, message):
    self.log("WARNING", message)

  def info(self, message):
    self.log("INFO", message)

  def log(self, type, message):
    timestamp = datetime.datetime.now(pytz.timezone("Europe/Bucharest"))
    pretty_timestamp = timestamp.strftime("%d-%b-%Y %H:%M:%S")
    print("[" + pretty_timestamp + "] " + type + ": " + message)
