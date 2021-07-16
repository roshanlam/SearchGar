import { Button } from '@components/Button'
import { Layout } from '@components/Layout'
import Image from 'next/image'

export default function dashboard({ trades }) {
  return (
    <>
      <Layout>
        <div className="font-mono py-12 px-12 grid bg-gray-100 md:grid-cols-4 md:grid-rows-5 grid-cols-1 gap-4">
          <div className="text-sm text-primary  md:row-start-1 md:row-span-5 flex flex-col space-y-4">
            <div className="bg-white p-6 shadow-md flex flex-col items-center space-y-4">
              <div className="text-center flex flex-col items-center w-full">
                <span>
                  <span className="font-bold">Roshan Lamichhane</span>
                </span>
              </div>
              <span className="text-center">
                Trustworthy, fast, reliable. no scam.
              </span>
              <Button
                fill
                type={'secondary'}>
                Edit Profile
              </Button>
            </div>
          </div>
        </div>
      </Layout>
    </>
  )
}