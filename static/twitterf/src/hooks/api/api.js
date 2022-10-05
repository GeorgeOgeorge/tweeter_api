import axios from 'axios';

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/twitter_api",
    // headers: {
    //     Authorization: "Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0OTMyMjk4LCJpYXQiOjE2NjQ5Mjg3NTgsImp0aSI6IjNkMjg0YWQ4MDg2MDRkZTY4ZjU4YWRjNTM5ZWZlYTMxIiwidXNlcl9pZCI6OH0.XOrFa_QuwzdMrboD-tI1rdgjrfDZN_gj8UN3xuRsHxc"
    // },
    credentials: true
}); 

export const useApi = () => ({
    // validateToken: async (token) => {
    //     const headers = {
    //         Authorization: `Bearer ${token}`,
    //         'content-type': 'application/json',
    //     };

    //     const response = await api.get('/profile/', { headers });
    //     return response.data;
    // },

    signin: async (username, password) => {
        const response = await api.post('/login/', {username, password});

        if (response.data) {
            return response.data;
        }
        return {}

    },

    signup: async (username, password, email) => {
        const response = await api.post('/twitterusers/', {username, password, email, bio: '', location: '', website:'', phone: '', birth_date: null})
        return response.data
    },

    logout: async () => {
        const response = await api.post('/logout/');
    },

    getPost: async (heards) => {
        const response = await api.get('/tweets/', {heards})
        return response.data
    },

    postPost: async ({text, location}, heards) => {
        const response = await api.post('/tweets/', {text, location}, {heards})
        return response.data
    }

})