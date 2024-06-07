from factory.product.i_problem_solver import IProblemSolver

class Fibonacci(IProblemSolver):

    def compute_results(self, data):
        list_result = []
        for num in data:
            result = self.__fibonacci(int(num))
            list_result.append(str(num) + " " + result)

        return list_result

    def __fibonacci(self,number):

        number_1 = 0
        number_2 = 1

        actual_number = 0   

        while actual_number <= number:

            if actual_number == number:
                return "True"
            
            actual_number = number_1 + number_2

            number_1 = number_2

            number_2 = actual_number
        
        return "False"


