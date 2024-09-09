import React, { useContext} from "react";
import GlobalContext from "../Context/GlobalContext";


export default function PedidoModal() {
  const {
    setShowEventModal,
    selectedEvent,
  } = useContext(GlobalContext);



  return (
    <div className="h-screen w-full fixed left-0 top-0 flex justify-center items-center">
      <form className="bg-white rounded-lg shadow-2xl w-1/4">
        <header className="bg-white px-4 py-2 flex justify-between items-center">
          <h2 className="text-lg font-semibold">Pedido {selectedEvent.id}</h2>
          <div>
            <button onClick={() => setShowEventModal(false)}>
              <span className="material-icons-outlined text-gray-400">
                close
              </span>
            </button>
          </div>
        </header>
        <div className="p-3">
        {selectedEvent ? (
            <div className="grid grid-cols-1 gap-y-4">
              <div className="flex justify-between">
                <p className=" text-gray-400">
                Nº do pedido
                </p>
                <p>
                {selectedEvent.id || "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className=" text-gray-400">
                Cliente
                </p>
                <p>
                {selectedEvent.nome || "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className=" text-gray-400">
                Contato
                </p>
                <p>
                {selectedEvent.celular || "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className=" text-gray-400">
                Tipo do evento
                </p>
                <p>
                {selectedEvent.ocasiao || "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className=" text-gray-400">
                Data da entrega
                </p>
                <p>
                {selectedEvent.data_entrega || "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className=" text-gray-400">
                Endereço
                </p>
                <p>
                {selectedEvent.logradouro +" "+ selectedEvent.bairro +" "+  selectedEvent.numero_complemento || "N/A"}
                </p>
              </div>
              <div className="flex justify-between">
                <p className=" text-gray-400">
                Valor
                </p>
                <p>
                {"R$" + selectedEvent.valor || "N/A"}
                </p>
              </div>
              <div>
                <p>
                Descrição
                </p>
                <p>
                {selectedEvent.descricao || "N/A"}
                </p>
              </div>
            </div>
          ) : (
            <p>Nenhum pedido selecionado</p>
          )}
        </div>
        <footer className="flex justify-center p-3 mt-5">
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-600 px-6 py-2 rounded text-white"
          >
            Save
          </button>
        </footer>
      </form>
    </div>
  );
}