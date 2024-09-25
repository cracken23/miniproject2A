import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import CameraInterface from './pages/CameraInterface';
import QRScanner from './pages/QRScanner';
import Checkout from './pages/Checkout'; // Import the Checkout component
import './App.css';
import supermarketImage from './images/supermarket.jpg'; // Correct import

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
  };

  return (
    <Router>
      {isAuthenticated && <Navbar onLogout={handleLogout} />}
      <div className="container">
        {isAuthenticated && (
          <h1 className="welcome-message">Welcome to SmartSpace Analytics</h1>
        )}
        {isAuthenticated && (
          <div className="image-container">
            <img src={supermarketImage} alt="Supermarket" className="hero-image" />
          </div>
        )}
        <Routes>
          <Route path="/" element={<Login onLogin={handleLogin} />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/camera-interface" element={<CameraInterface />} />
          <Route path="/qr-scanner" element={<QRScanner />} />
          <Route path="/checkout" element={<Checkout />} />
        </Routes>
      </div>
      <Footer />
    </Router>
  );
};

export default App;
