interface ApplicationError {
    [error_type: string]: string[];
}

type ServerError = string;

interface Error {
    response: {
        data: ApplicationError | ServerError;
        status: number;
        statusText: string;
    };
}

export const formatAPIError = (error: Error): string => {
    let errorMessage = 'Error';

    if (typeof error.response?.data === 'object') {
        const errorArrays = Object.values(error.response.data);
        const errorArray = errorArrays.reduce((acc, val) => [...acc, ...val], []);
        errorMessage = errorArray.join(' ');
    }

    return errorMessage;
};