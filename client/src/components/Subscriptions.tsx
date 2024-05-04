import { Quiz, QuizType } from "../generated/quizz";
import TopicChip from "./TopicChip";
import { useEffect, useState } from "react";
import { quizClient } from "../grpc_client/index"

type SubsciptionsProps = {
    selectedQuizType: QuizType | null
}

const Subscriptions = ({ selectedQuizType }: SubsciptionsProps) => {
    const [quizzes, setQuizzes] = useState<Quiz[]>([])
    const [error, setError] = useState(false)
    const [streamError, setstreamError] = useState(false)

    const fetchQuizzes = async () => {
        try {
            const { response } = await quizClient.getAvailableQuizzes({})
            setQuizzes(response.quizzes)
            setError(false)
        }
        catch (err) {
            setError(true)
        }
    }

    useEffect(() => {
        fetchQuizzes()
    }, [])

    return (
        <div className="flex flex-col gap-8">
            {error &&
                (<div className="flex flex-col gap-10">
                    <h1 className="text-5xl font-serif font-bold text-[red]">Couldn't fetch quizzes</h1>
                    <button className="p-4 bg-off-white font-bold rounded-xl hover:bg-soft-gray" onClick={fetchQuizzes}>Refetch quizzes</button>
                </div>)}
            {!error &&
                <>
                    <h1 className="text-5xl font-serif font-bold text-light-green-gray">Choose your favorite <span className="text-soft-gray"> quiz topics</span></h1>
                    <div className="flex flex-col">
                        {quizzes.map((quizz) => <TopicChip key={quizz.type} topic={quizz.type} label={quizz.label} selected={selectedQuizType != null && selectedQuizType == quizz.type} onStreamError={setstreamError} />)}
                    </div>
                </>
            }
            {streamError && <h1 className="text-3xl font-serif font-bold text-[red]">Server closed current streams, try again later</h1>}
        </div >
    )
}


export default Subscriptions;
