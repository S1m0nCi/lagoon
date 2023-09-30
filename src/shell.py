from lexer import Lexer

while True:
  text = input("Lagoon: ")
  tokeniser = Lexer(text)
  tokens = tokeniser.tokenise()

  print (tokens)