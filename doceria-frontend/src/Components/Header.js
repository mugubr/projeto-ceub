import React from "react";

export default function Header({ texto }) {
  return (
    <header className="flex items-center justify-between p-5 text-gray-500">
      <span className="text-xl font-bold">{texto}</span>
      <img
        src="https://via.placeholder.com/50"
        alt="Foto"
        className="w-12 h-12 rounded-full"
      />
    </header>
  );
}
