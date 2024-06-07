from generate_numbers.i_generator import INumberGenerator
import numpy
class GenerateUniform(INumberGenerator):

    def generate_numbers(self, min_num, max_num, size):
        numbers = abs(numpy.random.uniform(low=min_num, high=max_num, size=size))
        rounded_numbers = numpy.round(numbers).astype(int)
        return rounded_numbers