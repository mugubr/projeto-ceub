import React from "react";

export default function Content({ children }) {
  return <div className="flex-1 overflow-auto">{children}</div>;
}
