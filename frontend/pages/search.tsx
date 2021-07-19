import Link from 'next/link'
import Router, {useRouter} from 'next/router';
import { FormButton, FormCard, FormInput } from '@components/Form'
import { Layout } from '@components/Layout'
import type { NextApiRequest, NextApiResponse } from 'next'
import {SyntheticEvent, useState} from "react";

const handleSearch = () =>{
  const [searchQuery] = useState('');
  const router = useRouter();
  const submit = async (e: SyntheticEvent) =>{
    e.preventDefault()
    await fetch('', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      credentials: 'include',
      body: JSON.stringify({
        searchQuery
      })
    })
    await router.push('/')
  }
}

export default function Login() {
  return (
    <>
      <Layout>
        <div className="py-36 bg-gray-100 flex justify-center items-center text-sm">
          <FormCard>
            <dd className="text-xl">Search</dd>
            <form
              onSubmit={handleSearch}
              className="flex flex-col items-center w-full space-y-4 > *"
            >
              <FormInput label="Search Query" name="searchquery" type="text" required />
              <FormButton type="submit"> Search</FormButton>
            </form>
          </FormCard>
        </div>
      </Layout>
    </>
  )
}
