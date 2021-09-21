
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:

            self.front = node
            self.rear = node
        else:

            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
           dequeueValue=self.front.value
           self.front=self.front.next
           return dequeueValue
        except :
           return 'The Queue is empty'

class Dog:
    def __init__(self,name):
        self.name=name
        self.kind='dog'

class Cat:
    def __init__(self,name):
        self.name=name
        self.kind='cat'

class Animal:
    def __init__(self,name,kind):
        self.name=name
        self.kind=kind


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self,animal):

        if animal.kind=='cat':
            self.cat.enqueue(animal)
        elif animal.kind=='dog':
            self.dog.enqueue(animal)
        else:
            return 'the animal should be cat or dog'
    def dequeue(self,pref=None):
        if pref == 'cat':
            return self.cat.dequeue().name
        elif pref == 'dog':
            return self.dog.dequeue().name
        else:
            return None


def test_happypath_return_cat_name():
  if __name__ == "__main__":
    dj = Dog('dj')
    boby=Dog('boby')
    mert=Dog('mert')
    snow = Cat('snow')
    amy=Cat('amy')
    mshmsh=Cat('mshmsh')
    hmed=Animal('hmed','hores')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(dj)
    animalShelter.enqueue(boby)
    animalShelter.enqueue(mert)
    animalShelter.enqueue(snow)
    animalShelter.enqueue(amy)
    animalShelter.enqueue(mshmsh)

    actual = animalShelter.dequeue('cat')
    expected = 'snow'
    assert actual == expected

def test_Expected_failure_return_wrong_dog_name():
    dj = Dog('dj')
    boby=Dog('boby')
    mert=Dog('mert')
    snow = Cat('snow')
    amy=Cat('amy')
    mshmsh=Cat('mshmsh')
    hmed=Animal('hmed','hores')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(dj)
    animalShelter.enqueue(boby)
    animalShelter.enqueue(mert)
    animalShelter.enqueue(snow)
    animalShelter.enqueue(amy)
    animalShelter.enqueue(mshmsh)
    actual = animalShelter.dequeue('dog')
    expected = 'mert'
    assert actual != expected

def test_Edge_Case_return_None():
    dj = Dog('dj')
    boby=Dog('boby')
    mert=Dog('mert')
    snow = Cat('snow')
    amy=Cat('amy')
    mshmsh=Cat('mshmsh')
    hmed=Animal('hmed','hores')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(dj)
    animalShelter.enqueue(boby)
    animalShelter.enqueue(mert)
    animalShelter.enqueue(snow)
    animalShelter.enqueue(amy)
    animalShelter.enqueue(mshmsh)
    actual = animalShelter.dequeue('hores')
    expected = None
    assert actual == expected
