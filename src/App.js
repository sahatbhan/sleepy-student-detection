import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes, Outlet, Navigate } from 'react-router-dom';
import Sidebar from './Components/Sidebar'

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route exact path='/' element={<Sidebar />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
