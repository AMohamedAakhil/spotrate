import React from 'react'

const Navbar = () => {


  return (
    <div className="navbar bg-base-100 ">
  <div className="flex-1 ">
    <button className="btn btn-ghost normal-case text-2xl font-bold">Timescan Logistics</button>
  </div>
  <div className="flex-none gap-2">
    <div className="form-control">
      <input type="text" placeholder="Search" className="input input-bordered" />
    </div>
    <div className="dropdown dropdown-end">
     
      <ul tabIndex={0} className="mt-3 p-2 shadow menu menu-compact dropdown-content bg-base-100 rounded-box w-52">
        
        <li><a>Settings</a></li>
        <li><a>Logout</a></li>
      </ul>
    </div>
  </div>
</div>
  )
}

export default Navbar