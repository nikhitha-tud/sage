# sage_setup: distribution = sagemath-repl
## -*- encoding: utf-8 -*-
"""
This file (./sol/domaines_doctest.sage) was *autogenerated* from ./sol/domaines.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./sol/domaines_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./sol/domaines.tex, line 4::

  sage: def ndigits(x): return x.ndigits()
  sage: o = 720; ndigits(o)
  3

Sage example in ./sol/domaines.tex, line 28::

  sage: a = Reals(17)(pi); b = Reals(42)(pi)
  sage: type(a) == type(b)
  True
  sage: parent(a), parent(b)
  (Real Field with 17 bits of precision, Real Field with 42 bits of precision)

Sage example in ./sol/domaines.tex, line 46::

  sage: a = 0.1; b = 0.1*1
  sage: type(a), type(b)
  (<... 'sage.rings.real_mpfr.RealLiteral'>, <... 'sage.rings.real_mpfr.RealNumber'>)
  sage: parent(a) == parent(b)
  True

Sage example in ./sol/domaines.tex, line 70::

  sage: Reals(100)(a)-1/10
  0.00000000000000000000000000000
  sage: Reals(100)(b)-1/10
  5.5511151231257629805955278152e-18

Sage example in ./sol/domaines.tex, line 80::

  sage: E = CombinatorialFreeModule(QQ, [1,2,3])
  sage: H = Hom(E,E); H.rename("H")
  sage: C = E.category(); C
  Category of finite dimensional vector spaces with basis over Rational Field
  sage: phi1 = E.module_morphism(on_basis=lambda i: E.term(i), codomain=E)
  sage: phi2 = E.module_morphism(on_basis=lambda i: E.term(i),
  ....:                          triangular="lower", codomain=E)
  sage: phi3 = E.module_morphism(diagonal=lambda i: 1, codomain=E,
  ....:                          category=C)
  sage: phi1.parent() == phi2.parent() == phi3.parent() == H
  True
  sage: type(phi1)
  <class 'sage.modules.with_basis.morphism.ModuleMorphismByLinearity_with_category'>
  sage: type(phi2)
  <class 'sage.modules.with_basis.morphism.TriangularModuleMorphismByLinearity_with_category'>
  sage: type(phi3)
  <class 'sage.modules.with_basis.morphism.DiagonalModuleMorphism_with_category'>

"""
