import React, { useContext } from "react";
import GlobalContext from "../contexts/GlobalContext";
import { formatDateBR } from "../util";
import whatsapp from "../assets/whatsapp.png";
import { toast, ToastContainer } from "react-toastify";
export default function PedidoModal() {
  const { setShowPedidoModal, selectedPedido } = useContext(GlobalContext);
  const handleSendMessage = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/mensagens/enviar/${selectedPedido.celular}/1`,
      );
      if (!response.ok) {
        throw new Error("Erro ao enviar mensagem");
      }
      const result = await response.json();
      toast.success(result.message);
    } catch (error) {
      toast.error("Erro ao enviar mensagem");
    }
  };
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white rounded-lg shadow-2xl w-80 max-w-lg mx-4">
        <header className=" px-4 py-2 flex justify-between items-center rounded-t-lg">
          <h2 className="text-lg font-semibold">Pedido {selectedPedido.id}</h2>
          <button
            onClick={() => setShowPedidoModal(false)}
            className="text-gray-400 hover:text-gray-600"
          >
            <span className="material-icons-outlined">close</span>
          </button>
        </header>
        <div className="p-4">
          {selectedPedido ? (
            <div className="grid grid-cols-1 gap-y-4">
              <div className="flex justify-between">
                <p className="text-gray-500">Nº do pedido</p>
                <p>{selectedPedido.id || "N/A"}</p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Cliente</p>
                <p>{selectedPedido.nome || "N/A"}</p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Contato</p>
                <p>{selectedPedido.celular || "N/A"}</p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Tipo do evento</p>
                <p>{selectedPedido.ocasiao || "N/A"}</p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Data da entrega</p>
                <p>
                  {selectedPedido.data_entrega
                    ? formatDateBR(selectedPedido.data_entrega)
                    : "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Endereço</p>
                <p>
                  {selectedPedido.logradouro +
                    " " +
                    selectedPedido.bairro +
                    " " +
                    selectedPedido.numero_complemento || "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Valor</p>
                <p>
                  {selectedPedido.valor ? "R$" + selectedPedido.valor : "N/A"}
                </p>
              </div>
              <div>
                <p className="font-semibold">Descrição</p>
                <p>{selectedPedido.descricao || "N/A"}</p>
              </div>
            </div>
          ) : (
            <p>Nenhum pedido selecionado</p>
          )}
        </div>
        <footer className="flex justify-center p-4 rounded-b-lg">
          <img
            src={whatsapp}
            alt="whatsapp"
            className="w-8 h-8 cursor-pointer"
            onClick={handleSendMessage}
          />
        </footer>
      </div>
      <ToastContainer />
    </div>
  );
}
