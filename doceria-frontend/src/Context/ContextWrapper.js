import React, { useState, useEffect } from "react";
import GlobalContext from "./GlobalContext.js";
import dayjs from "dayjs";

export default function ContextWrapper(props) {
  const [monthIndex, setMonthIndex] = useState(dayjs().month());
  const [smallCalendarMonth, setSmallCalendarMonth] = useState(null);
  const [daySelected, setDaySelected] = useState(dayjs());
  const [showPedidoModal, setShowPedidoModal] = useState(false);
  const [showRealizarPedidoModal, setShowRealizarPedidoModal] = useState(false);
  const [selectedPedido, setSelectedPedido] = useState(null);
  const [currentUser, setCurrentUser] = useState();
  const [currentCliente, setCurrentCliente] = useState();
  const [botaoAtivo, setBotaoAtivo] = useState(false);
  const cliente_id = localStorage.getItem("cliente_id");
  const [carrinho, setCarrinho] = useState({
    cliente_id: cliente_id,
    data_entrega: "",
    ocasiao: "",
    bairro: "",
    logradouro: "",
    numero_complemento: "",
    ponto_referencia: "",
    produtos: [],
  });

  useEffect(() => {
    if (smallCalendarMonth !== null) {
      setMonthIndex(smallCalendarMonth);
    }
  }, [smallCalendarMonth]);

  useEffect(() => {
    if (!showPedidoModal) {
      setSelectedPedido(null);
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
        selectedPedido,
        setSelectedPedido,
        currentUser,
        setCurrentUser,
        showRealizarPedidoModal,
        setShowRealizarPedidoModal,
        botaoAtivo,
        setBotaoAtivo,
        currentCliente,
        setCurrentCliente,
        carrinho,
        setCarrinho,
      }}
    >
      {props.children}
    </GlobalContext.Provider>
  );
}
