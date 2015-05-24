import numpy as np
from scipy import special

#define sine integral -pi/2
def sine_integral_func(x):
    tmp = special.sici(x)
    tmp2 = -np.pi/2.0 + tmp[0]
    return tmp2

#construct sine integral over range 0<x<2*pi
x = np.arange(0.0,2.0*np.pi,0.01)
y = []
[y.append(sine_integral_func(i)) for i in x]

#save the x and y vectors to a file
save_list = [x,y]
np.savetxt('example_data/root_finding_unknown_function.txt',save_list)


