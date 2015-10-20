# -*- coding: utf-8 -*-
import math

class Transform(object):

    def __init__(self, s, r, tx, ty):
        # Public, to allow user access
        self.s = s
        self.r = r
        self.tx = tx
        self.ty = ty

    def transform(self, p):
        '''
        Parameter
            p
                point [x, y] or list of points [[x1,y1], [x2,y2], ...]
        '''
        def transform_one(q):
            return [self.s * q[0] - self.r * q[1] + self.tx,
                    self.r * q[0] + self.s * q[1] + self.ty]

        if not isinstance(p[0], list):
            # Single point
            return transform_one(p)
        # else
        return list(map(transform_one, p))

    def get_matrix(self):
        return [[self.s, -self.r, self.tx],
                [self.r,  self.s, self.ty],
                [     0,       0,       1]]

    def get_rotation(self):
        return math.atan2(self.r, self.s)

    def get_scale(self):
        return math.sqrt(self.r * self.r + self.s * self.s)

    def get_translation(self):
        return [self.tx, self.ty]
