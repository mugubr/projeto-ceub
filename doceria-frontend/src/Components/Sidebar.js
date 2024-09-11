import React, { useContext } from "react";
import GlobalContext from "../Context/GlobalContext";
import logo from "../assets/logo-barra-lateral.png";
import backgroundImage from "../assets/barra-lateral.png";
import { NavLink } from "react-router-dom";
import ContatoModal from "./ContatoModal";

export default function Sidebar() {
  const nome = localStorage.getItem("nome");
  const { showContatoModal, setShowContatoModal } = useContext(GlobalContext);
  return (
    <>
      {showContatoModal && <ContatoModal />}
      <aside
        className="w-72 h-full bg-cover bg-center text-white flex flex-col items-center p-16"
        style={{
          backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(${backgroundImage})`,
        }}
      >
        <img src={logo} className="w-36 h-auto mb-16" alt="logo" />
        <p className="mb-4 text-center items-center flex">Olá, {nome}!</p>
        <ul className="list-none w-full">
          <li className="mb-4">
            <NavLink
              to="/home"
              className={({ isActive }) =>
                `block py-2 px-4 ${isActive ? "bg-yellow-500" : "hover:bg-yellow-300"} w-full`
              }
              style={{ display: "block" }}
            >
              Início
            </NavLink>
          </li>
          <li className="mb-4">
            <NavLink
              to="/realizar-pedido"
              className={({ isActive }) =>
                `block py-2 px-4 ${isActive ? "bg-yellow-500" : "hover:bg-yellow-300"} w-full`
              }
              style={{ display: "block" }}
            >
              Realizar Pedido
            </NavLink>
          </li>
          <li className="mb-4">
            <NavLink
              to="/meus-pedidos"
              className={({ isActive }) =>
                `block py-2 px-4 ${isActive ? "bg-yellow-500" : "hover:bg-yellow-300"} w-full`
              }
              style={{ display: "block" }}
            >
              Meus Pedidos
            </NavLink>
          </li>
          <li className="mb-4">
            <a
              href="#!"
              onClick={() => setShowContatoModal(true)}
              className="block py-2 px-4 hover:bg-yellow-300 w-full"
            >
              Contato
            </a>
          </li>
        </ul>
      </aside>
    </>
  );
}
