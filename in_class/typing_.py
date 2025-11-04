# Class 10/30/25 about typing, then continuing 11/4/25 with stack, generics, and typevars

from enum import Enum
from typing import Union, Optional, TypeVar, Generic, Literal
Vector = list[float]

# def add(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
#     return a + b

# def vector_sum(a:Vector) -> float:
#     return sum(a)

# # Optional below is used in place of Union[type, None]
# def print_students(student:list) -> Optional[str]:
#     if len(student) > 0:
#         for i in student:
#             print(i)
#     else:
#         return None
    
T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items = []

    def push(self, item:T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
    
int_stack = Stack[int]()
int_stack.push(13)
int_stack.push(22)
# print(int_stack.pop())
# print(int_stack.pop())

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
# print(str_stack.pop())
# print(str_stack.pop())

Payable = Literal["CARD", "CASH", "PHONE"]

class Payable(Enum):
    CARD = 1
    CASH = 2
    PHONE = 3

# print(Payable.CARD.name) # .name give CARD; only Payable.CARD gives Payable.CARD
# print(Payable.CARD.value) # .value also gives 1
for i in Payable:
    print(i, i.value)

print(type(Payable.CARD))

class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    DONE = 3

class Task:
    def __init__(self, name:str, status:Status=Status.PENDING) -> None:
        self.name = name
        self.status = status
    def __str__(self) -> str:
        return f"Task(name={self.name}, status={self.status.name})"