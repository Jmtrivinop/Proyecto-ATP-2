from generate_numbers.i_generator import INumberGenerator

class MyApp:

    def run(self, number: INumberGenerator, min, max, range, test):
        if test:
           result = [1,2,3,4,5,6,7,8,9,10]
        else:
            result = number.generate_numbers(min, max, range)
            result = result.tolist()
        return result
    