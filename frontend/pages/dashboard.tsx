import { Button } from '@components/Button'
import { Layout } from '@components/Layout'
import Image from 'next/image'
import {SyntheticEvent, useEffect, useState} from "react";
import {route} from "next/dist/next-server/server/router";
import {router} from "next/client";
import {useRouter} from "next/router";

export default function dashboard() {
  const SearchHistory = async (e: SyntheticEvent) =>{
    const [query, setQuery] = useState('');
    const [time, setTime] = useState('');
    e.preventDefault()
    await fetch('https://localhost:8000/seeHistory/Query/',{
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
            credentials: 'include',
            body: JSON.stringify({
                time,
                query
            })
    });
  }

  const CrawlHistory = async (e: SyntheticEvent) =>{
    const [time, setTime] = useState('');
    const [websiteName, setWebsiteName] = useState('');
    const [websiteURl, setWebsiteURl] = useState('');
    const router = useRouter();
    e.preventDefault()
    await fetch('https://localhost:8000/seeHistory/Crawl/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      credentials: 'include',
      body: JSON.stringify(time, websiteName, websiteURl)
    })
    await router.push('/dashboard');
  }
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
                Developer
              </span>
              <Button
                fill
                type={'secondary'}
                onSubmit={SearchHistory}
              >
                See Search History
              </Button>
              <Button
                fill
                type={'secondary'}
                onSubmit={CrawlHistory}
              >
                See Crawl History
              </Button>
            </div>
          </div>
        </div>
      </Layout>
    </>
  )
}