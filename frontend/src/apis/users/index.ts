import axios from "axios";

export interface APIModel {
    pk: string;
}

export interface User extends APIModel{
    is_email_verified: boolean;
    created_date: string;
    account_number: string;
}

export interface ActiveUser extends User{
    access_token: string;
    refresh_token: string;
}

export function standardHeaders() {
    return{
        headers:{
            'Content-Type': 'application/json',
        },
    };
}

export async function createUser({
    display_name,
    email,
    password,
}: {
    display_name:string;
    email:string;
    password:string;
}){
    return axios.post('${process.env.BACKEND_API}/users', {display_name, email, password}, standardHeaders());
}

export async function getUser({uuid}: {uuid: string}): Promise<User> {
    const response = await axios.get<User>(`${process.env.REACT_APP_BACKEND_API}/users/${uuid}`);
    if (!response.data) {
        throw new Error('Error while fetching user. Please try again.');
    }
    return response.data;
}