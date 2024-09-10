import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import logo from "../assets/logo.png";
import InputMask from "react-input-mask";
import backgroundImage from "../assets/login.png";
import { toast, ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';

export default function RegistroPage() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    nome: "",
    email: "",
    data_nascimento: "",
    celular: "",
    usuario: "",
    senha: ""
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:8000/clientes", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        toast.error(errorData.message || "Erro ao cadastrar");
        throw new Error("Erro ao cadastrar");
      }

      toast.success("Cadastro realizado com sucesso!");
      
      setTimeout(() => navigate("/"), 3000);
      
    } catch (error) {
      console.error("Erro ao registrar usuário:", error);
    }
  };

  return (
    <div
      className="flex items-center justify-center min-h-screen w-full bg-cover bg-no-repeat"
      style={{
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(${backgroundImage})`,
      }}
    >
      <form className="w-full max-w-md p-6 text-center" onSubmit={handleSubmit}>
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
            name="nome"
            placeholder="Nome"
            required
            value={formData.nome}
            onChange={handleInputChange}
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-4">
          <input
            type="email"
            name="email"
            placeholder="Email"
            required
            value={formData.email}
            onChange={handleInputChange}
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-4">
          <input
            type="date"
            name="data_nascimento"
            placeholder="Data de Nascimento"
            required
            value={formData.data_nascimento}
            onChange={handleInputChange}
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-4">
          <InputMask
            mask="(99) 99999-9999"
            name="celular"
            placeholder="Celular"
            required
            value={formData.celular}
            onChange={handleInputChange}
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-4">
          <input
            type="text"
            name="usuario"
            placeholder="Usuário"
            required
            value={formData.usuario}
            onChange={handleInputChange}
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <div className="mb-6">
          <input
            type="password"
            name="senha"
            placeholder="Senha"
            required
            value={formData.senha}
            onChange={handleInputChange}
            className="w-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none"
          />
        </div>
        <button
          type="submit"
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
        <ToastContainer />
      </form>
    </div>
  );
}
