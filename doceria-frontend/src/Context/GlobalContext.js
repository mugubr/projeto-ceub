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
  showRealizarPedidoModal: false,
  setShowRealizarPedidoModal: () => {},
  selectedPedido: null,
  setSelectedPedido: () => {},
  currentUser: null,
  setCurrentUser: (user) => {},
  currentCliente: null,
  setCurrentCliente: () => {},
  botaoAtivo: false,
  setBotaoAtivo: () => {},
});

export default GlobalContext;
