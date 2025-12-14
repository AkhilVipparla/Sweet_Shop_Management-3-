import React, { useEffect, useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";
import "./Home.css";
import Navbar from "../components/Navbar";

const sweetImages = {
  laddoo: "/images/laddoo.jpg",
  "Kaju Katli": "/images/kaju-katli.jpg",
  "Gulab Jamun": "/images/Gulab-Jamun.jpg",
  "Motichoor Ladoo": "/images/Motichur-Laddu.jpg",
  Jalebi: "/images/jalebi.jpg",
  "Bombay Halwa": "/images/Bombay-Halwa.jpg",
  "Soan Papdi": "/images/Soan-Papdi.jpg",
  "Milk MysorePak": "/images/Milk-MysorePak.jpg",
  Badusha: "/images/Badusha.jpg",
};



function Home() {
  const [sweets, setSweets] = useState([]);
  const [search, setSearch] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    api
      .get("/sweets")
      .then((res) => setSweets(res.data))
      .catch(() => navigate("/login"));
  }, [navigate]);

  const filteredSweets = sweets.filter(
    (s) =>
      s.name.toLowerCase().includes(search.toLowerCase()) ||
      s.category.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
    
    <Navbar/>
    
    <div className="home-page">
      
      
      {/* HERO */}
      <section className="hero">
        <span className="badge">🍬 Welcome to our sweet paradise</span>
        <h1>
          Discover the Sweetest <span>Treats</span> in Town
        </h1>
        <p>
          From handcrafted chocolates to classic candies, explore our delightful
          collection of sweets that will make every moment sweeter.
        </p>
      </section>

      {/* SEARCH */}
      <section className="search-bar">
        <input
          type="text"
          placeholder="Search for your favorite sweets..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        
      </section>

      {/* SWEETS GRID */}
      <section className="sweets-grid">
        {filteredSweets.map((sweet) => (
          <div className="sweet-card" key={sweet.id}>
            <div className="sweet-image">
              
  <img
  src={`/images/${sweet.name
    .toLowerCase()
    .trim()
    .replace(/\s+/g, "-")}.jpg`}
  alt={sweet.name}
  onError={(e) => {
    e.target.src = "/images/laddoo.jpg";
  }}
/>



              <span className="tag">{sweet.category}</span>
            </div>

            <div className="sweet-content">
              <h3>{sweet.name}</h3>
              <p className="desc">
                Delicious {sweet.category.toLowerCase()} made to satisfy your
                cravings.
              </p>

              <div className="meta">
                <span className="price">₹{sweet.price}</span>
                <span className="stock">{sweet.quantity} in stock</span>
              </div>

              <button
                className="purchase-btn"
                disabled={sweet.quantity === 0}
              >
                Purchase
              </button>
            </div>
          </div>
        ))}
      </section>
    </div>
    </>
  );
}

export default Home;
