DRY
---
Definition :footcite:p:`2019:thomas`
````````````````````````````````````
Maintenance is a constant part of programming. If we have duplicated knowledge within
our programs, they all need to be changed in case that knowledge changes (e.g. a new
requirement) -> maintenance nightmare.

.. admonition:: Definition
    :class: design_principle

    **Don't repeat yourself!**

    Each piece of knowledge must have a single, unambiguous, authoritative representation
    within a system.

This doesn't just mean code within a program should not be copy-pasted, but two pieces
of code must not duplicate *knowledge* or *intent*, even if done in two very different ways.

To test, if your code complies with the principle, see if a single facet of your code need
to be changed, does this change require changes at different places in the code as well.

Example :footcite:p:`dry_python`
````````````````````````````````
We want to calculate the BMI of five subjects:

.. literalinclude:: _code/dry_bad.py
    :language: python
    :linenos:

which produces the following output:

.. code-block:: none

    bmi subject1 = 30
    bmi subject2 = 29
    bmi subject3 = 29
    bmi subject4 = 24
    bmi subject5 = 28

First let's remove the duplication of calculating the BMI for various subjects:

.. literalinclude:: _code/dry_improved_1.py
    :language: python
    :linenos:

We moved the calculation in its own class, which saves us from explicitly defining
the calculation for each subject. If the calculation method changes, there is now
only one place (the *bmi_calc()* method) to adapt the code.

To improve it further, let's move the print statement to the function as well, since
it is duplicated for each subject:

.. literalinclude:: _code/dry_improved_2.py
    :language: python
    :linenos:

To improve it even more let's remove calling each subject individually and move them
all to a list and iterate over it:

.. literalinclude:: _code/dry_improved_3.py
    :language: python
    :linenos:

Duplication in Documentation
````````````````````````````
When adding a docstring to a function, don't explain the function in detail e.g. to
compensate for bad design and naming. The code should be readable, so that a docstring
must not repeat what is happening in the function.

Duplication in Data
```````````````````
The attributes of a class must not depend on each other in a way, that if one
data value changes, another attribute has to be manually adapted.

.. code-block:: python

    class Line {
        Point start;
        Point end;
        double length;
    }

This is a violation of DRY. The length derives from the ``start`` and ``end`` attributes.
If the start or the end Point changes, the length must change as well. It's better to make
length a function:

.. code-block::

    class Line {
        Point start;
        Point end;

        @property
        def double(self):
            return self.start.distance_to(self.end);
    }

.. footbibliography::