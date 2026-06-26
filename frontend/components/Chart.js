import React from 'react'
import { Line } from 'react-chartjs-2'

const data = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June'],
  datasets: [
    {
      label: 'Cost Per Day',
      data: [65, 59, 80, 81, 56, 55],
      fill: false,
      backgroundColor: 'rgb(75, 192, 192)',
      borderColor: 'rgba(75, 192, 192, 0.2)',
    },
  ],
}

export default function Chart() {
  return (
    <div>
      <h3 className="text-xl font-bold mb-4">Cost Per Day</h3>
      <Line data={data} />
    </div>
  )
}
