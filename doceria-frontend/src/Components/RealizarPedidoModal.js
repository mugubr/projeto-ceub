import React, { useContext, useState } from "react";
import GlobalContext from "../contexts/GlobalContext";
import { toast, ToastContainer } from "react-toastify";

export default function RealizarPedidoModal({ totalCompra, produtos }) {
  const {
    showRealizarPedidoModal,
    setShowRealizarPedidoModal,
    setBotaoAtivo,
    setCarrinho,
  } = useContext(GlobalContext);
  const cliente_id = localStorage.getItem("cliente_id");
  const nome = localStorage.getItem("nome");
  const celular = localStorage.getItem("celular");
  const [formData, setFormData] = useState({
    cliente_id: cliente_id,
    ocasiao: "",
    data_entrega: "",
    logradouro: "",
    bairro: "",
    numero_complemento: "",
    ponto_referencia: "",
    produtos: produtos,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    console.log(JSON.stringify(formData));
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/pedidos", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        toast.error(errorData.detail || "Erro ao cadastrar pedido");
        return;
      }
      toast.success("Pedido realizado com sucesso!");

      await new Promise((resolve) => setTimeout(resolve, 1500));

      setCarrinho({
        cliente_id: cliente_id,
        data_entrega: "",
        ocasiao: "",
        bairro: "",
        logradouro: "",
        numero_complemento: "",
        ponto_referencia: "",
        produtos: [],
      });
      setShowRealizarPedidoModal(false);
      setBotaoAtivo(false);
    } catch (error) {
      console.error("Erro ao cadastrar o pedido:", error);
      toast.error("Erro ao cadastrar o pedido");
    }
  };

  const handleCancel = () => {
    setCarrinho({
      cliente_id: cliente_id,
      data_entrega: "",
      ocasiao: "",
      bairro: "",
      logradouro: "",
      numero_complemento: "",
      ponto_referencia: "",
      produtos: [],
    });

    setShowRealizarPedidoModal(false);

    setBotaoAtivo(false);
  };
  return (
    <>
      <ToastContainer />
      {showRealizarPedidoModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
          <div className="bg-white rounded-lg shadow-2xl w-full max-w-lg mx-4">
            <header className="px-4 py-2 flex justify-between items-center rounded-t-lg">
              <h2 className="text-lg font-semibold">Confirmar pedido</h2>
            </header>
            <form onSubmit={handleSubmit}>
              <div className="p-4">
                <div className=" mt-4 flex items-center justify-between">
                  <p className="block text-gray-500">Cliente</p>
                  <p className="text-lg font-semibold">{nome}</p>
                </div>
                <div className=" mt-4 flex items-center justify-between">
                  <p className="block text-gray-500">Contato</p>
                  <p className="text-lg font-semibold">{celular}</p>
                </div>
                <div className="mt-4 flex items-center justify-between">
                  <label htmlFor="ocasiao" className="block text-gray-500">
                    Tipo de evento
                  </label>
                  <input
                    type="text"
                    id="ocasiao"
                    name="ocasiao"
                    required
                    value={formData.ocasiao}
                    onChange={handleChange}
                    className="w-80 p-2 border border-gray-300 rounded mt-1"
                  />
                </div>
                <div className="mt-4 flex items-center justify-between">
                  <label htmlFor="data_entrega" className="block text-gray-500">
                    Data da entrega
                  </label>
                  <input
                    type="date"
                    id="data_entrega"
                    name="data_entrega"
                    required
                    value={formData.data_entrega}
                    onChange={handleChange}
                    className="w-80 p-2 border border-gray-300 rounded mt-1"
                  />
                </div>
                <span className="text-xs text-red-500">
                  {" "}
                  * Prazo mínimo de uma semana
                </span>
                <div className="mt-4 flex items-center justify-between">
                  <label htmlFor="logradouro" className="block text-gray-500">
                    Logradouro
                  </label>
                  <input
                    type="text"
                    id="logradouro"
                    name="logradouro"
                    required
                    value={formData.logradouro}
                    onChange={handleChange}
                    className="w-80 p-2 border border-gray-300 rounded mt-1"
                  />
                </div>
                <div className="mt-4 flex items-center justify-between">
                  <label htmlFor="bairro" className="block text-gray-500">
                    Bairro
                  </label>
                  <input
                    type="text"
                    id="bairro"
                    name="bairro"
                    required
                    value={formData.bairro}
                    onChange={handleChange}
                    className="w-80 p-2 border border-gray-300 rounded mt-1"
                  />
                </div>
                <div className="mt-4 flex items-center justify-between">
                  <label
                    htmlFor="numero_complemento"
                    className="block text-gray-500"
                  >
                    Complemento
                  </label>
                  <input
                    type="text"
                    id="numero_complemento"
                    name="numero_complemento"
                    required
                    value={formData.numero_complemento}
                    onChange={handleChange}
                    className="w-80 p-2 border border-gray-300 rounded mt-1"
                  />
                </div>
                <div className="mt-4 flex items-center justify-between">
                  <label
                    htmlFor="ponto_referencia"
                    className="block text-gray-500"
                  >
                    Ponto de referência
                  </label>
                  <input
                    type="text"
                    id="ponto_referencia"
                    name="ponto_referencia"
                    required
                    value={formData.ponto_referencia}
                    onChange={handleChange}
                    className="w-80 p-2 border border-gray-300 rounded mt-1"
                  />
                </div>
                <div className=" mt-4 flex items-center justify-between">
                  <p className="block text-gray-500">Valor</p>
                  <p className="text-lg font-semibold">
                    R$ {totalCompra.toFixed(2)}
                  </p>
                </div>
              </div>
              <footer className="flex justify-around p-4 rounded-b-lg">
                <button
                  type="submit"
                  className="bg-yellow-500 text-black py-2 px-4 rounded-lg font-bold"
                >
                  Confirmar
                </button>
                <button
                  type="button"
                  onClick={handleCancel}
                  className="bg-gray-100 text-red-500 py-2 px-4 rounded-lg font-bold"
                >
                  Cancelar
                </button>
              </footer>
            </form>
          </div>
        </div>
      )}
    </>
  );
}
