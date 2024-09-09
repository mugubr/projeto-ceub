import React, { useState, useContext, useEffect } from "react";
import GlobalContext from "../Context/GlobalContext";
import { getMonth } from "../util.js";
import CalendarioHeader from "./CalendarioHeader";
import EventoModal from "./EventoModal.js";
import Mes from "./Mes.js";
export default function Calendario() {
    const [currentMonth, setCurrentMonth] = useState(getMonth());
    const { monthIndex, showEventModal } = useContext(GlobalContext);
  
    useEffect(() => {
      setCurrentMonth(getMonth(monthIndex));
    }, [monthIndex]);

    return (
        <>
        {showEventModal && <EventoModal />}
        <div className="h-screen flex flex-col">
        <CalendarioHeader />
        <div className="flex flex-1">
          <Mes month={currentMonth} />
        </div>
      </div>
        
        </>
    )
}
