from factory.creator.i_problem_creator import IProblemCreator
from factory.creator.creator_fibonacci import CreatorFibonacci
from factory.creator.creator_fizzbuzz import CreatorFizzbuzz
from factory.creator.creator_prime import CreatorPrime

class MyApp:
        
    def select_problem(self, problem):
        if problem == "primeClassifier":
            return CreatorPrime()
        
        if problem == "fibonacci":
            return CreatorFibonacci()
        
        if problem == "fizzbuzz":
            return CreatorFizzbuzz()
        
        
        return None

    def run(self, creator: IProblemCreator, data):
    
        result = creator.solve(data)
        return result

