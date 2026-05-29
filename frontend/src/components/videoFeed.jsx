import { useEffect, useState } from "react";

function Videofeed(){
    const [timestamp,setTimestamp] = useState(Date.now());
    const [cam,setcam] = useState(true)
    useEffect(()=>{
        
        const interval = setInterval(async() => {
            const res = await fetch(
                "http://127.0.0.1:8000/predictions"
            );

            const data = await res.json();


            setcam(
                data.camera_available
            );
            
        }, 100);
        
        return ()=> clearInterval(interval);
    },[])
    if(cam){
        return (
        <div className="video-feed">
            <img
                src="http://127.0.0.1:8000/video_feed"
                width="100%"
            />
        </div>
    );
    }
        return(
            <div className="video-feed">
                <p>CAMERA UNAVAILABLE</p>
            </div>
        )
    
        

}

export default Videofeed;