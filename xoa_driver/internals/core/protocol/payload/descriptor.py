
from __future__ import annotations
from io import BytesIO

# import struct
from typing import (
    Any,
    Generic,
    Protocol,
    TypeVar,
)

from typing_extensions import (
    NoReturn,
    Self,
)

from .field import FieldSpecs

GenericType = TypeVar("GenericType")


class SetInstance(Protocol):
    _buffer: BytesIO


class GetInstance(Protocol):
    _buffer: memoryview


class RequestFieldState:
    @staticmethod
    def setter(descr: FieldDescriptor, instance: SetInstance, value: Any) -> None:
        instance._buffer.write(descr.specs.pack(val=value))

    @staticmethod
    def getter(descr: FieldDescriptor, instance: SetInstance, cls) -> NoReturn:
        raise AttributeError from None


class ResponseFieldState:
    @staticmethod
    def setter(descr: FieldDescriptor, instance: GetInstance, value: Any) -> NoReturn:
        raise AttributeError from None

    @staticmethod
    def getter(descr: FieldDescriptor, instance: GetInstance, cls) -> Any:
        return descr.specs.unpack(instance._buffer, descr.offset)


class FieldDescriptor(Generic[GenericType]):
    '''
    Descriptor representing getter and setter of the field
    '''
    __slots__ = ("specs", "user_type", "state", "name", "offset",)

    def __init__(self: Self, specs: FieldSpecs, user_type: GenericType, is_response: bool) -> None:
        # will be called from the Meta class
        self.specs = specs
        self.user_type = user_type
        self.state = RequestFieldState if not is_response else ResponseFieldState

    def __set_name__(self: Self, owner, name: str) -> None:
        # Will be called when owner object will be created
        self.name = name
        self.offset = sum(
            v for _, v in owner._order[:owner._order.index((name, self.specs.bsize))]
        )

    def __set__(self: Self, instance, value: GenericType) -> None:
        # Executed at the runtimne
        self.state.setter(self, instance, value)

    def __get__(self: Self, instance, cls) -> GenericType | Self:
        # Executed at the runtimne
        if instance is None:
            return self
        return self.state.getter(self, instance, cls)
