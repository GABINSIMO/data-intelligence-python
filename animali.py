
class animale:
    def __init__ (self, zoo):
        self.ZOO= zoo

    def stampa(self):

        h = felino()
        i = canide()
        j = ucceli()


        self.name= input ("inserire il come dell'animale: ")
        self.type= int(input( """scelgliere il tipo :   
          1.felino         
          2.canide         
          3.ucceli       """))

        if self.type == 1:
         print('felino', self.name)
         h.__init__()
        if self.type == 2:
         print('canide', self.name)
         i.__init__()
        if self.type == 3:
         print('ucceli', self.name)
         j.__init__()
    

class felino(animale):
    def __init__(self):
       self.velocita = 50 
       print (self.velocita)

class canide(animale):
    def __init__(self):
        self.ganbe= 4
        print (self.ganbe)
        
class ucceli(animale):
    def __init__(self):
        self.ali= 2
        print(self.ali)


#main
X=animale('benvenuto dal veterinario')
X.stampa()


     

