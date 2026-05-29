function Predictioncard({prediction}){
    return(
        <div className="card" >
            <h3>Predictions</h3>
            <div className="prediction">
                <p>{prediction}</p>
            </div>
        </div>
    );
}

export default Predictioncard;