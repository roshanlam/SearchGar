import Link from "next/link";

import { FormButton, FormCard, FormInput } from "@components/Form";
import { Layout } from "@components/Layout";

export default function Signup() {
  return (
    <>
      <Layout>
        <div className="py-20 bg-gray-100 flex justify-center items-center ">
          <FormCard>
            <dd className="text-xl">Sign Up</dd>
            <form
              action=""
              method="post"
              className="flex flex-col items-center w-full space-y-4 > *"
            >
              <FormInput
                label="Username"
                name="username"
                type="text"
                required
              />
              <FormInput label="Email" name="email" type="text" required />
              <FormInput
                label="Password"
                name="password"
                type="password"
                required
              />
              <FormInput
                label="Re-Enter Password"
                name="verifyPassword"
                type="password"
                required
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
}