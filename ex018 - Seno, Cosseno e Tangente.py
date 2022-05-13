import math
ângulo=float(input('Digite o ângulo que você deseja: '))
seno=math.sin(math.radians(ângulo))
cos=math.cos(math.radians(ângulo))
tang=math.tan(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tang))
