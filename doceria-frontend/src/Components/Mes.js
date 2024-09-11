import React from "react";
import Dia from "./Dia.js";

export default function Mes({ month, pedidos }) {
  return (
    <div className="flex-1 grid grid-cols-7 grid-rows-5 p-2">
      {month.map((row, i) => (
        <React.Fragment key={i}>
          {row.map((day, idx) => (
            <Dia day={day} key={idx} rowIdx={i} pedidos={pedidos} />
          ))}
        </React.Fragment>
      ))}
    </div>
  );
}
