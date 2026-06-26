import React from 'react'
import Navbar from '../components/Navbar'
import Chart from '../components/Chart'

export default function Dashboard() {
  return (
    <div>
      <Navbar />
      <div className="container mx-auto mt-8">
        <h2 className="text-2xl font-bold">Dashboard</h2>
        <Chart />
      </div>
    </div>
  )
}
