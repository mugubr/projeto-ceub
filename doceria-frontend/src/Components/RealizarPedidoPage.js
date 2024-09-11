import Header from "./Header";
import Content from "./Content";
import RealizarPedido from "./RealizarPedido";
import Sidebar from "./Sidebar";

export default function RealizarPedidoPage() {
  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar />
      <div className="flex flex-col flex-1">
        <Header texto={"Realizar Pedido"} />
        <Content>
          <RealizarPedido />
        </Content>
      </div>
    </div>
  );
}
