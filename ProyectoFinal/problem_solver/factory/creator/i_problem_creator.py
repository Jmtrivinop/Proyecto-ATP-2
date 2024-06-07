from abc import ABC, abstractmethod

class IProblemCreator(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass

    def solve(self, data):

        problem_solver = self.factory_method()

        result = problem_solver.compute_results(data)

        return result
