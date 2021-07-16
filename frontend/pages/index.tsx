import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import {Layout} from "@components/Layout";

export default function Home() {
  return (
    <>
      <Layout>
        <div className="py-10 bg-gray-900 sm:pt-16 lg:pt-8 lg:pb-14 lg:overflow-hidden">
          <div className="mx-auto max-w-7xl lg:px-8">
            <div className="lg:grid lg:grid-cols-2 lg:gap-8">
              <div className="mx-auto max-w-md px-4 sm:max-w-2xl sm:px-6 sm:text-center lg:px-0 lg:text-left lg:flex lg:items-center">
                <div className="lg:py-24">
                  <h3 className="mt-4 text-4xl tracking-tight font-extrabold text-white sm:mt-5 sm:text-6xl lg:mt-6 xl:text-6xl">
                    <span className="block">Welcome To SearchIt</span>
                    <span className="block">A Open Source Search Engine</span>
                  </h3>
                  <p className="mt-3 text-base text-gray-300 sm:mt-5 sm:text-xl lg:text-lg xl:text-xl">
                    With Search It you can browse the internet without your data being tracked or any ads being shown.
                  </p>

                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="py-10">
            <div className="max-w-4xl mx-auto justify-center flex">
              <div className="">
                <button className="px-8 py-2 bg-gray-900  text-white rounded-full border-black p-1">
                  Start Using It Now. No Need to Create Account Unless You Want To
                </button>
                <div className="py-4">
                  <p>Come and Help Use Improve The Search Engine By Giving Us Feedback</p>
                </div>
              </div>
            </div>
          </div>
      </Layout>
    </>
  )
}


const SendQuery = async  () =>{
  const res = await fetch(
      'url'
  )
  const response = await res.json()
  return response?.results
}

