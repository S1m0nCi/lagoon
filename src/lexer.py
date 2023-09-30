class Lexer():
  digits = "0123456789"
  operations = "+-/*"

  def __init__(self, text):
    self.text = text
    self.code = text.split(' ')
    self.index = 0
    self.tokens = []
    self.token = None
    self.char = self.text

  def tokenise(self):
    # we should split by spaces as separators: the code input will be in string form
    while self.index < len(self.text):
      # we can use a token class to convert to a token first
      if self.char in Lexer.digits:
        self.token = self.extract_number()
      
      elif self.char in Lexer.operations:
        self.token = Operation(self.char)
        self.move()
      self.tokens.append(self.token)

    return self.tokens

  def extract_number(self):
    isFloat = False
    number = ""
    while (self.char in Lexer.digits + '.') and (self.index in len(self.text)):
      if self.char == '.':
        isFloat = True
      number += self.char
      self.move()

    return Integer(number) if not isFloat else Float(number)
  
  def move(self):
    self.index += 1
    if self.index < len(self.text):
      self.char = self.text(self.index)


class Token():
  def __init__(self, type, value):
    self.type = type
    self.value = value

class Integer(Token):
  def __init__(self, value):
    super().__init__("INT", value)

class String(Token):
  def __init__(self, value):
    super().__init__("STR", value)
  
  @staticmethod
  def concatenate(string1, string2):
    return String(string1.value + string2.value)

class Float(Token):
  def __init__(self, value):
    super().__init__("FLT", value)

class Operation(Token):
  def __init__(self, value):
    super().__init__("OPR", value)