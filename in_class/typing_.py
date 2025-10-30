# Class 10/30/25

from typing import Union, Optional
Vector = list[float]

def add(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    return a + b

def vector_sum(a:Vector) -> float:
    return sum(a)

# Optional below is used in place of Union[type, None]
def print_students(student:list) -> Optional[str]:
    if len(student) > 0:
        for i in student:
            print(i)
    else:
        return None
    
# Next class we'll discuss generic type