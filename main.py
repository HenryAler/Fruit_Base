import sqlite3


class Base():

    def __init__(self):

        self.connection = sqlite3.connect('base.db')
        self.cursor = self.connection.cursor()

        try:
            self.cursor.execute('CREATE TABLE product(name, color, count, weight)')

        except sqlite3.OperationalError:
            pass
        
    def add_to_base(self):

        values_base = self.cursor.execute('SELECT name FROM product').fetchall()

        for i in values_base:

            if self.name in i[0]:

                print('есть такое')
                return
        
        self.cursor.execute("""
                            INSERT INTO product VALUES
                            (?, ?, ?, ?)
                            """, [self.name, self.color, self.count, self.weight])
        self.connection.commit()


class Product(Base):

    def __init__(self, name:str, color:str, count:int, weight:float) -> None:

        super().__init__()

        self.name = name
        self.color = color
        self.count = count
        self.weight = weight

    


pomidor = Product('Помидор', 'красный', 12, 45)
print(pomidor.name)
pomidor.add_to_base()


