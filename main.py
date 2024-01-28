from FileReader import *

if __name__ == "__main__":
    filename = "IVSample.txt"
    filepath = "C:\\Users\\danie\\Desktop\\USB SERGEY\\Daniil\\22.02.23  Devices after aluminium contacts\\500C1\\"
    Test = Reader(filename, filepath)
    Test.readIV()
    print(Test)