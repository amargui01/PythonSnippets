class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        """Addition of complex numbers."""
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        return ComplexNumber(real, imaginary)

    def __iadd__(self, other):
        """Addition with assignment (+=) for complex numbers."""
        self.real_part += other.real_part
        self.im_part += other.im_part
        return self

    def __eq__(self, other):
        """Compare two complex numbers for equality (==)."""
        return ((self.real_part == other.real_part) and
                (self.im_part == other.im_part))

z1 = ComplexNumber(1, 1)
z2 = ComplexNumber(-1, 2)
z3 = ComplexNumber(1,1)
# Arithmetic operations
z3 = z1 + z2
# Augmented assignment
z1 += z2




print(z3.real_part, z3.im_part)
print(z1.real_part, z1.im_part)
# Comparison operators
print(z1 == z3)




