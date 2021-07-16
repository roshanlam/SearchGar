import { FormButton, FormCard, FormInput } from "@components/Form";
import { Layout } from "@components/Layout";

export default function ResetPassword() {
  return (
    <>
      <Layout>
        <div className="py-52 bg-gray-100 flex justify-center items-center ">
          <FormCard>
            <dd className="text-xl">Reset Password</dd>
            <form
              action=""
              method="post"
              className="flex flex-col items-center w-full space-y-4 > *"
            >
              <FormInput
                label="Email Address"
                name="email"
                type="text"
                required
              />
              <FormButton type="submit"> Next</FormButton>
            </form>
          </FormCard>
        </div>
      </Layout>
    </>
  );
}