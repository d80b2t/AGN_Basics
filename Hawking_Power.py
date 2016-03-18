'''

'''

## https://en.wikipedia.org/wiki/Hawking_radiation
## https://en.wikipedia.org/wiki/Planck_constant
## http://docs.scipy.org/doc/scipy/reference/constants.html
## http://blog.philippklaus.de/2011/08/physical-constants-in-python/

from scipy.constants import *
print "The Planck constant h:", h
print "The Avogadro constant N_A:", N_A
print "The muon mass in u:", physical_constants['muon mass in u']

#hbar = 1.054571800e-34
#c    = 2.997e8
#pi   = 3.14159265358979323

M = 1.

print hbar, c, M

## Stefan-Boltzmann-Schwarzschild-Hawking power law:
print "Stefan-Boltzmann-Schwarzschild-Hawking power law:"
print "hbar. c^6  /  (15360 . pi . G^2 . M^2) which is "
print hbar*(c**6)
print 15360.*pi*G*G*M*M
print (hbar*(c**6)) / ( 15360.*pi*G*G*M*M)
