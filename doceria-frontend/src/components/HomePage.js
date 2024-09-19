import Header from "./Header";
import Content from "./Content";
import Home from "./Home";
import Sidebar from "./Sidebar";

export default function HomePage() {
  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar />
      <div className="flex flex-col flex-1">
        <Header texto={"Bem vindo(a) de volta!"} />
        <Content>
          <Home />
        </Content>
      </div>
    </div>
  );
}
