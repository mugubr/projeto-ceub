import Header from "./Header";
import Content from "./Content";

export default function HomePage() {
  return (
    <div className="flex h-screen overflow-hidden">
      <div className="flex flex-col flex-1">
        <Header texto={"Bem vindo(a) de volta!"} />
        <Content>
          <h1> Miau </h1>
        </Content>
      </div>
    </div>
  );
}
