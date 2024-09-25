// src/components/Navbar.js
import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Link, useNavigate } from 'react-router-dom';
import logo from '../images/llogo.png'; // Adjust the path to your logo image

const Navbar = ({ onLogout }) => {
  const navigate = useNavigate();

  const handleLogout = () => {
    onLogout();
    navigate('/');
  };

  return (
    <AppBar position="static">
      <Toolbar>
        <img src={logo} alt="Logo" style={{ width: '40px', height: '40px', marginRight: '10px' }} />
        <Typography variant="h6" style={{ flexGrow: 1 }}>
          Supermarket
        </Typography>
        <Button color="inherit" component={Link} to="/camera-interface">Camera Interface</Button>
        <Button color="inherit" component={Link} to="/qr-scanner">QR Scanner</Button>
        <Button color="inherit" component={Link} to="/dashboard">Dashboard</Button>
        <Button color="inherit" onClick={handleLogout}>Logout</Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
