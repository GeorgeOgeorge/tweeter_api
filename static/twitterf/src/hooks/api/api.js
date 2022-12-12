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
        const response = await api.post('/twitterusers/login/', { username, password });

        if (response.data) {
            return response.data;
        }
        return {}

    },

    signup: async (username, password, email) => {
        const response = await api.post('/twitterusers/', { username, password, email, bio: '', location: '', website: '', phone: '', birth_date: '2020-01-01' })
        return response.data
    },

    editProfile: async (id, data) => {
        const response = await api.put(`/twitterusers/${id}/`, data)
        return response.data
    },

    logout: async () => {
        const response = await api.post('/logout/');
    },

    getOnePost: async (id) => {
        const response = await api.get(`/tweets/${id}`)
        return response.data
    },

    getPost: async () => {
        const response = await api.get('/tweets/')
        return response.data
    },

    getPostsUser: async (id) => {
        const response = await api.get(`/tweets/${id}/get_user_tweets/`)
        return response.data
    },

    postPost: async ({ text, location, user_id }) => {
        const response = await api.post('/tweets/', { text, location, user_id })
        return response.data
    },

    curtePost: async (id, user_id) => {
        const response = await api.post(`tweets/${id}/like_tweet/`, { user_id: user_id })
        return response.status
    },

    comentPost: async (id, user_id, text, location) => {
        const response = await api.post(`tweets/${id}/comment_tweets/`, { text: text, location: location, user_id: user_id })
        return response.status
    },

    getRettweets: async (id) => {
        const response = await api.get(`/tweets/${id}/tweet_replies/`)
        return response.data
    },

    getUserAlreadyExist: async (name) => {
        const response = await api.post(`/twitterusers/username_exist/`, { name: name })
        return response.status
    },

    getUser: async (id) => {
        const response = await api.get(`/twitterusers/${id}/`)
        return response.data
    },

    follow: async (data) => {
        const response = await api.post(`/twitterusers/follow_user/`, data)
        return response.data
    },

    block: async (data) => {
        const response = await api.post(`/twitterusers/block_user/`, data)
        return response.data
    }

})