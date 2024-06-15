import { useState } from 'react'
import './App.css'
import SideBar from './components/SideBar'
import Login from './pages/Login'
import Register from './pages/Register'

import { Route, Routes } from 'react-router-dom'
import CreateFlashCard from './pages/CreateFlashcard'

function App() {
 

  return (
    <>
      <Routes>
        <Route path='/login' element={<Login />}/>
        <Route path='/register' element={<Register />}/>
        <Route path='/home' element={<SideBar/>}/>
        <Route 
            path='/createcard' 
            element={<CreateFlashCard />}
        />
        <Route path='/studycards' element={<SideBar/>}/>
      </Routes>
      
    </>
  )
}

export default App
