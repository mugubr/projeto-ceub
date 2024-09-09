import Calendario from "./Components/Calendario";
import Sidebar from './Components/Sidebar';
import Header from './Components/Header';
import Content from './Components/Content';

function App() {
  return (
    <div className="flex h-screen overflow-hidden">
    <Sidebar nome={'Teste'}/>
    <div className="flex flex-col flex-1">
        <Header texto={'Calendário'} />
        <Content>
            <Calendario/>
        </Content>
    </div>
</div>
  );
}

export default App;
