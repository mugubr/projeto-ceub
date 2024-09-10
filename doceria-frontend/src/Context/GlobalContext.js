import React from "react";

const GlobalContext = React.createContext({
  monthIndex: 0,
  setMonthIndex: (index) => {},
  smallCalendarMonth: 0,
  setSmallCalendarMonth: (index) => {},
  daySelected: null,
  setDaySelected: (day) => {},
  showPedidoModal: false,
  setShowPedidoModal: () => {},
  selectedEvent: null,
  setSelectedEvent: () => {},
  currentUser: null,
  setCurrentUser: (user) => {},
});

export default GlobalContext;
