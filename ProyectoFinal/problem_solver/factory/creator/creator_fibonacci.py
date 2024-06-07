from factory.creator.i_problem_creator import  IProblemCreator
from factory.product.fibonacci import Fibonacci


class CreatorFibonacci(IProblemCreator):

    def factory_method(self):
        return Fibonacci()