from numpy import sqrt, array, arange, dot, cross
import matplotlib as plt

# mass of sun
mSun = 1.9891e30
# gravitational constant
G = -6.6738e-11

# acceleration function wrt distance
def accelerationG(R):
  r = sqrt(dot(R, R))
  ax = G*mSun / r**3 * R[0]
  ay = G*mSun / r**3 * R[1]
  # print acceleration coordinates
  return array([ax, ay], float)

# energy function wrt position + velocity
def Energy(R, V):
  r = sqrt(dot(R, R))
  PE = -G*mSun / r
  KE = -0.5*dot(V, V)
  return PE + KE

# one orbit of mercury in seconds
# converting one earth year in seconds
oneYear = 88.0 * 24.0 * 60.0 * 60.0
# number of steps per year per revolution
N = 88.0
h = oneYear/N
tpoints = arange(0.0, oneYear, h)

# position coordinates
xpoints = []
ypoints = []

# velocity coordinates
vxpoints = []
vypoints = []

# using NASA's planetary fact sheet of Mercury
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/
r = array([46.002e9, 0.0], float)
v = array([0.0, 58.98e3], float)

# adding position elements to list
xpoints.append(r[0])
ypoints.append(r[1])

# setting inital conditions
E_i = Energy(r, v)  # total energy
L_i = cross(r, v)   # angular momentum

# 100 orbits around Sun
for orbits in range(100):
  for t in tpoints:
    # use leap-frog algorithm and update velocity by half-time step
    v += h/2 * accelerationG(r)
    # then update position using half-step
    r += v*h
    # finally update velocity again with another half_step
    v += h/2 * accelerationG(r)

    # compute total energy
    E = Energy(r, v) / E_i
    L = cross(r, v)
    
    # plot with batch size=10
    if (orbits%10 == 0):
      print(E, L/L_i)
      xpoints.append(r[0])
      ypoints.append(r[1])
