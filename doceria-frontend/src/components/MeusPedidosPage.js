import Header from "./Header";
import Content from "./Content";
import MeusPedidos from "./MeusPedidos";
import Sidebar from "./Sidebar";

export default function HomePage() {
  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar />
      <div className="flex flex-col flex-1">
        <Header texto={"Meus Pedidos"} />
        <Content>
          <MeusPedidos />
        </Content>
      </div>
    </div>
  );
}
