class poly():
    def __init__(self, coeff=[]):
        if isinstance(coeff, int) or isinstance(coeff, float):
            coeff = [coeff]
        self.coeff = np.array(coeff)
        self.order = len(coeff)
    
    def evaluate(self, x):
        result = 0.0
        for i in xrange(len(self)):
            result += self.coeff[i] * x**i
        return result
    
    def __len__(self):
        return self.order

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return poly(self.coeff * other)
        return poly(np.convolve(self.coeff, other.coeff))

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.coeffs[0] += num
            return self
        result = []
        diff = len(self) - len(other)
        if diff == 0:
            result = self.coeff + other.coeff
        elif diff > 0:
            result = self.coeff + np.concatenate((np.zeros(abs(diff)), other.coeff))
        else:
            result = np.concatenate((np.zeros(abs(diff)), self.coeff)) + other.coeff
        return poly(result)
