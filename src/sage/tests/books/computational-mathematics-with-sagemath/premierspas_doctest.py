# sage_setup: distribution = sagemath-repl
## -*- encoding: utf-8 -*-
"""
This file (./premierspas_doctest.sage) was *autogenerated* from ./premierspas.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./premierspas_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./premierspas.tex, line 589::

  sage: 1+1
  2

Sage example in ./premierspas.tex, line 645::

  sage: ( 1 + 2 * (3 + 5) ) * 2
  34

Sage example in ./premierspas.tex, line 656::

  sage: 2^3
  8
  sage: 2**3
  8

Sage example in ./premierspas.tex, line 664::

  sage: 20/6
  10/3

Sage example in ./premierspas.tex, line 700::

  sage: 20.0 / 14
  1.42857142857143

Sage example in ./premierspas.tex, line 724::

  sage: numerical_approx(20/14, digits=60)
  1.42857142857142857142857142857142857142857142857142857142857

Sage example in ./premierspas.tex, line 792::

  sage: 20 // 6
  3
  sage: 20 % 6
  2

Sage example in ./premierspas.tex, line 818::

  sage: factor(2^(2^5)+1)
  641 * 6700417

Sage example in ./premierspas.tex, line 952::

  sage: sin(pi)
  0
  sage: tan(pi/3)
  sqrt(3)
  sage: arctan(1)
  1/4*pi
  sage: exp(2 * I * pi)
  1

Sage example in ./premierspas.tex, line 967::

  sage: arccos(sin(pi/3))
  arccos(1/2*sqrt(3))
  sage: sqrt(2)
  sqrt(2)
  sage: exp(I*pi/7)
  e^(1/7*I*pi)

Sage example in ./premierspas.tex, line 987::

  sage: simplify(arccos(sin(pi/3)))
  1/6*pi

Sage example in ./premierspas.tex, line 1000::

  sage: numerical_approx(6*arccos(sin(pi/3)), digits=60)
  3.14159265358979323846264338327950288419716939937510582097494
  sage: numerical_approx(sqrt(2), digits=60)
  1.41421356237309504880168872420969807856967187537694807317668

Sage example in ./premierspas.tex, line 1139::

  sage: y = 1 + 2

Sage example in ./premierspas.tex, line 1144::

  sage: y
  3
  sage: (2 + y) * y
  15

Sage example in ./premierspas.tex, line 1156::

  sage: y = 1 + 2; y
  3

Sage example in ./premierspas.tex, line 1168::

  sage: y = 3 * y + 1; y
  10
  sage: y = 3 * y + 1; y
  31
  sage: y = 3 * y + 1; y
  94

Sage example in ./premierspas.tex, line 1208::

  sage: pi = -I/2
  sage: exp(2*I*pi)
  e

Sage example in ./premierspas.tex, line 1217::

  sage: from sage.symbolic.constants import pi

Sage example in ./premierspas.tex, line 1224::

  sage: restore()

Sage example in ./premierspas.tex, line 1267::

  sage: z = SR.var('z')
  sage: 2*z + 3
  2*z + 3

Sage example in ./premierspas.tex, line 1290::

  sage: y = SR.var('z')
  sage: 2*y + 3
  2*z + 3

Sage example in ./premierspas.tex, line 1306::

  sage: c = 2 * y + 3
  sage: z = 1
  sage: 2*y + 3
  2*z + 3
  sage: c
  2*z + 3

Sage example in ./premierspas.tex, line 1318::

  sage: x = SR.var('x')
  sage: expr = sin(x); expr
  sin(x)
  sage: expr(x=1)
  sin(1)

Sage example in ./premierspas.tex, line 1332::

  sage: u = SR.var('u')
  sage: u = u+1
  sage: u = u+1
  sage: u
  u + 2

Sage example in ./premierspas.tex, line 1347::

  sage: x = SR.var('x', 100)
  sage: (x[0] + x[1])*x[99]
  (x0 + x1)*x99

Sage example in ./premierspas.tex, line 1357::

  sage: var('a, b, c, x, y')
  (a, b, c, x, y)
  sage: a * x + b * y + c
  a*x + b*y + c

Sage example in ./premierspas.tex, line 1380::

  sage: var('bla')
  bla

"""
