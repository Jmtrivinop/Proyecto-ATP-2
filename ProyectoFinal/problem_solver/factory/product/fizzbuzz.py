from factory.product.i_problem_solver import IProblemSolver

class Fizzbuzz(IProblemSolver):

    def compute_results(self, data):
        list_result = []
        for num in data:
            result = self.__fizzbuzz(int(num))
            list_result.append(str(num) + " " + result)

        return list_result
    
    def __fizzbuzz(self,number):
        result = ""

        if number % 3 == 0:
            result += "Fizz"

        if number % 5 == 0:
            result += "Buzz"

        if result == "":
            result = str(number)

        return result
    


