import { BsBellSlashFill } from "react-icons/bs";
import { PlayQuizRequest, Question, QuizType } from "../generated/quizz"
import { FaBell } from "react-icons/fa";
import { useContext, useState } from "react";
import type { ServerStreamingCall } from "@protobuf-ts/runtime-rpc";
import { quizClient } from "../grpc_client";
import QuizContext from "../context/quizz_context";

type TopicChipProps = {
    topic: QuizType,
    label: string,
    selected: boolean,
    onStreamError: (error: boolean) => void
    // onActivate: (quizType: QuizType) => void
}

const TopicChip = ({ topic, label, selected, onStreamError }: TopicChipProps) => {
    const [active, setActive] = useState(false)
    const [stream, setStream] = useState<ServerStreamingCall<PlayQuizRequest, Question> | null>(null);
    const activeIcon = active ? <FaBell className="fill-off-white text-xl" /> : <BsBellSlashFill className="fill-light-green-gray text-xl" />;

    const { availableQuestions, updateAvailableQuestions, pickQuestionTopic } = useContext(QuizContext)
    const questionCount = availableQuestions.get(topic)?.length

    const handleClick = async () => {
        if (stream) {
            return
        }
        else {
            setActive(prevValue => !prevValue)
            const stream = quizClient.playQuiz({ quizType: topic })
            setStream(stream)
            onStreamError(false)
            try {
                for await (let question of stream.responses) {
                    updateAvailableQuestions(topic, question)
                }

            } catch (error) {
                console.log("CHiperror!!")
                onStreamError(true)
            }
            setStream(null)
            setActive(false)
        }

    }

    const handleTopicSelection = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        e.stopPropagation()
        pickQuestionTopic(topic)
    }

    return (
        <div className={active ? "relative m-2 flex justify-between items-center whitespace-nowrap rounded-lg border-[1.9px] py-2.5 px-4 border-off-white" :
            "relative m-2 flex justify-between items-center whitespace-nowrap rounded-lg border-[1.9px] py-2.5 px-4 border-light-green-gray"
        } onClick={handleClick}>
            <span className={active ? `font-sans text-m font-bold uppercase text-off-white` : `font-sans text-m font-bold uppercase text-light-green-gray`}>{label}</span>
            <button className="absolute text-m text-dark-green-gray flex justify-center items-center -top-3 -right-5 bg-soft-gray w-8 h-8 rounded-xl hover:bg-light-green-gray" onClick={(e) => handleTopicSelection(e)}
                style={(questionCount && questionCount > 0) ? { ...(selected ? { backgroundColor: "greenyellow" } : {}) } : { display: "none" }}
            >
                <p>{questionCount}</p>
            </button>

            {activeIcon}
        </div>
    );

}

export default TopicChip
