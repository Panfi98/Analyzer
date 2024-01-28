import numpy as np
class IVDataAnalyzer:
    def __init__(self, v = None, i = None, c = None, v_c= None):
        self.v = v
        self.i = i
        self.c = c
        self.v_c = v_c
    def log_transform(self):
        """transforms list/array to log values"""
        log_i = np.log10(self.i)
        return log_i
    def Cap_sq_in_tranform(self):
        """takes the square root and the inverse of capacitance"""
        C_sq_in = [1/(i**2) for i in self.C]
        return C_sq_in

    def get_Dr(self, eps=8.85e-14, eps_si=11.8, Areal=3.14e-3):
        """ Calculates deplition region"""
        D = [(eps*eps_si*Areal)/(i) for i in self.c]
        return D





