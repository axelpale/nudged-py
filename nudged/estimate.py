# -*- coding: utf-8 -*-

from .transform import Transform

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

    a1 = b1 = c1 = d1 = 0.0
    a2 = b2 = 0.0
    ad = bc = ac = bd = 0.0
    for i in range(N):
        a = X[i][0]
        b = X[i][1]
        c = Y[i][0]
        d = Y[i][1]
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

    if abs(den) < 1e-8:
        # The domain points are the same.
        # We assume the translation to the mean of the range
        # to be the best guess. However if N=0, assume identity.
        if N == 0:
            return Transform(1.0, 0.0, 0.0, 0.0)
        else:
            return Transform(1.0, 0.0, (c1 / N) - a, (d1 / N) - b)

    # Estimators
    s = (N * (ac + bd) - a1 * c1 - b1 * d1) / den
    r = (N * (ad - bc) + b1 * c1 - a1 * d1) / den
    tx = (-a1 * (ac + bd) + b1 * (ad - bc) + a2 * c1 + b2 * c1) / den
    ty = (-b1 * (ac + bd) - a1 * (ad - bc) + a2 * d1 + b2 * d1) / den

    return Transform(s, r, tx, ty)
