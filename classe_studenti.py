#classe per studenti

class person():
    def _init_(self, fname, lname):
        self.firstname = fname
        self.lastname = lname



class docente(person):
    #se voglio agguingere un altro campo per studente posso fare una altro init
    def _init_(self, fname, lname, year):
        person._init_(self, fname, lname)
        self.my_year=year

    def printname (self):
        print (self.firstname, self.lastname, self.my_year)
   

class studente(docente):
    def _int_(self, fname, lname, year, media):
        docente._init_(self,fname, lname, year)
        self.average= media

    def printname (self):
        print (self.firstname, self.lastname, self.my_year, self.average)
    
  
