======================
nudged\ :sup:`0.2.0`
======================

A Python lib to estimate scale, rotation, and translation between two sets of 2D points. Applicable for example in cases where one wants to move objects by multiple fingers or where a large number of points from an eye tracker device are wanted to be corrected based on a few calibration points. In general, you can apply nudged in any situation where you want to move a number of points based on a few sample points.

.. image:: ../master/doc/nudged-logo.png?raw=true
   :alt: Example transformation
   :height: 353px
   :width: 300px

Mathematically speaking, nudged is an optimal least squares estimator for `affine transformation matrices
<https://en.wikipedia.org/wiki/Affine_transformation>`_ with uniform scaling, rotation, and translation and without reflection or shearing. The estimation has time complexity of O(*n*) that consists of 6*n*+22 multiplications and 11*n*+19 additions, where *n* is the cardinality (size) of the point sets. In other words, nudged solves an affine 2D to 2D point set registration problem in linear time.



Install
=======

``$ pip install nudged``



Usage
=====

You have lists of points for the **domain** and **range** of the tranformation function to be estimated::

    dom = [[0,0], [2,0], [ 1,2]]
    ran  = [[1,1], [1,3], [-1,2]]

Compute optimal tranformation based on the points::

    trans = nudged.estimate(dom, ran);

Apply the transformation to other points::

    trans.transform([2,2])
    # [-1,3]

To explore the estimated transformation, you can::

    trans.get_matrix()
    # [[0,-1, 1],
    #  [1, 0, 1],
    #  [0, 0, 1]]

    trans.get_rotation()
    # 1.5707... = π / 2   (radians)

    trans.get_scale()
    # 1.0

    trans.get_translation()
    # [1, 1]



API
===


nudged.estimate(dom, ran)
------------------------------------------


**Parameters**

- *dom*, domain, list of [x,y] points
- *ran*, range, list of [x,y] points

The *dom* and *ran* should have equal length. Different lengths are allowed but additional points in the longer list are ignored in the estimation.

**Return** a new *nudged.Transform(...)* instance.


nudged.version
--------------

Contains the module version string equal to the version in *setup.py*.


nudged.Transform(s, r, tx, ty)
------------------------------

An instance returned by the *nudged.estimate(...)*.

In addition to the methods below, it has attributes *s*, *r*, *tx*, *ty* that define the `augmented transformation matrix
<https://en.wikipedia.org/wiki/Affine_transformation#Augmented_matrix>`_::

    |s  -r  tx|
    |r   s  ty|
    |0   0   1|

nudged.Transform#transform(points)
..................................

**Return** an list of transformed points or single point if only a point was given. For example::

    trans.transform([1,1])           # [2,2]
    trans.transform([[1,1]])         # [[2,2]]
    trans.transform([[1,1], [2,3]])  # [[2,2], [3,4]]

nudged.Transform#get_matrix()
.............................

**Return** an 3x3 augmented transformation matrix in the following list format::

    [[s,-r, tx],
     [r, s, ty],
     [0, 0,  1]]

nudged.Transform#get_rotation()
...............................

**Return** rotation in radians.

nudged.Transform#get_scale()
............................

**Return** scaling multiplier, e.g. ``0.333`` for a threefold shrink.

nudged.Transform#get_translation()
..................................

**Return** ``[tx, ty]`` where ``tx`` and ``ty`` denotes movement along x-axis and y-axis accordingly.



For developers
==============

Run unit tests::

    $ python setup.py test



Versioning
==========

`Semantic Versioning 2.0.0
<http://semver.org/>`_



License
=======

`MIT License
<http://github.com/axelpale/nudged-py/blob/master/LICENSE>`_
