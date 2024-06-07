from factory.product.i_problem_solver import IProblemSolver

class PrimeClassifier(IProblemSolver):

    def compute_results(self, data):
        list_result = []
        for num in data:
            result = self.__prime_classifier(int(num))
            list_result.append(str(num) + " " + result)

        return list_result
    
    def __prime_classifier(self,number):
        if self.__is_prime(number):
            return "is prime"
        if self.__is_cuadratic_semiprime(number):
            return "is cuadratic semiprime"
        if self.__is_semiprime(number):
            return "is semiprime"
        return str(number)

    def __is_prime(self, number):
        count = 0
        for i in range(2,number + 1):
            
            if (number % i) == 0:
                count +=1
        
        if count <2:
            return True

        return False
    
    def __is_semiprime(self, number):
        count = 0
        divisor = []
        for i in range(2,number):
            if (number % i) == 0 and self.__is_prime(i):
                divisor.append(i)
                count +=1
        
        if count == 2 and divisor[0]* divisor[1] == number:

            return True
        
        return False

    def __is_cuadratic_semiprime(self, number):
        for i in range(2,number + 1):
            if (number % i) == 0 and self.__is_prime(i):
                if (i*i) == number:
                    return True
        return False


