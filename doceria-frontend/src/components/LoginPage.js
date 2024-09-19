import React, { useContext, useState } from "react";
import GlobalContext from "../contexts/GlobalContext.js";
import { Link, useNavigate } from "react-router-dom";
import logo from "../assets/logo.png";
import backgroundImage from "../assets/login.png";
import { useForm } from "react-hook-form";
import { jwtDecode } from "jwt-decode";
import { toast, ToastContainer } from "react-toastify";

export default function LoginPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const navigate = useNavigate();
  const { setCurrentUser } = useContext(GlobalContext);
  const [errorMessage, setErrorMessage] = useState("");

  const onSubmit = async (data) => {
    try {
      const response = await fetch("http://localhost:8000/auth/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          username: data.username,
          password: data.password,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        setErrorMessage(errorData.detail || "Erro ao fazer login");
        throw new Error("Erro ao fazer login");
      }

      const result = await response.json();
      toast.success("Login bem sucedido");

      localStorage.setItem("access_token", result.access_token);
      const decodedToken = jwtDecode(result.access_token);
      const user = {
        username: decodedToken.sub,
      };
      setCurrentUser(user);
      localStorage.setItem("user", user.username);
      navigate(
        user.username === "katherine.corrales" ? "/calendario" : "/home",
      );
    } catch (error) {
      console.error("Erro ao enviar dados", error);
    }
  };

  return (
    <div
      className="flex items-center justify-center min-h-screen w-full bg-cover bg-no-repeat"
      style={{
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(${backgroundImage})`,
      }}
    >
      <div className="w-full max-w-xs mx-auto bg-transparent p-6 text-center">
        <form onSubmit={handleSubmit(onSubmit)}>
          <img
            src={logo}
            alt="Logo do site"
            className="w-40 h-auto mx-auto mb-12"
          />
          <div className="text-left">
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
              {...register("username", { required: "Usuário é obrigatório" })}
              className={`w-full h-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none ${errors.username ? "border-red-500" : ""}`}
            />
            {errors.username && (
              <p className="text-red-500 text-xs">{errors.username.message}</p>
            )}
          </div>
          <div className="relative w-full h-9 mb-6">
            <input
              type="password"
              placeholder="Senha"
              {...register("password", { required: "Senha é obrigatória" })}
              className={`w-full h-full bg-gray-50 bg-opacity-20 border border-white rounded-full text-sm px-5 py-2 text-white placeholder-white outline-none ${errors.password ? "border-red-500" : ""}`}
            />
            {errors.password && (
              <p className="text-red-500 text-xs">{errors.password.message}</p>
            )}
          </div>
          <button
            type="submit"
            className="w-full h-11 bg-yellow-300 border-none rounded-full shadow-lg cursor-pointer text-xs font-bold"
          >
            ENTRAR
          </button>
          <div className="mt-2 text-xs text-center">
            <Link to="/registro" className="text-white hover:underline">
              CADASTRE-SE
            </Link>
          </div>
          {errorMessage && (
            <div className=" text-red-500">
              <p className="text-xs">{errorMessage}</p>
            </div>
          )}
          <ToastContainer />
        </form>
      </div>
    </div>
  );
}
