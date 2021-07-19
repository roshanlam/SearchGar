import Link from "next/link";
import { FormButton, FormCard, FormInput } from "@components/Form";
import { Layout } from "@components/Layout";
import {SyntheticEvent, useState} from "react";
import {useRouter} from "next/router";

const SignUp = () => {
      const [email, setEmail] = useState('');
      const [password, setPassword] = useState('');
      const router = useRouter();
      const handleSignUp = async (e: SyntheticEvent) => {
            e.preventDefault();
            await fetch('http://localhost:8000/register/', {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    email,
                    password
                })
            });
            await router.push('/login');
        }

  return (
      <>
      <Layout>
        <div className="py-20 bg-gray-100 flex justify-center items-center ">
          <FormCard>
            <dd className="text-xl">Sign Up</dd>
            <form
              onSubmit={handleSignUp}
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
              <FormButton type="submit">Login</FormButton>
            </form>
            <p className="text-sm text-gray-400">
              By registering you agree to SearchIt&apos;s{" "}
              <a className="text-gray-900 hover:underline">
                Terms of Using the SearchIt Platform
              </a>{" "}
              and{" "}
              <a className="text-gray-900 hover:underline">Privacy Policy</a>
            </p>
            <Link href="/login">
              <a className="text-sm text-gray-900 hover:underline">
                Already have an account? Log in
              </a>
            </Link>
          </FormCard>
        </div>
      </Layout>
      </>
  );
};
export default SignUp;