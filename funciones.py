from math import factorial
import sympy as sp
import numpy as np

def taylor(f,x0,n):
    x = sp.symbols('x')
    p = 0
    for k in range(0,n+1):
        df    = sp.diff(f,x,k)
        df_x0 = df.evalf(subs={x:x0})
        T     = (df_x0*(x-x0)**k)/factorial(k)
        p     = p+T
    return p

def Newton(f,x0,tol):
  x = sp.symbols('x')
  df = sp.diff(f,x)
  N = x - f/df
  N = sp.lambdify(x,N)
  x1 = N(x0)

  while(np.abs(x1-x0)>tol):
    x0 = x1
    x1 = N(x0)

  
  return x1

def Biseccion(f,a,b,tol):

  if (f(a) * f(b) > 0):
    msg = 'La función no cumple el teorema en el intervalo'
    return msg

  else:
    contador = 0
    while(np.abs(b-a) > tol):
      c= (a+b)/2
      if (f(a) * f(c) < 0):
        b = c
      else:
        a = c
      contador += 1

    
  return c

def Pos_falsa(f,a,b,tol):

  if (f(a) * f(b) > 0):
    msg = 'La función no cumple el teorema en el intervalo, busque otro intervalo'
    return msg

  else:
    c = a - (f(a)*(a-b))/(f(a)-f(b))
    while(np.abs(f(c)) > tol):
      c = a - (f(a)*(a-b))/(f(a)-f(b))
      if (f(a) * f(c) < 0):
        b = c
      else:
        a = c
  return c

def Secante(f,x0,x1,tol):
  x2 = x1 - f(x1)*(x0-x1)/(f(x0)-f(x1))
  while(np.abs(x2-x1)>tol):
    x0 = x1
    x1 = x2
    x2 = x1-f(x1)*(x0-x1)/(f(x0)-f(x1))
  return x2

def lagrange(xdata,ydata):
  X = sp.symbols('X')
  N = len(xdata)
  P = 0
  for i in range(N):
    T = 1
    for j in range(N):
      if j != i:
        T = T*(X-xdata[j]) / (xdata[i]- xdata[j])
      P = P+T*ydata[i]
  return P, sp.lambdify(X,P)

def p_simple(xdata,ydata):
  X = sp.symbols('X')
  N = len(xdata)
  M = np.zeros([N,N])
  P = 0
  for i in range(N):
    M[i,0] = 1
    for j in range(1,N):
      M[i,j] = M[i,j-1]*xdata[i]
  ai = np.linalg.solve(M,ydata)
  for i in range(1,N):
    P=P+ai[i]*X**i
  return P, sp.lambdify(X,P)

def mc(xd, yd, valor_a_interpolar):
    m = len(xd)
    sy = sum(yd)
    sx = sum(xd)
    sxy = sum(x * y for x, y in zip(xd, yd))
    dsx = sum(x ** 2 for x in xd)
    sx2 = sx ** 2

    # Calcular los coeficientes a0 y a1 de la recta y = a0 + a1 * x
    a0 = ((sy * dsx) - (sx * sxy)) / ((m * dsx) - sx2)
    a1 = ((m * sxy) - (sx * sy)) / ((m * dsx) - sx2)

    # Calcular el valor interpolado
    interpolated_value = a0 + a1 * valor_a_interpolar

    return interpolated_value, a0, a1


def Euler(f,a,b,h,co):
  n = int((b-a)/h)
  t = np.linspace(a,b,n+1)
  yeu = [co]
  for i in range(n):
    yeu.append(yeu[i]+h*f(t[i],yeu[i]))
  return t, yeu

#Runge-Kuta
def Runge4(f,a,b,h,co):
  n = int((b-a)/h)
  t = np.linspace(a,b,n+1)
  yk = [co]
  for i in range(n):
    k1 = h*f(t[i],yk[i])
    k2 = h*f(t[i]+h/2,yk[i]+1/2*k1)
    k3 = h*f(t[i]+h/2, yk[i]+ 1/2*k2)
    k4 = h*f(t[i+1], yk[i]+k3)
    yk.append(yk[i]+1/6*(k1+2*k2+2*k3+k4))
  return t,yk