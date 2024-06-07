from factory.creator.i_problem_creator import  IProblemCreator
from factory.product.prime_classifier import PrimeClassifier

class CreatorPrime(IProblemCreator):

    def factory_method(self):
        return PrimeClassifier()
    
    