import { createContext, useState } from "react";
import { Question, QuizType } from "../generated/quizz";

type QuizContextType = {
    availableQuestions: Map<QuizType, Question[]>,
    selectedQuizType: QuizType | null,
    score: number,
    allAttempts: number,
    updateAvailableQuestions: (quizType: QuizType, question: Question) => void,
    pickQuestionTopic: (quizType: QuizType) => void,
    correctAnswer: () => void,
    incorrectAnswer: () => void,
    popQuestionFromQuiz: (quizType: QuizType, question: Question) => void,
};

const QuizContext = createContext<QuizContextType>(
    {} as QuizContextType
);

export default QuizContext;

export const QuizProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [availableQuestions, setAvailableQuestions] = useState(new Map<QuizType, Question[]>())
    const [selectedQuizType, setSelectedQuizType] = useState<QuizType | null>(null)
    const [score, setScore] = useState(0)
    const [allAttempts, setAllAttempts] = useState(0)

    const updateAvailableQuestions = (quizType: QuizType, question: Question) => {
        setAvailableQuestions(prevMap => {
            const questionsPerQuizz = prevMap.get(quizType) || []
            const newQuestions = [...questionsPerQuizz, question]
            const updatedMap = new Map(prevMap)
            updatedMap.set(quizType, newQuestions)
            return updatedMap
        })
    }

    const pickQuestionTopic = (quizType: QuizType) => {
        setSelectedQuizType(quizType);
    }

    const correctAnswer = () => {
        setScore(score => score + 1)
        setAllAttempts(allAttempts => allAttempts + 1)
    }
    const incorrectAnswer = () => {
        setAllAttempts(allAttempts => allAttempts + 1)
    }

    const popQuestionFromQuiz = (quizType: QuizType, question: Question) => {
        setAvailableQuestions(prevMap => {
            const questionsPerQuizz = prevMap.get(quizType) || []
            const newQuestions = questionsPerQuizz.filter(_question => _question.text != question.text)
            const updatedMap = new Map(prevMap)
            updatedMap.set(quizType, newQuestions)
            return updatedMap
        })
    }

    return <QuizContext.Provider value={{ availableQuestions, selectedQuizType, score, allAttempts, updateAvailableQuestions, pickQuestionTopic, correctAnswer, incorrectAnswer, popQuestionFromQuiz }}>
        {children}
    </ QuizContext.Provider>
}
