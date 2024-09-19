import dayjs from "dayjs";
import React, { useContext } from "react";
import GlobalContext from "../contexts/GlobalContext.js";
import { formatDate } from "../util.js";

export default function CalendarioHeader() {
  const { monthIndex, setMonthIndex } = useContext(GlobalContext);

  function handlePrevMonth() {
    setMonthIndex((prevIndex) => prevIndex - 1);
  }

  function handleNextMonth() {
    setMonthIndex((prevIndex) => prevIndex + 1);
  }

  function handleReset() {
    setMonthIndex(dayjs().month());
  }

  return (
    <header className="px-4 py-2 flex items-center justify-between bg-yellow-400">
      <button
        onClick={handleReset}
        className="flex items-center justify-center border-black rounded-xl py-2 px-4 bg-yellow-500"
      >
        Hoje
      </button>
      <div className="flex text-center items-center">
        <button onClick={handlePrevMonth} className="mx-2">
          <span className="material-icons-outlined ">chevron_left</span>
        </button>
        <h2 className="ml-4 text-xl  font-bold">
          {formatDate(
            dayjs(new Date(dayjs().year(), monthIndex)),
            "MMMM YYYY",
          ).replace(/^\w/, (c) => c.toUpperCase())}
        </h2>
        <button onClick={handleNextMonth} className="mx-2">
          <span className="material-icons-outlined ">chevron_right</span>
        </button>
      </div>
    </header>
  );
}
