'''
Rectangle class for teaching Python.
'''

class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self, ):
        self.area = self.length*self.width
        print 'Area = %.4f' % self.area

    def calc_circ(self, ):
        self.circ = self.length*2 + self.width*2
        print 'Circumference = %.4f' % self.circ

