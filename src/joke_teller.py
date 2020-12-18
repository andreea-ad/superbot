import pyjokes

class JokeTeller:
  def __init__(self):
    self.joke = pyjokes.get_joke()
  
  def tell_joke(self):
    return self.joke