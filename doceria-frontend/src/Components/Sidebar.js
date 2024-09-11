import React from "react";
import logo from "../assets/logo-barra-lateral.png";
import backgroundImage from "../assets/barra-lateral.png";

export default function Sidebar() {
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
          <a href="/home">Início</a>
        </li>
        <li className="mb-4 text-center items-center flex">
          <a href="/realizar-pedido">Realizar Pedido</a>
        </li>
        <li className="mb-4 text-center items-center flex">
          <a href="/meus-pedidos">Meus Pedidos</a>
        </li>
        <li className="mb-4 text-center items-center flex">
          <a href="/contato">Contato</a>
        </li>
      </ul>
    </aside>
  );
}
