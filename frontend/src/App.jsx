import { useState } from 'react'
import Sidebar from './components/sidebar'
import Videofeed from './components/videoFeed'
import './App.css'

function App() {


  return (
    <div className='app'>
      <Sidebar></Sidebar>
      <Videofeed/>
    </div>
  )
}

export default App
