import sqlite3 as sq

class DB():
    def __init__(self):
        self.connect = sq.connect('ID.db',check_same_thread=False)
        self.cursor = self.connect.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Id(User_Id INTEGER, User_Name TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Weight(Andrey_Weight REAL)''')
        self.cursor.execute('''INSERT INTO Weight(Andrey_Weight) VALUES (?)''',(1110.0,))
        self.connect.commit()
    
    def GetWeight(self):
        with self.connect:
            return (self.cursor.execute('''SELECT Andrey_Weight FROM Weight''').fetchone())[0]

    def GetUserId(self):
        with self.connect:
            return [i[0] for i in self.cursor.execute('''SELECT User_Id FROM Id''').fetchall()]

    def SwapWeight(self, NewWeight):
        with self.connect:
            self.cursor.execute('''UPDATE Weight SET Andrey_Weight = (?)''', (NewWeight,))

    def CheckUser(self,id):
        with self.connect:
            if self.cursor.execute('''SELECT User_Id FROM id WHERE User_Id = (?)''',(id,)).fetchone() is None:
                return False
            return True

    def AddUser(self,msg):
        with self.connect:
            self.cursor.execute('''INSERT INTO Id(User_Id, User_Name) VALUES (?,?)''',(msg.from_user.id,msg.from_user.full_name))

    def GetName(self, id):
        with self.connect:
            return self.cursor.execute('''SELECT User_Name FROM id WHERE User_Id = (?)''',(id,)).fetchone()[0]
    
    def DeleteUser(self,id):
        with self.connect:
            self.cursor.execute('''DELETE FROM Id WHERE User_Id = (?)''', (id,))