import Calendario from "./components/Calendario";
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import Content from './components/Content';


function App() {
  return (
    <div className="flex h-screen overflow-hidden">
    <Sidebar nome={'Teste'}/>
    <div className="flex flex-col flex-1">
        <Header texto={'Teste'} />
        <Content>
            <Calendario/>
        </Content>
    </div>
</div>
  );
}

export default App;
