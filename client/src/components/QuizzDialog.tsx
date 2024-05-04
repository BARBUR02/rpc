import { useState } from "react"
import { Question, QuizType } from "../generated/quizz"

type QuizzDialogProps = {
    questions: Question[],
    quizType: QuizType | null,
    correctAnswer: () => void,
    incorrectAnswer: () => void,
    popQuestionFromQuiz: (quizType: QuizType, question: Question) => void
}

const QuizzDialog = ({ questions, quizType, correctAnswer, incorrectAnswer, popQuestionFromQuiz }: QuizzDialogProps) => {
    const [answer, setAnswer] = useState<string | null>(null)
    const activeQuestion = questions[0]

    const checkAnswer = (answer: string) => {
        if (answer == activeQuestion.expected) {
            correctAnswer()
        } else {
            incorrectAnswer()
        }
        setAnswer(answer)
        setTimeout(() => {
            if (quizType) {
                popQuestionFromQuiz(quizType, activeQuestion)
            }
            setAnswer(null)
        }, 1000)

    }

    if (!quizType) {
        return null
        return <h1 className="text-3xl font-sans font-bold text-light-green-gray">Select quizz type to <span>start THE quizz!</span></h1>
    }

    if (questions.length == 0) {
        return <h1 className="text-3xl font-sans font-bold text-light-green-gray">Empty question list for given type,<span>subscribe for more questions!</span></h1>
    }

    return (
        <section className="w-full flex flex-col justify-self-center gap-12 mt-12 bg-light-green-gray bg-opacity-40 px-12 py-8 rounded-lg  shadow-inner">
            <div className="flex flex-row justify-between">
                <div>
                    <h3 className="text-md font-sans font-bold text-off-white" style={!answer ? { display: "none" } : {}}>Next question soon...</h3>
                </div>
                <div className="flex gap-2">
                    <h3 className="text-md font-sans font-bold text-light-green-gray">Question type:</h3>
                    <h3 className="text-md  font-sans font-bold text-soft-gray">{QuizType[quizType]}</h3>
                </div>
            </div>
            <div className="flex flex-col gap-8">
                <div>
                    <h2 className="text-3xl font-sans font-bold text-dark-green-gray">{activeQuestion.text}</h2>
                    <div className="w-full h-2 bg-dark-green-gray rounded-xl"></div>
                </div>
                <ul className="grid grid-cols-2 list-none gap-16">
                    {activeQuestion.options.map(_answer => (
                        <li className="p-4 bg-off-white rounded-lg cursor-pointer hover:bg-soft-gray font-medium hover:font-bold"
                            key={_answer}
                            onClick={() => {
                                checkAnswer(_answer)
                            }}
                            style={answer ? (answer && activeQuestion.options.some(option => option == answer) && _answer == activeQuestion.expected) ? { background: "greenyellow", pointerEvents: "none" } : (answer == _answer ? { background: "red", pointerEvents: "none" } : { pointerEvents: "none" }) :
                                {}
                            }
                        >{_answer}</li>

                    ))}
                </ul>
            </div>
        </section >
    )
}


export default QuizzDialog
