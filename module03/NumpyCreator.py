import numpy

class NumpyCreator(object):
    '''Receives as an argument a different type of data structure and transforms it into
a Numpy array'''
    def from_list(self, lst):
        '''Takes a list or nested lists and returns its corresponding
Numpy array.'''
        result = []
        if isinstance(lst, list):
            for i in lst:
                result.append(i)
            print(result)
    def from_tuple(self, tpl): 
        '''Takes a tuple or nested tuples and returns its correspond-
ing Numpy array.'''
        if isinstance(tpl, tuple):
            result = []
            for i in tpl:
                result.append(i)
            print(result)
    def from_iterable(self, itr): 
        '''Takes an iterable and returns an array which contains
all its elements.'''
        result = []
        for i in itr:
            result.append(i)
        print(result)
    def from_shape(self, shape, value): #NE MARCHE PAS
        '''Returns an array filled with the same value. The first argument is a tuple which 
        specifies the shape of the array, and the second argument specifies the value of the 
        elements. This value must be 0 by default.'''
        if value == None:
            value = 0
        result = []
        # for i in shape[0]:
        #     i = value
        #     result.append(i)
        # for j in shape[1]:
        #     j = value
        #     result.append(j)
        numpy.arange(shape[0] * shape[1]).reshape(shape)
        print(result)
    def random(self, shape): 
        '''Returns an array filled with random values. It takes as an
argument a tuple which specifies the shape of the array.'''
    def identity(self, n): 
        '''Returns an array representing the identity matrix of size n.'''