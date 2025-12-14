import React from "react";
import { useNavigate } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  const navigate = useNavigate();

  return (
    <header className="navbar">
      <div className="navbar-inner">
        {/* LEFT */}
        <div className="navbar-left">
          <div className="logo-box">🍬</div>
          <span className="logo-text">Sweet Shop</span>
          <button
          className="signin-btn"
          onClick={() => navigate("/login")}
        >
          Sign Out
        </button>
        </div>

        {/* RIGHT */}
        
      </div>
    </header>
  );
}

export default Navbar;
