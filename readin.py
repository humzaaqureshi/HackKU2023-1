"yaeesh mukadam"
from PIL import Image
from pytesseract import pytesseract

class READIN:
    def __init__(self, filename):
        self.filename = filename 
        self.img = Image.open(self.filename)
        self.text = pytesseract.image_to_string(self.img)
        self.itemized_information = self.text.split()


    def all_information(self):
        print(self.text)

    def print_all_info_into_a_list(self):
        print(self.itemized_information)

    def findtotal(self):
        count = 0
        for word in self.itemized_information:
            if word.lower() == "the":
                count = count + 1

        return count

demo = READIN("testpic.png")
print(demo.findtotal())




    
