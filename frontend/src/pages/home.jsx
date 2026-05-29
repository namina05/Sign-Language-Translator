import { Link } from "react-router-dom";

function Homepage(){
    return(
        <div className="home">

            <div className="hero">

                <h1>SIGN VISION AI</h1>

                <p className="subtitle">
                    Real-time sign language recognition powered by AI
                </p>

                <Link to="/translator">
                    <button className="start-btn">
                        Start Translating
                    </button>
                </Link>

            </div>

            <div className="stats">

                <div className="stat-card">
                    <h2>99.06%</h2>
                    <p>Model Accuracy</p>
                </div>

                <div className="stat-card">
                    <h2>5000+</h2>
                    <p>Samples Trained</p>
                </div>

                <div className="stat-card">
                    <h2>26</h2>
                    <p>ASL Letters Supported</p>
                </div>

                <div className="stat-card">
                    <h2>Real-Time</h2>
                    <p>Recognition</p>
                </div>

            </div>

            <footer>
                Built with React • FastAPI • MediaPipe • Scikit-Learn
            </footer>

        </div>
    );
}

export default Homepage;