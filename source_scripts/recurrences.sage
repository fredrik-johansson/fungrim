from ore_algebra import *
C.<z,nu> = PolynomialRing(QQ)
R.<x> = PolynomialRing(C)
A.<Dx> = OreAlgebra(R)

# 9b2f38, e85dee
Z = (z+x)**2*Dx**2 + (z+x)*Dx + ((z+x)**2 - nu**2)
Z.to_S(OreAlgebra(C['r'], 'Sr'))

# e233b0, 7377c8
Z = (z+x)**2*Dx**2 + (z+x)*Dx - ((z+x)**2 + nu**2)
Z.to_S(OreAlgebra(C['r'], 'Sr'))

