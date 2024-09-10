import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/logo.png";
import InputMask from "react-input-mask";
import backgroundImage from "../assets/login.png";

export default function RegistroPage() {
  return (
    <div
      className="flex items-center justify-center min-h-screen w-full bg-cover bg-no-repeat"
      style={{
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(${backgroundImage})`,
      }}
    >
      <form className="w-full max-w-md p-6 text-center">
        <img
          src={logo}
          alt="Logo do site"
          className="w-40 h-auto mx-auto mb-6"
        />
        <div className="text-left mb-4">
          <p className="text-sm font-bold text-white">Vamos criar sua conta</p>
        </div>
        <div className="mb-4">
          <input
            type="text"
            placeholder="Nome"
            required
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-4">
          <input
            type="email"
            placeholder="Email"
            required
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-4">
          <input
            type="date"
            placeholder="Data de Nascimento"
            required
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-4">
          <InputMask
            mask="(99) 99999-9999"
            placeholder="Celular"
            required
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-4">
          <input
            type="text"
            placeholder="Usuário"
            required
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-6">
          <input
            type="password"
            placeholder="Senha"
            required
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <button
          type="button"
          className="w-full h-11 bg-yellow-300 border-none rounded-full shadow-lg cursor-pointer text-xs font-bold"
        >
          CADASTRAR
        </button>
        <div className="mt-2 text-xs text-center text-white">
          Já tem uma conta?{" "}
          <Link to="/" className="hover:underline">
            Faça login
          </Link>
        </div>
      </form>
    </div>
  );
}
