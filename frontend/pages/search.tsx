import Link from 'next/link'
import { FormButton, FormCard, FormInput } from '@components/Form'
import { Layout } from '@components/Layout'
import type { NextApiRequest, NextApiResponse } from 'next'

export default function Login() {
  return (
    <>
      <Layout>
        <div className="py-36 bg-gray-100 flex justify-center items-center text-sm">
          <FormCard>
            <dd className="text-xl">Search</dd>
            <form
              action=""
              method="post"
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
