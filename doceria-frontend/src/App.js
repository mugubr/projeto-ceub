import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LoginPage from "./Components/LoginPage.js";
import RegistroPage from "./Components/RegistroPage.js";
import CalendarioPage from "./Components/CalendarioPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/registro" element={<RegistroPage />} />
        <Route path="/calendario" element={<CalendarioPage />} />
      </Routes>
    </Router>
  );
}

export default App;
