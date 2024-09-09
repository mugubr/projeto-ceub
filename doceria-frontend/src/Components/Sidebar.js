import React from 'react';
import logo from '../assets/logo-barra-lateral.png';
import background from '../assets/barra-lateral.png';
import CalendarioAuxiliar from './CalendarioAuxiliar';

export default function Sidebar({nome}) {
    return (
        <aside
            className="w-72 h-full bg-cover bg-center text-white flex flex-col items-center p-16"
            style={{ backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(${background})` }}
        >
            <img src={logo} className="w-36 h-auto mb-5" alt="logo" />
            <span className="">Olá, {nome}!</span>
            <ul className="list-none w-full">
                <li className="mb-2 cursor-pointer text-center hover:underline">Menu Item 1</li>
                <li className="mb-2 cursor-pointer text-center hover:underline">Menu Item 2</li>
                <li className="mb-2 cursor-pointer text-center hover:underline">Menu Item 3</li>
            </ul>
            <div className='w-full mt-auto'>
                <CalendarioAuxiliar />
            </div>
        </aside>
    );
}

