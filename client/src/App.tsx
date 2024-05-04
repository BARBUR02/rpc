import { useContext } from 'react'
import './App.css'
import Subscriptions from './components/Subscriptions'
import QuizContext from './context/quizz_context'
import QuizzDialog from './components/QuizzDialog'



function App() {
  const { score, allAttempts, selectedQuizType, availableQuestions, correctAnswer, incorrectAnswer, popQuestionFromQuiz } = useContext(QuizContext)

  const selectedQuestions = selectedQuizType ? availableQuestions.get(selectedQuizType) || [] : []

  return (
    <>
      <div className='h-screen w-screen grid grid-cols-3 gap-4 bg-dark-green-gray m-0 p-16'>
        <div>
          <Subscriptions selectedQuizType={selectedQuizType} />
        </div>
        <div className='col-span-2 flex flex-col  items-center gap-4 justify-start'>
          <div className='flex flex-row  self-end gap-4'>
            <h1 className="text-5xl font-serif font-bold text-light-green-gray">Your score</h1>
            <h1 className="text-5xl font-serif font-bold text-light-green-gray">{score}</h1>
          </div>
          <div className='flex self-end flex-row gap-4'>
            <h1 className="text-5xl font-serif font-bold text-soft-gray">Total attempts</h1>
            <h1 className="text-5xl font-serif font-bold text-soft-gray">{allAttempts}</h1>
          </div>
          <div className="flex-grow flex items-center justify-center w-5/6">
            <QuizzDialog questions={selectedQuestions} quizType={selectedQuizType} correctAnswer={correctAnswer} incorrectAnswer={incorrectAnswer} popQuestionFromQuiz={popQuestionFromQuiz}></QuizzDialog>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
