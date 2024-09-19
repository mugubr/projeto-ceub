import React, { useState, useContext, useEffect } from "react";
import GlobalContext from "../contexts/GlobalContext.js";
import { getMonth } from "../util.js";
import CalendarioHeader from "./CalendarioHeader.js";
import PedidoModal from "./PedidoModal.js";
import Mes from "./Mes.js";
import usePedidosByMes from "../hooks/usePedidosByMes.js";

export default function Calendario() {
  const [currentMonth, setCurrentMonth] = useState(getMonth());
  const { monthIndex, showPedidoModal } = useContext(GlobalContext);
  const pedidos = usePedidosByMes(monthIndex + 1);

  useEffect(() => {
    setCurrentMonth(getMonth(monthIndex));
  }, [monthIndex]);

  return (
    <>
      {showPedidoModal && <PedidoModal />}
      <div className="flex flex-col h-full">
        <CalendarioHeader />
        <div className="flex flex-1 overflow-auto">
          <Mes month={currentMonth} pedidos={pedidos} />
        </div>
      </div>
    </>
  );
}
