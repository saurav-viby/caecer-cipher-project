alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=['1','2','3']

from cipher_art import logo
print(logo)
def ceacer (ctext,cshift,cdirection):
  final_text=""
  if cdirection=="decode":
    cshift*=-1
  for letter in ctext:
      if letter in alphabet:
        pos=alphabet.index(letter)
        newpos=pos+cshift
        final_text+=alphabet[newpos]
      else:
        final_text+=letter
  print(f"Here is the {cdirection}d result {final_text}")
true=True
while true:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction== "encode" or direction=="decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
  else:
    print ("invalid")
    exit()
  ceacer(ctext=text,cdirection=direction,cshift=shift)
  cont=input("do you want to start again(yes/No)=").lower()
  if cont=="no":
    true=False


    
