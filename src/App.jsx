import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import HomePage from "./pages/HomePage";
import MenuPage from "./pages/MenuPage";
import PushUp from "./components/PushUp";
import PullUp from "./components/PullUp";
import BicepCurl from "./components/BicepCurl";

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route exact path="/Menu" element={<MenuPage />} />
          <Route exact path="/push_up" element={<PushUp />} />
          <Route exact path="/pull_up" element={<PullUp />} />
          <Route exact path="/bicep_curls" element={<BicepCurl/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
