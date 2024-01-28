from FileReader import *
from Plotter import *
from DataAnalyzer import *

if __name__ == "__main__":
    filename = "diode_6_forward_500um.txt"
    filepath = "C:\\Users\\danie\\Desktop\\USB SERGEY\\Daniil\\20230213_device_from_Victor\\diode_6_0.5mm\\"
    test1 = Reader(filename, filepath)
    V,I = test1.readIV()
    IV_analyze = IVDataAnalyzer(V,I)
    I_log = IV_analyze.log_transform()
    test_plot = Plotter(V,I,"Volt","Ampere","Testplot","current as a function of volt")
    test_plot1 = Plotter(V, I_log, "Volt", "Log(Ampere)", "Testplot", "log current as a function of log")
    test_plot.plot_data()
    test_plot1.plot_data()

    #print(firstplot)