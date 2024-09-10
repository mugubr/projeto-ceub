import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/logo.png";
import backgroundImage from "../assets/login.png";

export default function LoginPage() {
  return (
    <div
      className="flex items-center justify-center min-h-screen w-full bg-cover bg-no-repeat"
      style={{
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(${backgroundImage})`,
      }}
    >
      <div className="w-full max-w-xs mx-auto bg-transparent p-6 text-center">
        <form>
          <img
            src={logo}
            alt="Logo do site"
            className="w-40 h-auto mx-auto mb-12"
          />
          <div className="text-left ">
            <p className="text-sm font-bold text-white">Olá,</p>
            <p className="text-sm font-bold text-white">
              seja bem-vindo(a) de volta!
            </p>
          </div>
          <div className="text-left mb-2">
            <p className="text-xs text-gray-400">
              Faça o seu login para começar
            </p>
          </div>
          <div className="relative w-full h-9 mb-6">
            <input
              type="text"
              placeholder="Usuário"
              required
              className="w-full h-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
            />
          </div>
          <div className="relative w-full h-9 mb-6">
            <input
              type="password"
              placeholder="Senha"
              required
              className="w-full h-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
            />
          </div>
          <button
            type="button"
            className="w-full h-11 bg-yellow-300 border-none rounded-full shadow-lg cursor-pointer text-xs font-bold"
          >
            ENTRAR
          </button>
          <div className="mt-2 text-xs text-center">
            <Link to="/registro" className="text-white hover:underline">
              CADASTRE-SE
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
}
