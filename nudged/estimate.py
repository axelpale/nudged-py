# -*- coding: utf-8 -*-

from transform import Transform

def estimate(domainpoints, rangepoints):
    '''
    Parameters
        domainpoints
            list of [x, y] 2D lists
        rangepoints
            list of [x, y] 2D lists
    '''

    # Alias
    X = domainpoints
    Y = rangepoints

    # Allow arrays of different length but
    # ignore the extra points.
    N = min(len(X), len(Y))

    a1 = b1 = c1 = d1 = 0
    a2 = b2 = 0
    ad = bc = ac = bd = 0
    for x, y in zip(X, Y): TODO min N restriction
        a = x[0]
        b = x[1]
        c = y[0]
        d = y[1]
        a1 += a
        b1 += b
        c1 += c
        d1 += d
        a2 += a * a
        b2 += b * b
        ad += a * d
        bc += b * c
        ac += a * c
        bd += b * d

    # Denominator.
    # It is zero iff X[i] = X[j] for every i and j in [0, n).
    # In other words, iff all the domain points are the same.
    den = N * a2 + N * b2 - a1 * a1 - b1 * b1

    TODO

    return Transform()
