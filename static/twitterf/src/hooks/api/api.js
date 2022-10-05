import axios from 'axios';

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/twitter_api"
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

    getPost: async () => {
        const response = await api.get('/tweets/')
        return response.data
    },

    postPost: async (text, location) => {
        const response = await api.post('/tweets/', {text, location})
        return response.data
    }

})