class Reader:
    """This class have methods that
    reads strings from different types of
    measurements and stores them into lists.
    """
    def __init__(self, filename, filepath = str()):
        self.filename = filename
        self.filepath = filepath
        self.idata = []
    #    self.data = []

    def readIV(self):
        """This method is tuned to IV data"""
        with open(self.filepath + self.filename) as file:
            properties = file.readline()
            properties = properties.split()
            lines = file.readlines()
            v = []
            i = []
            for line in lines:
                v.append(float(line.split()[0]))
                i.append(float(line.split()[1]))
        self.idata.append(v)
        self.idata.append(i)
        return v,i

    def __str__(self):
        """This special method previews the first and the last stored current values
        by printing the initiated object of this class. This is made to give an
        idea if the file is the correct one
        """
        return f"The first and the last Current values measure are: {self.idata[1][0]} and {self.idata[1][-1]}"
    
    def __add__(self, other):
        """returns combined data """
        combined = [self.idata[0] + other.idata[0], self.idata[1] + other.idata[1]]
        return combined


if __name__ == "__main__":
    filename = "IVSample.txt"
    filepath = "C:\\Users\\danie\\Desktop\\USB SERGEY\\Daniil\\22.02.23  Devices after aluminium contacts\\500C1\\"
    Test = Reader(filename,filepath)
    Test.readIV()
    print(Test)
    a = ['a0','b0']
    b = ['a','b']
    print(a+b,type(a+b))

