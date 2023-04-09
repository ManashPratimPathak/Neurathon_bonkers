import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import HomePage from "./pages/HomePage";
import MenuPage from "./pages/MenuPage";
import PushUp from "./components/PushUp";
import PullUp from "./components/PullUp";
import BicepCurl from "./components/BicepCurl";
import Chart from "./components/Chart";
import ResultBicepCurl from "./components/resultBicepCurl";
import ResultPullUp from "./components/resultPullUp";
import ResultPushUp from "./components/resultPushUp";

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route exact path="/Menu" element={<MenuPage />} />
          <Route exact path="/push_up" element={<PushUp />} />
          <Route exact path="/pull_up" element={<PullUp />} />
          <Route exact path="/bicep_curls" element={<BicepCurl />} />
          <Route exact path="/chart" element={<Chart />} />
          <Route exact path="/result/pullUp" element={<ResultPullUp />} />
          <Route exact path="/result/pushUp" element={<ResultPushUp />} />
          <Route exact path="/result/bicepCurl" element={<ResultBicepCurl />} />
          {/* <Route exact path="/result/pushUpStart" element={<Practice />} /> */}

        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
