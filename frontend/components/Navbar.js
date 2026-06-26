import React from 'react'
import Link from 'next/link'

export default function Navbar() {
  return (
    <nav className="bg-dark-charcoal p-4 text-white">
      <div className="container mx-auto flex justify-between">
        <div>
          <Link href="/">
            <a className="text-xl font-bold">RouteIQ</a>
          </Link>
        </div>
        <div>
          <Link href="/dashboard">
            <a className="mx-2">Dashboard</a>
          </Link>
        </div>
      </div>
    </nav>
  )
}
