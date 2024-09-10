import React from "react";
import Dia from "./Dia.js";
import dayjs from "dayjs";

export default function Mes({ month }) {
  const mes = dayjs().month() + 1;
  return (
    <div className="flex-1 grid grid-cols-7 grid-rows-5 p-2">
      {month.map((row, i) => (
        <React.Fragment key={i}>
          {row.map((day, idx) => (
            <Dia day={day} key={idx} rowIdx={i} mes={mes} />
          ))}
        </React.Fragment>
      ))}
    </div>
  );
}
