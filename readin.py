
"Humza Qureshi and yaeesh mukadam"
from PIL import Image
from pytesseract import pytesseract
from covertpicture import ConvertImage
import sqlite3

class READIN:
    def __init__(self, filename):
        self.receipt_text = ConvertImage(filename)
        self.receipt = self.receipt_text.return_text()
        self.itemized_information = self.receipt.split()
        self.total = 0
        self.conn = sqlite3.connect("Receipts.db")
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS receipts (Amount real)""")

    def findtotal(self):
        index = self.itemized_information.index("TOTAL")
        try:
            self.total = float(self.itemized_information[index + 1])
        except ValueError:
            self.itemized_information.pop(index)
            self.findtotal()

    def db_add(self): 
        params = self.total
        self.c.execute("INSERT INTO receipts VALUES (?)", (params,))

    def db_print(self):
        self.c.execute("SELECT * FROM receipts")
        items = self.c.fetchall()
        for ele in items:
            print(ele[0])
        self.conn.commit()

    def run(self):
        
        self.findtotal()

        self.db_add()

        self.db_print()







    
