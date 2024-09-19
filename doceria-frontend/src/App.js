import React, { useContext } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import LoginPage from "./components/LoginPage.js";
import GlobalContext from "./contexts/GlobalContext.js";
import RegistroPage from "./components/RegistroPage.js";
import CalendarioPage from "./components/CalendarioPage";
import HomePage from "./components/HomePage.js";
import RealizarPedidoPage from "./components/RealizarPedidoPage.js";
import MeusPedidosPage from "./components/MeusPedidosPage.js";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const ProtectedRoute = ({ element, allowedUsers }) => {
  const { currentUser } = useContext(GlobalContext);

  if (!currentUser || !allowedUsers.includes(currentUser.username)) {
    return <Navigate to="/" replace />;
  }

  return element;
};

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/registro" element={<RegistroPage />} />
        <Route
          path="/calendario"
          element={
            <ProtectedRoute
              element={<CalendarioPage />}
              allowedUsers={["katherine.corrales"]}
            />
          }
        />
        <Route path="*" element={<Navigate to="/" replace />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/realizar-pedido" element={<RealizarPedidoPage />} />
        <Route path="/meus-pedidos" element={<MeusPedidosPage />} />
      </Routes>
      <ToastContainer />
    </Router>
  );
}

export default App;
