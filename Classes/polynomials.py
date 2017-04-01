class Polynomial(list):
    def __init__(self, *args):
        super(Polynomial, self).__init__(*args)
    def __add__(self, other):
        new_terms = []
        
        i = 0
        while i < max(len(self), len(other)):
            new_terms.append(self[i] + other[i])
            i += 1

        return Polynomial(new_terms)
    def __getitem__(self, key):
        if key < len(self):
            return super(Polynomial, self).__getitem__(key)
        else:
            return 0