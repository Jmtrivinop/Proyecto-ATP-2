import abc

class INumberGenerator(abc.ABC):

    @abc.abstractmethod
    def generate_numbers(self, min, max, range) :
        pass
