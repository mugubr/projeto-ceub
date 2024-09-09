import dayjs from "dayjs";
import React, { useContext, useEffect, useState } from "react";
import GlobalContext from "../Context/GlobalContext";
import { getMonth } from "../util";
import { formatDate } from "../util.js";


export default function CalendarioAuxiliar() {
  const [currentMonthIdx, setCurrentMonthIdx] = useState(
    dayjs().month()
  );
  const [currentMonth, setCurrentMonth] = useState(getMonth());
  useEffect(() => {
    setCurrentMonth(getMonth(currentMonthIdx));
  }, [currentMonthIdx]);

  const {
    monthIndex,
    setSmallCalendarMonth,
    setDaySelected,
  } = useContext(GlobalContext);

  useEffect(() => {
    setCurrentMonthIdx(monthIndex);
  }, [monthIndex]);

  function handlePrevMonth() {
    setCurrentMonthIdx(currentMonthIdx - 1);
  }
  function handleNextMonth() {
    setCurrentMonthIdx(currentMonthIdx + 1);
  }
  function getDayClass(day) {
    const format = "DD-MM-YY";
    const nowDay = dayjs().format(format);
    const currDay = day.format(format);
    if (nowDay === currDay) {
      return "bg-blue-500 rounded-full text-white";
    }  else {
      return "";
    }
  }
  return (
    <div className="mt-9 w-full">
      <header>
 
        <div className="flex">
          <button onClick={handlePrevMonth}>
            <span className="material-icons-outlined cursor-pointer text-white">
              chevron_left
            </span>
          </button>
          <p className="text-white font-bold text-sm">
          {formatDate(dayjs(new Date(dayjs().year(), currentMonthIdx)), "MMMM YYYY").replace(/^\w/, c => c.toUpperCase())}
        </p>
          <button onClick={handleNextMonth}>
            <span className="material-icons-outlined cursor-pointer text-white">
              chevron_right
            </span>
          </button>
        </div>
      </header>
      <div className="grid grid-cols-7 text-center">
        {currentMonth[0].map((day, i) => (
          <span key={i} className="text-sm py-1 text-center text-gray-400">
            {formatDate(day, "dd")}
          </span>
        ))}
        {currentMonth.map((row, i) => (
          <React.Fragment key={i}>
            {row.map((day, idx) => (
              <button
                key={idx}
                onClick={() => {
                  setSmallCalendarMonth(currentMonthIdx);
                  setDaySelected(day);
                }}
                className={`py-2 w-full ${getDayClass(day)} ${day.day() === 0 || day.day() === 6 ? "text-blue-700" : ""}`}
              >
                <span className="text-xs">{day.format("D")}</span>
              </button>
            ))}
          </React.Fragment>
        ))}
      </div>
    </div>
  );
}