import React from "react";
import logo from "../assets/logo-barra-lateral.png";
import backgroundImage from "../assets/barra-lateral.png";
import CalendarioAuxiliar from "./CalendarioAuxiliar";

export default function CalendarioSidebar() {
  return (
    <aside
      className="w-72 h-full bg-cover bg-center text-white flex flex-col items-center p-16"
      style={{
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(${backgroundImage})`,
      }}
    >
      <img src={logo} className="w-36 h-auto mb-16" alt="logo" />
      <ul className="list-none w-full">
        <li className="mb-4 text-center items-center flex">
          <span className="block w-4 h-4 mr-2 bg-blue-600 rounded-sm"></span>
          Pedido
        </li>
        <li className="mb-4 text-center items-center flex">
          <span className="block w-4 h-4 mr-2 bg-yellow-600 rounded-sm"></span>
          Produção
        </li>
        <li className="mb-4 text-center items-center flex">
          <span className="block w-4 h-4 mr-2 bg-green-600 rounded-sm"></span>
          Entrega
        </li>
      </ul>
      <div className="w-full mt-auto">
        <CalendarioAuxiliar />
      </div>
    </aside>
  );
}
