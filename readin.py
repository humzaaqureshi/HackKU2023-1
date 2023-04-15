"Yaeesh Mukadam and Humza Q"
from PIL import Image
from pytesseract import pytesseract
from readreceipt import ConvertImage

class READIN:
    def __init__(self):
        self.receipt_text = ConvertImage("walmartreceipt.jpg")
        self.receipt = self.receipt_text.return_text()
        self.itemized_information = self.receipt.split()


    def all_information(self):
        print(self.text)

    def print_all_info_into_a_list(self):
        print(self.itemized_information)

    def findtotal(self):
        index = self.itemized_information.index("TOTAL")
        try:
            total = float(self.itemized_information[index + 1])
            print(total)
        except ValueError:
            self.itemized_information.pop(index)
            self.findtotal()




    
