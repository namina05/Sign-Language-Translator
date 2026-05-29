function Handdetected({detected}){
    return(
        <div className="card">
            <h3>HAND STATUS</h3>
            <div className="detection">
                <p>{detected?"HAND DETECTED":"NO HAND DETECTED"}</p>
            </div>
        </div>
    );
}

export default Handdetected;