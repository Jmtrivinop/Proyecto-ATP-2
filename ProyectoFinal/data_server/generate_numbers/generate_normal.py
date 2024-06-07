from generate_numbers.i_generator import INumberGenerator
import numpy
class GenerateNormal(INumberGenerator):

    def generate_numbers(self, min_num, max_num, size):
        loc = (min_num + max_num) / 2
        scale = abs(max_num - min_num) / 6 
        numbers = abs(numpy.random.normal(loc=loc, scale=scale, size=size))
        rounded_numbers = numpy.round(numbers).astype(int)
        return rounded_numbers