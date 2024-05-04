import { GrpcWebFetchTransport } from "@protobuf-ts/grpcweb-transport"
import { QuizServiceClient } from "../generated/quizz.client"

const transport = new GrpcWebFetchTransport({ baseUrl: "http://localhost:8080" })
export const quizClient = new QuizServiceClient(transport)

