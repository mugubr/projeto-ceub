import React, { useState, useEffect } from "react";

export default function DoceCard({
  id,
  img,
  nome,
  preco,
  vegano,
  gluten,
  lactose,
  adicionarAoCarrinho,
  quantidades,
  setQuantidades,
  isRealizarPedido,
}) {
  const [quantidade, setQuantidade] = useState(quantidades[id] || 1);

  useEffect(() => {
    setQuantidade(quantidades[id] || 1);
  }, [quantidades, id]);

  const incrementarQuantidade = () => {
    setQuantidade((prev) => {
      const novaQuantidade = prev + 1;
      setQuantidades((prevQuantidades) => ({
        ...prevQuantidades,
        [id]: novaQuantidade,
      }));
      return novaQuantidade;
    });
  };

  const decrementarQuantidade = () => {
    setQuantidade((prev) => {
      const novaQuantidade = Math.max(1, prev - 1);
      setQuantidades((prevQuantidades) => ({
        ...prevQuantidades,
        [id]: novaQuantidade,
      }));
      return novaQuantidade;
    });
  };

  return (
    <div className="flex flex-col sm:flex-row bg-white rounded-md p-4 min-w-[200px]">
      <div>
        <img
          src={img || "default_image_path.png"}
          alt={nome}
          className="w-full h-32 object-cover rounded-md mb-4 sm:mb-0 sm:mr-4"
        />
        <div className="flex justify-center">
          {!vegano && (
            <span className="material-icons-outlined text-gray-600">eco</span>
          )}
          {!gluten && (
            <span className="material-icons-outlined text-gray-600">
              bakery_dining
            </span>
          )}
          {!lactose && (
            <span className="material-icons-outlined text-gray-600">
              icecream
            </span>
          )}
        </div>
      </div>

      <div className="flex flex-col text-center sm:text-left">
        <h3 className="text-lg font-semibold text-gray-700">{nome}</h3>
        <span className="text-yellow-500 font-bold">{preco}</span>
        {isRealizarPedido && (
          <div className="flex items-center justify-center mt-2">
            <button
              className="bg-gray-200 text-black rounded-full w-8 h-8 flex items-center justify-center mr-2 cursor-pointer transition-colors hover:bg-gray-300"
              onClick={decrementarQuantidade}
            >
              -
            </button>
            <div className="w-8 text-center text-gray-800">{quantidade}</div>
            <button
              className="bg-gray-200 text-black rounded-full w-8 h-8 flex items-center justify-center ml-2 cursor-pointer transition-colors hover:bg-gray-300"
              onClick={incrementarQuantidade}
            >
              +
            </button>
          </div>
        )}
        {isRealizarPedido && (
          <button
            className="bg-yellow-400 text-gray-700 rounded-lg py-2 px-4 mt-4 cursor-pointer transition-colors hover:bg-yellow-500"
            onClick={() => adicionarAoCarrinho(id, quantidade)}
          >
            Adicionar
          </button>
        )}
      </div>
    </div>
  );
}
