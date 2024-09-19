import React, { useState, useEffect, useContext } from "react";
import brigadeiro from "../assets/brigadeiro.png";
import DoceCard from "./DoceCard";
import GlobalContext from "../contexts/GlobalContext";
import ContatoModal from "./ContatoModal";
import { NavLink } from "react-router-dom";

export default function Home() {
  const [produtos, setProdutos] = useState([]);
  const user = localStorage.getItem("user");
  const { showContatoModal, setShowContatoModal } = useContext(GlobalContext);
  useEffect(() => {
    async function fetchCliente() {
      try {
        const response = await fetch(
          `http://localhost:8000/clientes/usuario/${user}`,
        );
        const data = await response.json();
        localStorage.setItem("cliente_id", data.id);
        localStorage.setItem("nome", data.nome);
        localStorage.setItem("celular", data.celular);
      } catch (error) {
        console.error("Erro ao recuperar o cliente:", error);
      }
    }

    fetchCliente();
  }, [user]);

  useEffect(() => {
    const fetchProdutos = async () => {
      try {
        const response = await fetch("http://localhost:8000/produtos");
        const data = await response.json();
        setProdutos(data.produtos);
      } catch (error) {
        console.error("Erro ao buscar produtos:", error);
      }
    };

    fetchProdutos();
  }, []);
  return (
    <>
      {showContatoModal && <ContatoModal />}
      <div className="w-full h-full flex flex-col bg-gray-100 overflow-hidden">
        <main className="flex-1 p-6 overflow-auto">
          <section className="grid grid-cols-1 gap-6 mb-12 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-3">
            <div className="flex flex-col items-center bg-white shadow-md rounded-md p-4">
              <div className="bg-yellow-400 text-white p-4 rounded-lg mb-4 flex items-center justify-center shadow-lg">
                <span className="material-icons-outlined text-white text-3xl">
                  shopping_cart
                </span>
              </div>
              <NavLink
                to="/realizar-pedido"
                className="text-gray-700 font-semibold text-center"
              >
                Realizar Pedido
              </NavLink>
            </div>

            <div className="flex flex-col items-center bg-white shadow-md rounded-md p-4">
              <div className="bg-yellow-400 text-white p-4 rounded-lg mb-4 flex items-center justify-center shadow-lg">
                <span className="material-icons-outlined text-white text-3xl">
                  list_alt
                </span>
              </div>
              <NavLink
                to="/meus-pedidos"
                className="text-gray-700 font-semibold text-center"
              >
                Meus Pedidos
              </NavLink>
            </div>

            <div className="flex flex-col items-center bg-white shadow-md rounded-md p-4">
              <div className="bg-yellow-400 text-white p-4 rounded-lg mb-4 flex items-center justify-center shadow-lg">
                <span className="material-icons-outlined text-white text-3xl">
                  contact_support
                </span>
              </div>
              <a
                href="#!"
                onClick={() => setShowContatoModal(true)}
                className="text-gray-700 font-semibold text-center"
              >
                Contato
              </a>
            </div>
          </section>

          <div className="bg-white p-4 rounded-md shadow-lg mb-6">
            <section className="overflow-x-auto">
              <h2 className="text-xl font-semibold text-gray-700 mb-6">
                Novidades
              </h2>
              <div className="flex flex-wrap gap-6 justify-center">
                {produtos.slice(0, 3).map((produto) => (
                  <DoceCard
                    key={produto.id}
                    img={produto.imagem || brigadeiro}
                    nome={produto.nome}
                    vegano={produto.vegano}
                    gluten={produto.gluten}
                    lactose={produto.lactose}
                    preco={`R$ ${produto.preco}`}
                    adicionarAoCarrinho={() => {}}
                    quantidades={{}}
                    setQuantidades={() => {}}
                    isRealizarPedido={false}
                  />
                ))}
              </div>
            </section>
          </div>

          <div className="bg-white p-4 rounded-md shadow-lg">
            <section className="overflow-x-auto">
              <h2 className="text-xl font-semibold text-gray-700 mb-6">
                Outros Produtos
              </h2>
              <div className="flex flex-wrap gap-6 justify-center">
                {produtos.slice(3).map((produto) => (
                  <DoceCard
                    key={produto.id}
                    id={produto.id}
                    img={produto.imagem || brigadeiro}
                    nome={produto.nome}
                    vegano={produto.vegano}
                    gluten={produto.gluten}
                    lactose={produto.lactose}
                    preco={`R$ ${produto.preco}`}
                    adicionarAoCarrinho={() => {}}
                    quantidades={{}}
                    setQuantidades={() => {}}
                    isRealizarPedido={false}
                  />
                ))}
              </div>
            </section>
          </div>
        </main>
      </div>
    </>
  );
}
