alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1]

def InverterLetras(string):
  for i in range(len(string)):
    if (string[i].isupper()):
      str_hex = int(ord(string[i])) % 65
      print(alfabeto[str_hex])
    else:
      str_hex = int(ord(string[i])) % 97
      print(alfabeto[str_hex].lower())

InverterLetras("aAaAaAa")