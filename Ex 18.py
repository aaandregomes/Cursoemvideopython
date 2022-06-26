'''import math
oposto = float(input('O:'))
adjasente = float(input('A:'))
angulo = float(input('Angulo:'))
h = (adjasente/math.cos(math.radians(angulo)))
h2 = (oposto/math.sin(math.radians(angulo)))
print('O valor da hipotenusa é {:.3f} '.format(h))'''

import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.3f}'.format(\033m[4;33mhi))

