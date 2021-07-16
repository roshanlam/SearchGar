import Link from 'next/link'
import { FormButton, FormCard, FormInput } from '@components/Form'
import { Layout } from '@components/Layout'

export default function Login() {
  return (
    <>
      <Layout>
        <div className="py-36 bg-gray-100 flex justify-center items-center text-sm">
          <FormCard>
            <dd className="text-xl">Log In</dd>
            <form
              action=""
              method="post"
              className="flex flex-col items-center w-full space-y-4 > *"
            >
              <FormInput label="Email" name="email" type="text" required />
              <FormInput
                label="Password"
                name="password"
                type="password"
                required
              />
              <Link href="/resetpassword">
                <a className="ml-auto text-right text-sm hover:underline">
                  Recover your password
                </a>
              </Link>

              <FormButton type="submit"> Sign In</FormButton>
            </form>
            <Link href="/signup">
              <a className="text-sm text-gray-900 hover:underline">
                Register an Account
              </a>
            </Link>
          </FormCard>
        </div>
      </Layout>
    </>
  )
}