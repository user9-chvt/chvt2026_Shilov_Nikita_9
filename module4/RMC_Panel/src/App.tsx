// import { useState } from 'react'
import './App.css'

function App() {
  // const [count, setCount] = useState(0)
  return (
    <>
      <section className='m-0 h-200 w-auto bg-gray-100'>
        <h1 className='bg-amber-200 border-b-2 ps-5 p-2'>Панель для Управления RMC</h1>

        <div className='m-10 bg-amber-100 h-100 border-4'>
          <h1 className='m-5 ps-3 text-2xl'>Управление РМС2:</h1>

          <button className='hover:bg-amber border-2 bg-amber-400 rounded-[5px] text-xl p-2 ms-8 hover:bg-amber-300 active:bg-amber-500'>Проехать вперед</button>

          <h2 className='ms-8 mt-5 text-xl'>Заряд батареи: </h2>

        </div>
      </section>
    </>
  )
}

export default App
