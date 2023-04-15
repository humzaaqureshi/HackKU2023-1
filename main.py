

from readin import READIN
def main():


    try:
        filename = input("Enter a filename: ")
        read = READIN(filename)
        read.run()
    except FileNotFoundError:
        print("File does not exist. Ending Program")

    # Executive class


if __name__ == "__main__":
   main()
