import {Table} from '@components/Table';
import {Layout} from "@components/Layout";


const MockData = {
    query: 'Who is Roshan',
    crawlWebsiteRequest: 'https://roshanlamichhane.tech',
    updatedTime: 'Today'
}

export default function History() {
    return (
        <>
            <Layout>
                <div className="md:col-span-3 bg-white shadow-md">
                    <Table />
                </div>
            </Layout>
        </>
    )
}
