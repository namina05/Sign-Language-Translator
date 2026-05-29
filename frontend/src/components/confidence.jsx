function Confidencebar({confidence}){
    const getColor = () => {
        if (confidence > 80) return "#22c55e";
        if (confidence > 50) return "#facc15";
        return "#ef4444";
        };
    return(
        <div className="card">
            <h3>Confidence</h3>
            <div className="bar">
                <div className="fill"
                    style = {{width:`${confidence}%`
                    ,background: getColor()}}>

                </div>
            </div>
            <p>{confidence}%</p>
        </div>
    );
}

export default Confidencebar;