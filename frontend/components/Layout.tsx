import Head from "next/head"
import { Header } from "@components/Header"
import { Footer } from "@components/Footer"
import { Config } from "config"

export const Layout = ({ children }) => {
  return (
    <>
      <Head>
        <title>{Config.title}</title>
      </Head>

      <Header />
      <main>{children}</main>
      <Footer />
    </>
  )
}