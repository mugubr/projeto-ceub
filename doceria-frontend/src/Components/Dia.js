import dayjs from "dayjs";
import React, { useContext, useState, useEffect } from "react";
import GlobalContext from "../Context/GlobalContext.js";
import { formatDate } from "../util.js";
import usePedidosByMes from "../hooks/usePedidosByMes.js"

const statusColors = {
  "Em andamento": "#F8EDCE", 
  "Entregue": "#D7EFD5",    
};

const statusColorsBar = {
  "Em andamento": "#EBB623", 
  "Entregue": "#61C354",    
};

export default function Dia({ day, rowIdx, mes}) {
  const [dayEvents, setDayEvents] = useState([]);
  const pedidos = usePedidosByMes(mes);

  const {
    setDaySelected,
    setShowEventModal,
    setSelectedEvent,
  } = useContext(GlobalContext);


  useEffect(() => {
    const dateKey = day.format("YYYY-MM-DD");
    setDayEvents(pedidos[dateKey] || []);
  }, [day, pedidos]);

  function getCurrentDayClass() {
    return day.format("DD-MM-YY") === dayjs().format("DD-MM-YY")
      ? "text-blue-600 font-bold"
      : "";
  }
  return (
    <div className="border border-gray-200 flex flex-col">
      <header className="flex flex-col items-center">
        {rowIdx === 0 && (
          <p className="text-sm mt-1">
            {formatDate(day, "ddd").toUpperCase()}
          </p>
        )}
        <p
          className={`text-sm p-1 my-1 text-center  ${getCurrentDayClass()}`}
        >
          {formatDate(day, "DD")}
        </p>
      </header>
      <div
        className="flex-1 cursor-pointer overflow-y-auto overflow-x-hidden"
        onClick={() => {
          setDaySelected(day);
          setShowEventModal(true);
        }}
      >
<div className="max-h-48 overflow-y-auto overflow-x-hidden">
          {dayEvents.map((evt, idx) => {
            const statusColor = statusColors[evt.status] || "#000000";
            const statusColorBar = statusColorsBar[evt.status] || "#000000";
            return (
              <div
                key={idx}
                onClick={() => setSelectedEvent(evt)}
                style={{ backgroundColor: statusColor }}
                className="w-full p-1 mr-3 text-sm truncate flex items-center relative"
              >
                <span
                  className="absolute left-0 top-0 h-full w-1"
                  style={{ backgroundColor: statusColorBar }}
                ></span>
                <div className="pl-2">{evt.nome}/{evt.ocasiao}</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}