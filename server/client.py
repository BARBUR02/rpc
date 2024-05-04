import grpc
from generated import quizz_pb2_grpc
from google.protobuf.empty_pb2 import Empty

from generated.quizz_pb2 import PlayQuizRequest
from generated import quizz_pb2


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = quizz_pb2_grpc.QuizServiceStub(channel)
    response = stub.GetAvailableQuizzes(Empty())
    for quiz in response.quizzes:
        print(quiz)

    response = stub.PlayQuiz(
        PlayQuizRequest(
            quiz_type=quizz_pb2.QuizType.PHYSICS,
        )
    )

    for _response in response:
        print(_response)


if __name__ == "__main__":
    run()
