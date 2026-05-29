import { BrowserRouter, Routes, Route } from "react-router-dom";
import Homepage from "./pages/home";
import Translator from "./pages/translator";
import "./App.css";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route 
        path="/"
        element={<Homepage />}/>
        <Route
          path = "/translator"
          element={<Translator />}
        />
      </Routes>
    
    </BrowserRouter>
  );
}

export default App
