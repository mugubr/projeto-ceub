import React, { useState } from "react";

export default function Header({ texto }) {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => setIsDropdownOpen(!isDropdownOpen);

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("user");
    localStorage.removeItem("cliente_id");
    window.location.href = "/";
  };

  return (
    <header className="flex items-center justify-between p-5 ">
      <span className="text-xl font-bold">{texto}</span>
      <div className="relative flex items-center">
        <img
          src="https://via.placeholder.com/50"
          alt="Foto"
          className="w-12 h-12 rounded-full cursor-pointer"
          onClick={toggleDropdown}
        />
        <span
          className={`material-icons-outlined cursor-pointer ml-2  transition-transform ${isDropdownOpen ? "rotate-180" : ""}`}
          onClick={toggleDropdown}
        >
          keyboard_arrow_down
        </span>
        {isDropdownOpen && (
          <div className="absolute right-0 mt-24 w-48 bg-white border border-gray-300 rounded-md shadow-lg z-10">
            <button
              onClick={handleLogout}
              className="w-full px-4 py-2 text-left text-black  hover:bg-yellow-300"
            >
              Logout
            </button>
          </div>
        )}
      </div>
    </header>
  );
}
