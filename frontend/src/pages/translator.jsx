
import Sidebar from "../components/sidebar";
import Videofeed from "../components/videoFeed";
import { useEffect } from "react";

function Translator() {
    useEffect(() => {

    fetch("http://127.0.0.1:8000/start", {
        method: "POST"
    });

    return () => {

        fetch("http://127.0.0.1:8000/stop", {
            method: "POST"
        });

    };

}, []);
    return (
            <div className="app">
                <Sidebar />
                <Videofeed />
            </div>
    );
}

export default Translator;