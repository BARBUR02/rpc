from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuizType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT: _ClassVar[QuizType]
    ANIMAL: _ClassVar[QuizType]
    GEOGRAPHY: _ClassVar[QuizType]
    PHYSICS: _ClassVar[QuizType]
    SPORT: _ClassVar[QuizType]
DEFAULT: QuizType
ANIMAL: QuizType
GEOGRAPHY: QuizType
PHYSICS: QuizType
SPORT: QuizType

class Question(_message.Message):
    __slots__ = ("text", "expected", "options")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    expected: str
    options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, text: _Optional[str] = ..., expected: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ...) -> None: ...

class Quiz(_message.Message):
    __slots__ = ("type", "label", "no_questions")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    NO_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    type: QuizType
    label: str
    no_questions: int
    def __init__(self, type: _Optional[_Union[QuizType, str]] = ..., label: _Optional[str] = ..., no_questions: _Optional[int] = ...) -> None: ...

class QuizListResponse(_message.Message):
    __slots__ = ("quizzes",)
    QUIZZES_FIELD_NUMBER: _ClassVar[int]
    quizzes: _containers.RepeatedCompositeFieldContainer[Quiz]
    def __init__(self, quizzes: _Optional[_Iterable[_Union[Quiz, _Mapping]]] = ...) -> None: ...

class PlayQuizRequest(_message.Message):
    __slots__ = ("quiz_type",)
    QUIZ_TYPE_FIELD_NUMBER: _ClassVar[int]
    quiz_type: QuizType
    def __init__(self, quiz_type: _Optional[_Union[QuizType, str]] = ...) -> None: ...
