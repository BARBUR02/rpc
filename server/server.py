import grpc
from generated import quizz_pb2_grpc
from quizz_service.quizz import QuizService
import concurrent.futures

import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    quizz_pb2_grpc.add_QuizServiceServicer_to_server(QuizService(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    print(f"Server started")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
