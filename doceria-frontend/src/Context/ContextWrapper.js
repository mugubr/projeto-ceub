import React, { useState, useEffect } from "react";
import GlobalContext from "./GlobalContext.js";
import dayjs from "dayjs";

export default function ContextWrapper(props) {
  const [monthIndex, setMonthIndex] = useState(dayjs().month());
  const [smallCalendarMonth, setSmallCalendarMonth] = useState(null);
  const [daySelected, setDaySelected] = useState(dayjs());
  const [showPedidoModal, setShowPedidoModal] = useState(false);
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    if (smallCalendarMonth !== null) {
      setMonthIndex(smallCalendarMonth);
    }
  }, [smallCalendarMonth]);

  useEffect(() => {
    if (!showPedidoModal) {
      setSelectedEvent(null);
    }
  }, [showPedidoModal]);

  return (
    <GlobalContext.Provider
      value={{
        monthIndex,
        setMonthIndex,
        smallCalendarMonth,
        setSmallCalendarMonth,
        daySelected,
        setDaySelected,
        showPedidoModal,
        setShowPedidoModal,
        selectedEvent,
        setSelectedEvent,
        currentUser,
        setCurrentUser,
      }}
    >
      {props.children}
    </GlobalContext.Provider>
  );
}
