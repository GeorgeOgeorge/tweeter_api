import requests

ACCESS_TOKEN_VALUE = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2OTg2NjY4LCJpYXQiOjE2NTY5ODQ4NjgsImp0aSI6IjkyZjljYWFhM2UzMzRlYTI4ZWJkYmI5OTI4ZmJkYTU3IiwidXNlcl9pZCI6Mn0.VDcaldSiVrZ9pcoS1bd6-g5n78h0wFFEgLWzNyHlZAA'
REFRESH_TOKEN_VALUE = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Njk5MjA2OCwiaWF0IjoxNjU2OTg0ODY4LCJqdGkiOiI0NDU2OWFlMzJkMGI0MGU5YmVhMDlmNmYyYjExNDAxYyIsInVzZXJfaWQiOjJ9.7L8l1OexL24i-QTLlVDjUKyNZKN5JLa4xqBbOwYvXtg'
SERVER = 'https://b2-twitter.herokuapp.com/twitter_api'

HEADERS={'Authorization': f'Token {ACCESS_TOKEN_VALUE}'}

class Testlogin:

    def test_login_get_token(self):
        result = requests.post(
            url=f'{SERVER}/login/',
            json={
                "username": "rui",
                "password": "rui"
            }
        )
        assert result.status_code == 200
        assert list(result.json().keys()) == ['refresh', 'access']

    def test_login_get_new_token(self):
        result = requests.post(
            url=f'{SERVER}/login/refresh_token',
            json={
                "refresh": REFRESH_TOKEN_VALUE
            }
        )
        assert result.status_code == 200
        assert list(result.json().keys()) == ['access', 'refresh']


class TestTwitterUser:

    def test_list_users(self):
        result = requests.get(
            url=f'{SERVER}/twitterusers/',
            headers=HEADERS
        )
        assert result.status_code == 200
        assert result.json() != []

    def test_find_user(self):
        user_id = 2
        result = requests.get(
            url=f'{SERVER}/twitterusers/{user_id}/',
            headers=HEADERS
        )
        assert result.status_code == 200
        assert result.json()['id'] == user_id

    def test_create_user(self):
        username = "hank"
        result = requests.post(
            url=f'{SERVER}/twitterusers/',
            headers=HEADERS,
            json={
                "username": f"{username}",
                "password": "vo",
                "bio": "",
                "email": "",
                "location": "",
                "website": "",
                "phone": "",
                "birth_date": "2020-03-14"
            }
        )
        assert result.status_code == 201
        assert result.json()['username'] == username

    def test_update_user(self):
        user_id = 12,
        username = "hank"
        result = requests.put(
            url=f'{SERVER}/twitterusers/',
            headers=HEADERS,
            json={
                "id": {user_id},
                "username": f"{username}",
                "password": "vo",
                "bio": "hey, i'm using twitter",
                "email": f"{username}@email.com",
                "location": "new york",
                "website": "",
                "phone": "",
                "birth_date": "2020-03-14"
            }
        )
        assert result.status_code == 201
        assert result.json()['username'] == username

    def test_delte_user(self):
        user_id = 14
        result = requests.delete(
            url=f'{SERVER}/twitterusers/{user_id}/',
            headers=HEADERS
        )
        assert result.status_code == 204
        result = requests.get(
            url=f'{SERVER}/twitterusers/{user_id}/',
            headers=HEADERS
        )
        assert result.status_code == 404


class TestTweet:

    def test_list_tweets(self):
        result = requests.get(
            url=f'{SERVER}/tweets/',
            headers=HEADERS
        )
        assert result.status_code == 200
        assert result.json() != []

    def test_list_last_10_tweets(self):
        result = requests.get(
            url=f'{SERVER}/tweets/get_recent_tweets/',
            headers=HEADERS
        )
        assert result.status_code == 200
        assert result.json() != []

    def test_like_tweet(self):
        pass

    def test_post_tweet(self):
        pass

    def test_comment_tweet(self):
        pass

    def test_filtered_tweets(self):
        pass

    def test_update_tweets(self):
        pass

    def test_delete_tweet(self):
        pass
