import Calendario from "./Calendario";
import CalendarioSidebar from "./CalendarioSidebar";
import Header from "./Header";
import Content from "./Content";

export default function CalendarioPage() {
  return (
    <div className="flex h-screen overflow-hidden">
      <CalendarioSidebar />
      <div className="flex flex-col flex-1">
        <Header texto={"Calendário"} />
        <Content>
          <Calendario />
        </Content>
      </div>
    </div>
  );
}
