import React, { useContext } from "react";
import GlobalContext from "../Context/GlobalContext";
import { formatDateBR } from "../util";
export default function PedidoModal() {
  const { setShowPedidoModal, selectedEvent } = useContext(GlobalContext);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white rounded-lg shadow-2xl w-80 max-w-lg mx-4">
        <header className=" px-4 py-2 flex justify-between items-center rounded-t-lg">
          <h2 className="text-lg font-semibold">Pedido {selectedEvent.id}</h2>
          <button
            onClick={() => setShowPedidoModal(false)}
            className="text-gray-400 hover:text-gray-600"
          >
            <span className="material-icons-outlined">close</span>
          </button>
        </header>
        <div className="p-4">
          {selectedEvent ? (
            <div className="grid grid-cols-1 gap-y-4">
              <div className="flex justify-between">
                <p className="text-gray-500">Nº do pedido</p>
                <p>{selectedEvent.id || "N/A"}</p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Cliente</p>
                <p>{selectedEvent.nome || "N/A"}</p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Contato</p>
                <p>{selectedEvent.celular || "N/A"}</p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Tipo do evento</p>
                <p>{selectedEvent.ocasiao || "N/A"}</p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Data da entrega</p>
                <p>
                  {selectedEvent.data_entrega
                    ? formatDateBR(selectedEvent.data_entrega)
                    : "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Endereço</p>
                <p>
                  {selectedEvent.logradouro +
                    " " +
                    selectedEvent.bairro +
                    " " +
                    selectedEvent.numero_complemento || "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className="text-gray-500">Valor</p>
                <p>
                  {selectedEvent.valor ? "R$" + selectedEvent.valor : "N/A"}
                </p>
              </div>
              <div>
                <p className="font-semibold">Descrição</p>
                <p>{selectedEvent.descricao || "N/A"}</p>
              </div>
            </div>
          ) : (
            <p>Nenhum pedido selecionado</p>
          )}
        </div>
        <footer className="flex justify-center p-4 rounded-b-lg">
          <button
            type="button"
            onClick={() => setShowPedidoModal(false)}
            className="bg-blue-500 hover:bg-blue-600 px-6 py-2 rounded text-white"
          >
            Fechar
          </button>
        </footer>
      </div>
    </div>
  );
}
