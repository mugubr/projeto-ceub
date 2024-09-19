import React, { useState, useEffect, useContext } from "react";
import DoceCard from "./DoceCard";
import brigadeiro from "../assets/brigadeiro.png";
import GlobalContext from "../contexts/GlobalContext";
import { toast, ToastContainer } from "react-toastify";
import RealizarPedidoModal from "./RealizarPedidoModal";

export default function RealizarPedido() {
  const [quantidades, setQuantidades] = useState({});
  const [produtos, setProdutos] = useState([]);
  const [totalCompra, setTotalCompra] = useState(0);
  const {
    botaoAtivo,
    setBotaoAtivo,
    showRealizarPedidoModal,
    setShowRealizarPedidoModal,
    carrinho,
    setCarrinho,
  } = useContext(GlobalContext);
  useEffect(() => {
    const fetchProdutos = async () => {
      try {
        const response = await fetch("http://localhost:8000/produtos");
        const data = await response.json();
        setProdutos(data.produtos);
        setQuantidades(
          data.produtos.reduce((acc, produto) => {
            acc[produto.id] = 1;
            return acc;
          }, {}),
        );
      } catch (error) {
        console.error("Erro ao buscar produtos:", error);
      }
    };

    fetchProdutos();
  }, []);
  useEffect(() => {
    const calcularTotal = () => {
      const total = carrinho.produtos.reduce((acc, item) => {
        const produto = produtos.find((p) => p.id === item.produto_id);
        return acc + (produto ? produto.preco * item.quantidade : 0);
      }, 0);
      setTotalCompra(total);
    };
    calcularTotal();
  }, [carrinho, produtos]);

  const adicionarAoCarrinho = (produto_id, quantidade) => {
    if (quantidade >= 25) {
      setCarrinho((prevCarrinho) => {
        const produtosAtuais = prevCarrinho.produtos || [];

        const produtoExistente = produtosAtuais.find(
          (item) => item.produto_id === produto_id,
        );

        if (produtoExistente) {
          return {
            ...prevCarrinho,
            produtos: produtosAtuais.map((item) =>
              item.produto_id === produto_id ? { ...item, quantidade } : item,
            ),
          };
        } else {
          return {
            ...prevCarrinho,
            produtos: [...produtosAtuais, { produto_id, quantidade }],
          };
        }
      });

      setBotaoAtivo(true);
    } else {
      setBotaoAtivo(false);
      toast.error(
        "É necessário selecionar pelo menos 25 unidades de um único produto.",
      );
    }
  };

  const handleConcluirPedido = () => {
    if (botaoAtivo) {
      setShowRealizarPedidoModal(true);
    }
  };

  return (
    <>
      {showRealizarPedidoModal && (
        <RealizarPedidoModal
          totalCompra={totalCompra}
          produtos={carrinho.produtos}
        />
      )}
      <div className="w-full h-full flex flex-col bg-gray-100 overflow-hidden">
        <main className="flex-1 p-6 overflow-auto">
          <div className="bg-white p-4 rounded-md shadow-lg mb-6">
            <section className="overflow-x-auto">
              <h2 className="text-xl font-semibold text-gray-700 mb-6">
                Novidades
              </h2>
              <div className="flex flex-wrap gap-6 justify-center">
                {produtos.slice(0, 3).map((produto) => (
                  <DoceCard
                    key={produto.id}
                    id={produto.id}
                    img={produto.imagem || brigadeiro}
                    nome={produto.nome}
                    vegano={produto.vegano}
                    gluten={produto.gluten}
                    lactose={produto.lactose}
                    preco={`R$ ${produto.preco}`}
                    adicionarAoCarrinho={adicionarAoCarrinho}
                    quantidades={quantidades}
                    setQuantidades={setQuantidades}
                    isRealizarPedido={true}
                  />
                ))}
              </div>
            </section>
          </div>

          <div className="bg-white p-4 rounded-md shadow-lg mb-6">
            <section className="overflow-x-auto">
              <h2 className="text-xl font-semibold text-gray-700 mb-6">
                Mais vendidos
              </h2>
              <div className="flex flex-wrap gap-6 justify-center">
                {produtos.slice(3, 6).map((produto) => (
                  <DoceCard
                    key={produto.id}
                    id={produto.id}
                    img={produto.imagem || brigadeiro}
                    nome={produto.nome}
                    vegano={produto.vegano}
                    gluten={produto.gluten}
                    lactose={produto.lactose}
                    preco={`R$ ${produto.preco}`}
                    adicionarAoCarrinho={adicionarAoCarrinho}
                    quantidades={quantidades}
                    setQuantidades={setQuantidades}
                    isRealizarPedido={true}
                  />
                ))}
              </div>
            </section>
          </div>

          <div className="bg-white p-4 rounded-md shadow-lg">
            <section className="overflow-x-auto">
              <h2 className="text-xl font-semibold text-gray-700 mb-6">
                Outros
              </h2>
              <div className="flex flex-wrap gap-6 justify-center">
                {produtos.slice(6).map((produto) => (
                  <DoceCard
                    key={produto.id}
                    id={produto.id}
                    img={produto.imagem || brigadeiro}
                    nome={produto.nome}
                    vegano={produto.vegano}
                    gluten={produto.gluten}
                    lactose={produto.lactose}
                    preco={`R$ ${produto.preco}`}
                    adicionarAoCarrinho={adicionarAoCarrinho}
                    quantidades={quantidades}
                    setQuantidades={setQuantidades}
                    isRealizarPedido={true}
                  />
                ))}
              </div>
            </section>
          </div>

          <button
            className={` flex items-center justify-center w-48 py-2 mx-auto mt-6 text-center rounded-lg font-bold transition-colors ${botaoAtivo ? "bg-yellow-500 text-black cursor-pointer hover:bg-yellow-600" : "bg-gray-300 text-gray-500 cursor-not-allowed"}`}
            disabled={!botaoAtivo}
            onClick={handleConcluirPedido}
          >
            Concluir Pedido
          </button>
        </main>
        <ToastContainer />
      </div>
    </>
  );
}
