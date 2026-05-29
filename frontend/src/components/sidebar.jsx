import Confidencebar from "./confidence";
import Handdetected  from "./handDetected";
import Predictioncard from "./prediction";
import Sentencebuffer from "./sentencebuffer";
import { useEffect,useState } from "react";


function Sidebar(){
    const [prediction,setPrediction] = useState("...");
    const [confidence,setConfidence] = useState(0);
    const [sentence,setSentence] = useState("");
    const [detected,setDetected] = useState(false); 

    useEffect(() => {
    const interval = setInterval(async () => {
        const res = await fetch("http://127.0.0.1:8000/predictions")
        const data = await res.json()


        setDetected(data.hand_detected);

        setPrediction(data.predictions)
        setConfidence(data.confidence)
        setSentence(data.sentence)
        setDetected(data.hand_detected)

    }, 100)

    return () => clearInterval(interval)
    }, [])

    return(

        <div className = "sidebar">
            <h1>SIGN VISION AI</h1>
            <Predictioncard prediction = {prediction}/>
            <Sentencebuffer sentence = "HI"></Sentencebuffer>
            <Confidencebar confidence = {confidence}/>
            <Handdetected detected = {detected} />
        </div>
    );
}

export default Sidebar;