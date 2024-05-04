from time import sleep
from generated import quizz_pb2_grpc
from generated import quizz_pb2
import json


class QuizService(quizz_pb2_grpc.QuizServiceServicer):
    def GetAvailableQuizzes(self, request, context):
        return get_quizz_list()

    def PlayQuiz(self, request: quizz_pb2.PlayQuizRequest, context):
        for question in get_quiz_questions(request.quiz_type):
            yield question
            sleep(2)


QUIZ_FILE_PATH = "data/quizz.json"


def get_quiz_questions(
    quiz_type: quizz_pb2.QuizType,
) -> list[quizz_pb2.Question]:
    if quiz := next(
        (
            _quiz
            for _quiz in _load_quiz_file()
            if _quiz["type"] == quizz_pb2.QuizType.Name(quiz_type)
        ),
        None,
    ):
        return [
            quizz_pb2.Question(
                text=question["text"],
                expected=question["expected"],
                options=question["options"],
            )
            for question in quiz["questions"]
        ]

    return []


def get_quizz_list() -> quizz_pb2.QuizListResponse:
    quizzes = load_quizzes()
    return quizz_pb2.QuizListResponse(quizzes=quizzes)


def load_quizzes() -> list[quizz_pb2.Quiz]:
    result = [
        quizz_pb2.Quiz(
            type=quiz["type"],
            label=quiz["label"],
            no_questions=len(quiz["questions"]),
        )
        for quiz in _load_quiz_file()
    ]
    return result


def _load_quiz_file() -> dict:
    with open(QUIZ_FILE_PATH) as file:
        return json.load(file)
