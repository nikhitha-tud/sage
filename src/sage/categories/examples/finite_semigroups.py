"""
Examples of finite semigroups
"""
#*****************************************************************************
#  Copyright (C) 2008-2009 Nicolas M. Thiery <nthiery at users.sf.net>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#******************************************************************************

from sage.misc.cachefunc import cached_method
from sage.sets.family import Family
from sage.categories.semigroups import Semigroups
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.element_wrapper import ElementWrapper


class LeftRegularBand(UniqueRepresentation, Parent):
    r"""
    An example of a finite semigroup

    This class provides a minimal implementation of a finite semigroup.

    EXAMPLES::

        sage: S = FiniteSemigroups().example(); S
        An example of a finite semigroup: the left regular band generated by ('a', 'b', 'c', 'd')

    This is the semigroup generated by::

        sage: S.semigroup_generators()
        Family ('a', 'b', 'c', 'd')

    such that `x^2 = x` and `x y x = xy` for any `x` and `y` in `S`::

        sage: S('dab')
        'dab'
        sage: S('dab') * S('acb')
        'dabc'

    It follows that the elements of `S` are strings without
    repetitions over the alphabet `a`, `b`, `c`, `d`::

        sage: sorted(S.list())
        ['a', 'ab', 'abc', 'abcd', 'abd', 'abdc', 'ac', 'acb', 'acbd', 'acd',
         'acdb', 'ad', 'adb', 'adbc', 'adc', 'adcb', 'b', 'ba', 'bac',
         'bacd', 'bad', 'badc', 'bc', 'bca', 'bcad', 'bcd', 'bcda', 'bd',
         'bda', 'bdac', 'bdc', 'bdca', 'c', 'ca', 'cab', 'cabd', 'cad',
         'cadb', 'cb', 'cba', 'cbad', 'cbd', 'cbda', 'cd', 'cda', 'cdab',
         'cdb', 'cdba', 'd', 'da', 'dab', 'dabc', 'dac', 'dacb', 'db',
         'dba', 'dbac', 'dbc', 'dbca', 'dc', 'dca', 'dcab', 'dcb', 'dcba']

    It also follows that there are finitely many of them::

        sage: S.cardinality()
        64

    Indeed::

        sage: 4 * ( 1 + 3 * (1 + 2 * (1 + 1)))
        64

    As expected, all the elements of `S` are idempotents::

        sage: all( x.is_idempotent() for x in S )
        True

    Now, let us look at the structure of the semigroup::

        sage: S = FiniteSemigroups().example(alphabet = ('a','b','c'))
        sage: S.cayley_graph(side="left", simple=True).plot()
        Graphics object consisting of 60 graphics primitives
        sage: S.j_transversal_of_idempotents() # random (arbitrary choice)
        ['acb', 'ac', 'ab', 'bc', 'a', 'c', 'b']

    We conclude by running systematic tests on this semigroup::

        sage: TestSuite(S).run(verbose = True)
        running ._test_an_element() . . . pass
        running ._test_associativity() . . . pass
        running ._test_cardinality() . . . pass
        running ._test_category() . . . pass
        running ._test_construction() . . . pass
        running ._test_elements() . . .
          Running the test suite of self.an_element()
          running ._test_category() . . . pass
          running ._test_eq() . . . pass
          running ._test_new() . . . pass
          running ._test_not_implemented_methods() . . . pass
          running ._test_pickling() . . . pass
          pass
        running ._test_elements_eq_reflexive() . . . pass
        running ._test_elements_eq_symmetric() . . . pass
        running ._test_elements_eq_transitive() . . . pass
        running ._test_elements_neq() . . . pass
        running ._test_enumerated_set_contains() . . . pass
        running ._test_enumerated_set_iter_cardinality() . . . pass
        running ._test_enumerated_set_iter_list() . . . pass
        running ._test_eq() . . . pass
        running ._test_new() . . . pass
        running ._test_not_implemented_methods() . . . pass
        running ._test_pickling() . . . pass
        running ._test_some_elements() . . . pass
    """

    def __init__(self, alphabet=('a','b','c','d')):
        r"""
        A left regular band.

        EXAMPLES::

            sage: S = FiniteSemigroups().example(); S
            An example of a finite semigroup: the left regular band generated by ('a', 'b', 'c', 'd')
            sage: S = FiniteSemigroups().example(alphabet=('x','y')); S
            An example of a finite semigroup: the left regular band generated by ('x', 'y')
            sage: TestSuite(S).run()
        """
        self.alphabet = alphabet
        Parent.__init__(self,
                        category=Semigroups().Finite().FinitelyGenerated())

    def _repr_(self):
        r"""
        TESTS::

            sage: S = FiniteSemigroups().example()
            sage: S._repr_()
            "An example of a finite semigroup: the left regular band generated by ('a', 'b', 'c', 'd')"
        """
        return "An example of a finite semigroup: the left regular band generated by %s"%(self.alphabet,)

    def product(self, x, y):
        r"""
        Returns the product of two elements of the semigroup.

        EXAMPLES::

            sage: S = FiniteSemigroups().example()
            sage: S('a') * S('b')
            'ab'
            sage: S('a') * S('b') * S('a')
            'ab'
            sage: S('a') * S('a')
            'a'

        """
        assert x in self
        assert y in self
        x = x.value
        y = y.value
        return self(x + ''.join(c for c in y if c not in x))

    @cached_method
    def semigroup_generators(self):
        r"""
        Returns the generators of the semigroup.

        EXAMPLES::

            sage: S = FiniteSemigroups().example(alphabet=('x','y'))
            sage: S.semigroup_generators()
            Family ('x', 'y')

        """
        return Family([self(i) for i in self.alphabet])

    def an_element(self):
        r"""
        Returns an element of the semigroup.

        EXAMPLES::

            sage: S = FiniteSemigroups().example()
            sage: S.an_element()
            'cdab'

            sage: S = FiniteSemigroups().example(("b"))
            sage: S.an_element()
            'b'
        """

        return self(''.join(self.alphabet[2:]+self.alphabet[0:2]))

    class Element (ElementWrapper):
        wrapped_class = str
        __lt__ = ElementWrapper._lt_by_value

Example = LeftRegularBand
