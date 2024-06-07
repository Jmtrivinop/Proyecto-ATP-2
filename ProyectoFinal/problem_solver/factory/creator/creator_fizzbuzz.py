from factory.creator.i_problem_creator import  IProblemCreator
from factory.product.fizzbuzz import Fizzbuzz

class CreatorFizzbuzz(IProblemCreator):

    def factory_method(self):
        return Fizzbuzz()