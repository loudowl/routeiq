import React from 'react'
import Link from 'next/link'

export default function Home() {
  return (
    <div className="container mx-auto">
      <h1 className="text-4xl font-bold text-center">Welcome to RouteIQ</h1>
      <p className="text-center mt-4">Optimize your AI API costs with intelligent routing.</p>
      <div className="flex justify-center mt-8">
        <Link href="/dashboard">
          <a className="bg-blue-500 text-white px-4 py-2 rounded">Go to Dashboard</a>
        </Link>
      </div>
    </div>
  )
}
