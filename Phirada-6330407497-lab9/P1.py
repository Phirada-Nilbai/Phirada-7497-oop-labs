#Phirada Nilbai
#633040749-7
#Lab9 P1

"""P1.py This file illustrates the usage of an abstrace class"""
from abc import ABC
class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

     def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")


if __name__== "__main__":
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()
