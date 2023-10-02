import React from 'react'
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom'

import { carrot } from './assets'

import { Home, EventsScheduler, DatesScheduler } from './pages'


const App = () => {
  return (
    <BrowserRouter>
      <header className='w-full flex justify-between items-center
      bg-white sm:px-8 py-4 border-b border-b-[#e6ebf4]'>
        <Link to="/">
          <img src={carrot} alt='logo'
          className='w-28 object-contain' />
        </Link>

        <div className='w-1/6 px-6 flex justify-between items-center'>
          <Link to='/events'
          className='font-inter font-medium bg-[#ec843e] text-white
          px-4 py-2 rounded-md'>
            Events
          </Link>
          <Link to='/dates'
          className='font-inter font-medium bg-[#ec843e] text-white
          px-4 py-2 rounded-md'>
            Dates
          </Link>
        </div>
      </header>

      <main className='sm:p-8 px-4 py-8 w-full bg-[#f9fafe] 
      min-h-[calc(100vh - 73px)]'>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='events' element={<EventsScheduler />} />
          <Route path='dates' element={<DatesScheduler />} />
        </Routes>
      </main>

    </BrowserRouter>
  )
}

export default App