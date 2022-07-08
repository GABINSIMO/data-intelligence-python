#esercizio sull'ereditarieta

class Crealista():
 lista=[]
 nome ='nome'
 cognome='cognome'
 eta=12
 lavoro='lavoro'

persona = Crealista()

persona.nome= input ('inserire il nome')
if(type(persona.nome)==str):
 persona.lista.append(persona.nome)

persona.cognome= input ('inserire il cognome') 
if(type(persona.cognome)==str):
 persona.lista.append(persona.cognome)

persona.eta= input ('inserire eta')
if(int(persona.eta)):
 persona.lista.append(persona.eta)

persona.nome= input ('inserire il lavoro')
if(type(persona.nome)==str):
 persona.lista.append(persona.lavoro)

print(persona.lista)

