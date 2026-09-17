// import { useState } from 'react'
import './App.css'

function App() {

  //   function forward() {
  //   return (
  //     fetch('http://localhost:5000/api/forward')
  //   )
  // }
  // const [count, setCount] = useState(0)

  function forward() {
    fetch("http://localhost:8000/api/forward", {
      method: "POST"
    })
  }

  return (
    <>
      <section className='m-0 h-100 w-auto bg-gray-100 mb-80'>
        <h1 className='bg-amber-200 border-b-2 ps-5 p-2'>Панель для Управления РМК1 и РМК2</h1>

        <div className='m-8 bg-amber-100 h-150 border-4'>
          <h1 className='m-2 ps-3 text-2xl'>Управление РМК2:</h1>

          <button className='hover:bg-amber border-2 bg-amber-400 rounded-[5px] text-xl p-2 ms-8 hover:bg-amber-300 active:bg-amber-500' onClick={forward}>Проехать вперед</button>{/* forward */}
          <button className='hover:bg-amber border-2 border-red-500 bg-amber-400 rounded-[5px] text-xl p-2 ms-8 hover:bg-amber-300 active:bg-amber-500 mt-15'>Аварийная Остановка</button>

          <p className='text-xl px-5 mt-1'>введите целевой аруко:</p>
          <input className='mx-5 p-3 bg-amber-300' type="ВВедите целевой аруко"/>

          <div>
            <h1 className='m-5 ps-3 text-2xl'>Карта занятости РМК2:</h1>

            <ul className='bg-amber-200 text-3xl text-center mx-30 font-bold-5'>
              <li>0 - 0 - 0 - 0 - 0</li>
              <li>0 - 0 - 0 - 0 - 0</li>
              <li>0 - 0 - 0 - 0 - 0</li>
              <li>0 - 0 - 0 - 0 - 0</li>
              <li>0 - 0 - 0 - 0 - 0</li>
            </ul>

          </div>

          <h2 className='ms-8 mt-5 text-xl'>Заряд батареи в вольтах: <p className='text-sm p-5'>n/a</p></h2>

        </div>
      </section>

      <section className='h-100 w-auto bg-gray-100 mb-40'>
        <div className='mt-10 m-10 bg-amber-100 h-160 border-4'>
          <h1 className='m-5 ps-3 text-2xl'>Управление РМК1:</h1>

          <button className='hover:bg-amber border-2 bg-amber-400 rounded-[5px] text-xl p-2 ms-8 hover:bg-amber-300 active:bg-amber-500' onClick={forward}>Проехать вперед</button>{/* forward */}
          <button className='hover:bg-amber border-2 border-red-500 bg-amber-400 rounded-[5px] text-xl p-2 ms-8 hover:bg-amber-300 active:bg-amber-500 mt-15'>Аварийная Остановка</button>

          <p className='text-xl px-5 mt-1'>введите целевой аруко:</p>
          <input className='mx-5 p-3 bg-amber-300' type="ВВедите целевой аруко"/>

          <div>
            <h1 className='m-5 ps-3 text-2xl'>Карта занятости РМК2:</h1>

            <ul className='bg-amber-200 text-3xl text-center mx-30 font-bold-5'>
              <li>0 - 0 - 0 - 0 - 0</li>
              <li>0 - 0 - 0 - 0 - 0</li>
              <li>0 - 0 - 0 - 0 - 0</li>
              <li>0 - 0 - 0 - 0 - 0</li>
              <li>0 - 0 - 0 - 0 - 0</li>
            </ul>

          </div>

          <h2 className='ms-8 mt-5 text-xl'>Заряд батареи в вольтах: <p className='text-sm p-5'>n/a</p></h2>
        </div>
      </section>
    </>
  )
}

export default App
