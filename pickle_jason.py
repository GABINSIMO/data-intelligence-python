import pickle
import pprint
import json

lista1 = ({"a":11, "b":24, "c":11})
lista2 = "siamo la classe migliore di "

#json
mess1j = json.dumps(lista1)
mess2j = json.dumps(lista1)
#pickle
mess1p = pickle.dumps(lista2)
mess2p = pickle.dumps(lista2)


print("................CONVERTITORE....................")

while True:
    scelta = int (input("1 per json e 2 per pickle\n"))
    if scelta == 1:
        mess1j = json.loads(mess1j)
        print (mess1j)
        mess1j["c"]= int (input ("inserire il valore\n"))
        newMESS1j = json.dumps(mess1j)
        print (newMESS1j)

        mess2j= json.loads(mess2j)
        print (mess2j) 
        mess2j = mess2j + "security"
        newMESS2j = json.dumps(mess2j)
        print (newMESS2j)

    elif scelta == 2:
        mess1p = pickle.loads(mess1p)
        print (mess1p)
        mess1p["c"]= int (input ("inserire il valore"))
        newMESS1p = pickle.dumps(mess1p)
        print (newMESS1p)

        mess2p= pickle.loads(mess2p)
        print (mess2p) 
        mess2p = mess2p + "security"
        newMESS2p = pickle.dumps(mess2p)
        print (newMESS2p)

    




   

    