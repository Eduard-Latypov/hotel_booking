from fastapi import Path, Query, Body
from pydantic import BaseModel
from typing import TypeVar, Protocol, Any


class CanAdd(Protocol):
    def __add__(self, other: Any) -> Any:
        ...


T = TypeVar("T", bound=CanAdd)


def func(arg1: T, arg2: T) -> T:
    return arg1 + arg2


print(func("text", "text2"))


print("text".__add__(" text"))


def func_2(arg1, arg2):
    print(arg1 + arg2)
