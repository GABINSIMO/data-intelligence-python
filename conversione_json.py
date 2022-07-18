import json

lista=[]
print("\n" "..............WELCOME..............")
x = input ("inserire un valore: ")
y = json.dumps(x)
lista.append(y)
insert = 1
while insert < 5:
    nuovo = int(input("vuoi inserire un'altro valore? " 
    "1.yes  " 
    "2.no   "  ))
    if ( nuovo == 1):
       x = input ("inserire un valore: ")
       y = json.dumps(x)
       lista.append(y)
       insert = insert + 1
    else:
        break

print (lista)
carica = 0
while carica <len(lista):
    position = int(input ("inserire la posizione del'elemento della lista da caricare: "))
    if (position < len(lista)):
        p = json.loads(lista[position])
        print (p)
    else:
        print ("ERROR 404")
    carica = carica +1 
    