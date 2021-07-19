import Link from 'next/link'
import { FormButton, FormCard, FormInput } from '@components/Form'
import { Layout } from '@components/Layout'
import {SyntheticEvent, useState} from "react";
import {useRouter} from "next/router";

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();
  const handleLogin = async (e: SyntheticEvent) => {
    e.preventDefault()
    await fetch('http://localhost:8080/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      credentials: 'include',
      body: JSON.stringify({
        email, password
      })
    });
    await router.push('/');
  }

  return (
    <>
      <Layout>
        <div className="py-36 bg-gray-100 flex justify-center items-center text-sm">
          <FormCard>
            <dd className="text-xl">Log In</dd>
            <form
              onSubmit={handleLogin}
              className="flex flex-col items-center w-full space-y-4 > *"
            >
              <FormInput
                  label="Email" name="email"
                  type="text" required
                  onChange={e => setEmail(e.target.value)}
              />
              <FormInput
                label="Password"
                name="password"
                type="password"
                required
                onChange={e => setPassword(e.target.value)}
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
  );
};

export default Login;