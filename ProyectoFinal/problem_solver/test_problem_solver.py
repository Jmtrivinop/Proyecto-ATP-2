import pytest
from factory.creator.creator_fibonacci import CreatorFibonacci
from factory.creator.creator_fizzbuzz import CreatorFizzbuzz
from factory.creator.creator_prime import CreatorPrime
from my_app import MyApp 

@pytest.fixture
def app():
    return MyApp()

def test_select_problem_prime(app):
    creator = app.select_problem("primeClassifier")
    assert isinstance(creator, CreatorPrime)

def test_select_problem_fibonacci(app):
    creator = app.select_problem("fibonacci")
    assert isinstance(creator, CreatorFibonacci)

def test_select_problem_fizzbuzz(app):
    creator = app.select_problem("fizzbuzz")
    assert isinstance(creator, CreatorFizzbuzz)

def test_select_problem_invalid(app):
    creator = app.select_problem("invalid")
    assert creator is None

def test_solve_prime(app):
    creator = CreatorPrime()
    data = [2,3,5,6,7,8,9]
    result = app.run(creator, data)

    expected_result = ["2 is prime", "3 is prime", "5 is prime", "6 is semiprime", "7 is prime", "8 8", "9 is cuadratic semiprime"]

    assert result == expected_result

def test_solve_fibonacci(app):
    creator = CreatorFibonacci()
    data = [2,3,5,6,7,8,9]
    result = app.run(creator, data)

    expected_result = ["2 True", "3 True", "5 True", "6 False", "7 False", "8 True", "9 False"]

    assert result == expected_result
def test_solve_fizzbuzz(app):
    creator = CreatorFizzbuzz()
    data = [2,3,5,6,15, 21]
    result = app.run(creator, data)

    expected_result = ["2 2", "3 Fizz", "5 Buzz", "6 Fizz", "15 FizzBuzz", "21 Fizz"]

    assert result == expected_result
