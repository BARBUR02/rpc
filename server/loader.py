import json

from generated import quizz_pb2

QUIZ_FILE_PATH = "data/quizz.json"


def load_quizzes() -> list[quizz_pb2.Quiz]:
    return [
        quizz_pb2.Quiz(
            type=quizz_pb2.QuizType(quiz["type"]),
            label=quiz["label"],
            no_questions=len(quiz["questions"]),
        )
        for quiz in _load_quiz_file()
    ]


def get_quiz_questions(
    quiz_type: quizz_pb2.QuizType,
) -> list[quizz_pb2.Question]:
    if quiz := next(
        (_quiz for _quiz in _load_quiz_file() if _quiz["type"] == str(quiz_type)), None
    ):
        return [
            quizz_pb2.Question(
                text=question["type"],
                expected=question["expected"],
                options=question["options"],
            )
            for question in quiz["questions"]
        ]

    return []


def get_quizz_list() -> quizz_pb2.QuizListResponse:
    return quizz_pb2.QuizListResponse(quizzes=load_quizzes())


def _load_quiz_file() -> dict:
    with open(QUIZ_FILE_PATH) as file:
        return json.load(file)
