import Link from 'next/link'
import { FormButton, FormCard, FormInput } from '@components/Form'
import { Layout } from '@components/Layout'
import type { NextApiRequest, NextApiResponse } from 'next'

export default function WebsiteCrawlRequest() {
  return (
    <>
      <Layout>
        <div className="py-36 bg-gray-100 flex justify-center items-center text-sm">
          <FormCard>
            <dd className="text-xl">Request Website To Be Crawled</dd>
            <form
              action=""
              method="post"
              className="flex flex-col items-center w-full space-y-4 > *"
            >
              <FormInput label="Enter Website Link" name="websiteLink" type="url" required />
              <FormButton type="submit"> Submit Website Crawl Request</FormButton>
            </form>
          </FormCard>
        </div>
      </Layout>
    </>
  )
}
