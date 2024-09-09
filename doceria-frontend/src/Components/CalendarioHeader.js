import dayjs from "dayjs";
import React, { useContext } from "react";
import GlobalContext from "../context/GlobalContext";
import { formatDate } from "../util.js";

export default function CalendarioHeader() {
  const { monthIndex, setMonthIndex } = useContext(GlobalContext);
  function handlePrevMonth() {
    setMonthIndex(monthIndex - 1);
  }
  function handleNextMonth() {
    setMonthIndex(monthIndex + 1);
  }
  function handleReset() {
    setMonthIndex(
      monthIndex === dayjs().month()
        ? monthIndex + Math.random()
        : dayjs().month()
    );
  }
  return (
    <header className="px-4 py-2 flex items-center justify-between bg-gray-200">
      <button
        onClick={handleReset}
        className="flex items-center justify-center border rounded-xl py-2 px-4 bg-gray-300"
      >
        Hoje
      </button>
      <div className="flex text-center items-center">

      <button onClick={handlePrevMonth} className="mx-2">
          <span className="material-icons-outlined text-gray-600">chevron_left</span>
        </button>
      <h2 className="ml-4 text-xl text-gray-500 font-bold">
    {formatDate(dayjs(new Date(dayjs().year(), monthIndex)), "MMMM YYYY").replace(/^\w/, c => c.toUpperCase())}
      </h2>
      <button onClick={handleNextMonth} className="mx-2">
          <span className="material-icons-outlined text-gray-600">chevron_right</span>
        </button>
      </div>
    </header>
  );
}