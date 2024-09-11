import React, { useState, useEffect } from "react";
import { formatDateBR } from "../util";

export default function MeusPedidos() {
  const [pedidos, setPedidos] = useState([]);
  const cliente_id = localStorage.getItem("cliente_id");
  useEffect(() => {
    const fetchPedidos = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/pedidos/cliente/${cliente_id}`,
        );
        const data = await response.json();
        setPedidos(data.pedidos);
      } catch (error) {
        console.error("Erro ao buscar pedidos:", error);
      }
    };

    fetchPedidos();
  }, [cliente_id]);

  return (
    <div className="container mx-auto px-4 py-8 bg-gray-100 h-full overflow-y-auto">
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white border border-gray-300 rounded-lg shadow">
          <thead>
            <tr>
              <th className="px-4 py-2 bg-gray-200 text-center text-sm font-semibold text-gray-600">
                Número do Pedido
              </th>
              <th className="px-4 py-2 bg-gray-200 text-center text-sm font-semibold text-gray-600">
                Data
              </th>
              <th className="px-4 py-2 bg-gray-200 text-center text-sm font-semibold text-gray-600">
                Endereço
              </th>
              <th className="px-4 py-2 bg-gray-200 text-center text-sm font-semibold text-gray-600">
                Valor
              </th>
              <th className="px-4 py-2 bg-gray-200 text-center text-sm font-semibold text-gray-600">
                Status
              </th>
              <th className="px-4 py-2 bg-gray-200 text-center text-sm font-semibold text-gray-600">
                Data da Entrega
              </th>
            </tr>
          </thead>
          <tbody>
            {pedidos.length > 0 ? (
              pedidos.map((pedido) => (
                <tr key={pedido.id} className="border-t border-gray-300">
                  <td className="px-4 py-2 text-sm text-center  text-gray-800">
                    {pedido.id}
                  </td>
                  <td className="px-4 py-2 text-sm text-center  text-gray-800">
                    {formatDateBR(pedido.criado_em)}
                  </td>
                  <td className="px-4 py-2 text-sm text-center  text-gray-800">
                    {pedido.logradouro +
                      " " +
                      pedido.bairro +
                      " " +
                      pedido.numero_complemento}
                  </td>
                  <td className="px-4 py-2 text-sm text-center  text-gray-800">
                    {"R$" + pedido.valor}
                  </td>
                  <td className="px-4 py-2 text-sm text-center  text-gray-800">
                    {pedido.status}
                  </td>
                  <td className="px-4 py-2 text-sm text-center  text-gray-800">
                    {formatDateBR(pedido.data_entrega)}
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" className="px-4 py-2 text-center text-gray-500">
                  Nenhum pedido encontrado
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
