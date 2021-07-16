import React, { useState } from 'react'
export const Table = ({ className = '' }) => {
  const [tab, setTab] = useState<'search' | 'crawl'>('search')

  return (
    <div
      className={`text-primary flex flex-col h-full justify-between ${className}}`}>
      <div>
        <div className="px-6 py-4 flex items-center ">
          <h3 className="focus:bg-link focus:border-b focus:border-link">
            Search{' '}
          </h3>
          <h3 className="focus:bg-link focus:border-b focus:border-link">
            Crawl{' '}
          </h3>
        </div>

        <div className="overflow-x-auto ">
          <div className="align-middle inline-block min-w-full ">
            <div className="overflow-hidden">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-200 ">
                  <tr className="text-left border-t border-span border-gray-300">
                    <th
                      scope="col"
                      className="px-6 py-2 text-gray-900 text-xs font-medium  uppercase tracking-wider"
                    >
                      Search
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-2 text-gray-900 text-xs font-medium  uppercase tracking-wider"
                    >
                      URL/Result
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-2 text-gray-900 text-xs font-medium  uppercase tracking-wider"
                    >
                      Role
                    </th>
                    <th scope="col" className="px-6 py-2 text-gray-900 text-xs font-medium  uppercase tracking-wider">

                    </th>
                  </tr>
                </thead>
                <tbody>
                  {
                    // Rows
                  }
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}