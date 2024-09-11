import React, { useContext } from "react";
import GlobalContext from "../Context/GlobalContext";
export default function ContatoModal() {
  const { setShowContatoModal } = useContext(GlobalContext);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white rounded-lg shadow-2xl w-80 max-w-lg mx-4">
        <header className=" px-4 py-2 flex justify-between items-center rounded-t-lg">
          <h2 className="text-lg font-semibold">Contato</h2>
          <button
            onClick={() => setShowContatoModal(false)}
            className="text-gray-400 hover:text-gray-600"
          >
            <span className="material-icons-outlined">close</span>
          </button>
        </header>
        <div className="p-4">
          <div className="grid grid-cols-1 gap-y-4">
            <div className="flex justify-center flex-col items-center">
              <p>Instagram</p>
              <p className="text-gray-500">@katherinecorrales_doceria</p>
            </div>

            <div className="flex justify-center flex-col items-center">
              <p>Celular</p>
              <p className="text-gray-500">(61) 98497-2660</p>
            </div>

            <div className="flex justify-center flex-col items-center">
              <p>Encomendas</p>
              <ul className="flex flex-col justify-center items-center text-center">
                <li>
                  <p className="text-gray-500">
                    Prazo mínimo de uma semana de antecedência para realizar sua
                    encomenda;
                  </p>
                </li>
                <li>
                  <p className="text-gray-500">
                    Pedido mínimo de 25 unidades por sabor;
                  </p>
                </li>
              </ul>
            </div>
            <div className="flex justify-center flex-col items-center">
              <p>Retirada</p>
              <p className="text-gray-500">WMS 14 - Sobredinho</p>
              <p className="text-red-500">Horário agendado</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
