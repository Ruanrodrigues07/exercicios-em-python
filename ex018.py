import math
angulo: float = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'
      '\nO ângulo de {} tem o COSSENO de {:.2f}'
      '\nO ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, seno,
                                                         angulo, cosseno,
                                                         angulo, tangente))
