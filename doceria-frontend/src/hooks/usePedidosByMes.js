import dayjs from "dayjs";
import { useState, useEffect } from "react";

const apiUrl = "http://localhost:8000";

const ano = dayjs().year();

export default function usePedidosByMes(month) {
  const [pedidos, setPedidos] = useState({});

  useEffect(() => {
    async function fetchPedidos() {
      try {
        const response = await fetch(
          `${apiUrl}/pedidos/mes/${month}?ano=${ano}`,
        );
        const data = await response.json();

        const organizedPedidos = {};
        const { pedidos: pedidosPorDia } = data;

        Object.keys(pedidosPorDia).forEach((day) => {
          pedidosPorDia[day].forEach((pedido) => {
            const dateKey = dayjs(pedido.data_entrega).format("YYYY-MM-DD");
            if (!organizedPedidos[dateKey]) {
              organizedPedidos[dateKey] = [];
            }
            organizedPedidos[dateKey].push({
              ...pedido,
              label: "pedido",
            });
          });
        });

        setPedidos(organizedPedidos);
      } catch (error) {
        console.error("Erro ao recuperar os pedidos:", error);
      }
    }

    fetchPedidos();
  }, [month]);

  return pedidos;
}
