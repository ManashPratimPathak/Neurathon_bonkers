import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import HomePage from "./pages/HomePage";
import MenuPage from "./pages/MenuPage";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route exact path="/Menu" element={<MenuPage />} />
          <Route exact path="/Menu" element={<MenuPage />} />
          <Route exact path="/Menu" element={<MenuPage />} />
          <Route exact path="/Menu" element={<MenuPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
