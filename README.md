![workflow](https://github.com/imwisagist/Test_for_ITFOX/actions/workflows/main.yml/badge.svg)

### News
The service is designed for creating and viewing news. <br>
Users can write comments to the news and put likes.

##### The service is available at the following addresses:
- Admin-panel - [`http://csn.sytes.net:800/admin/`](http://csn.sytes.net:800/admin/)
- Authentication - [`http://csn.sytes.net:800/api/v1/auth/`](http://csn.sytes.net:800/api/v1/auth/)
- News - [`http://csn.sytes.net:800/api/v1/news/`](http://csn.sytes.net:800/api/v1/news/)

<details>
<summary><strong>How Admin-panel loks like</strong></summary>
<br>

![screenshot](https://github.com/imwisagist/Test_for_ITFOX/blob/main/images/admin1.png?raw=true)

![screenshot](https://github.com/imwisagist/Test_for_ITFOX/blob/main/images/admin2.png?raw=true)

![screenshot](https://github.com/imwisagist/Test_for_ITFOX/blob/main/images/admin3.png?raw=true)

![screenshot](https://github.com/imwisagist/Test_for_ITFOX/blob/main/images/admin4.png?raw=true)

</details>

<details>
<summary><strong>User and Administrator capabilities</strong></summary>
<br>

#### What authorized users can do
- Perform authentication under your username and password.
- View a list of all news, individual news.
- Create/edit/delete your own news.
- View/write comments on all the news.
- Create/delete your comments and delete comments on your news.
- Create/delete your own likes.
- View the number of comments and likes to any news.
- Watch the ten latest comments on any news.

#### What can an administrator do
The administrator has all the rights of an authorized user.
Also, he can:
- Edit/delete any news.
- Edit/delete any comments.
- Edit/Delete/create users.
- Delete/like on behalf of any user.
- Create/edit/delete tokens for any users.

</details>

<details>
<summary><strong>Running in Docker containers</strong></summary>
<br>

- Cloning a remote repository.
- There is a .env file in the /infra directory, with environment variables, ready to use,
edit it at your discretion if required.
- Building and deploying containers.
```bash
git clone https://github.com/Imwisagist/Test_for_ITFOX.git && cd infra && bash deploy.sh
```
- The standard Django admin panel is available at [`http://localhost/admin/`](http://localhost/admin/)
<br> The login data is specified in the .env file (the superuser is created automatically at the stage of applying migrations)
- Authentication Endpoint [`http://localhost/api/v1/auth/`](http://localhost/api/v1/auth/)
<br> To get a token, send a POST request with 2 parameters in the body username and password
<br> Create a user in the admin panel or use the data from the .env file
- News Endpoint [`http://localhost/api/v1/news/`](http://localhost/api/v1/news/)
- Details on endpoints are in the documentation below
</details>

<details>
<summary><strong>API Documentation</strong></summary>
<br>

**`POST` | Getting an authentication token: `http://localhost/api/v1/auth/`**

Request:
```
{
    "username": "imwisagist",
    "password": "qazxswedc"
}
```
Response:
```
{
    "token": "bc1cc7d433ce6293911731113aeb03d6ac263b73"
}
```

**`GET` | Getting the news list: `http://localhost/api/v1/news/`**

Response:
```
{
    "count": 12,
    "next": "http://localhost/api/v1/news/?limit=10&offset=10",
    "previous": null,
    "results": [
        {
            "id": 1,
            "pub_date": "2023-07-04",
            "title": "gfhfghgf",
            "text": "hfghgfhfg",
            "author": "imwisagist",
            "likes_count": 0,
            "comments_count": 1,
            "ten_latest_comments": [
                "last"
            ]
        },
        {
            "id": 2,
            "pub_date": "2023-07-04",
            "title": "hgfhfgh",
            "text": "fghfghfgh",
            "author": "imwisagist",
            "likes_count": 1,
            "comments_count": 0,
            "ten_latest_comments": []
        },
        ....
    ]
}
```

**`POST` | Creating news: `http://localhost/api/v1/news/`**

Request:
```
{
    "title": "Great news",
    "text": "The war is over."
}
```
Response:
```
{
    "id": 13,
    "pub_date": "2023-07-04",
    "title": "Great news",
    "text": "The war is over.",
    "author": "imwisagist",
    "likes_count": 0,
    "comments_count": 0,
    "ten_latest_comments": []
}
```

**`GET` | Getting a separate news item: `http://localhost/api/v1/news/<news_id>/`**

Response:
```
{
    "id": 13,
    "pub_date": "2023-07-04",
    "title": "Great news",
    "text": "The war is over.",
    "author": "imwisagist",
    "likes_count": 0,
    "comments_count": 0,
    "ten_latest_comments": []
}
```

**`PUT` | Updating News: `http://localhost/api/v1/news/<news_id>/`**

Request:
```
{
    "title": "Great news",
    "text": "Finally! The war is over."
}
```
Response:
```
{
    "id": 13,
    "pub_date": "2023-07-04",
    "title": "Great news",
    "text": "Finally! The war is over.",
    "author": "imwisagist",
    "likes_count": 0,
    "comments_count": 0,
    "ten_latest_comments": []
}
```

**`DELETE` | Deleting news: `http://localhost/api/v1/news/<news_id>/`**

Response:
```
{
    204 No Content
}
```

**`GET` | Getting comments: `http://localhost/api/v1/news/<news_id>/comments/`**

Response:
```
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}
```

**`POST` | Creating a comment: `http://localhost/api/v1/news/<news_id>/comments/`**

Request:
```
{
    "text": "Finally! The war is over."
}
```
Response:
```
{
    "id": 17,
    "pub_date": "2023-07-04",
    "text": "Finally! The war is over.",
    "news": 14,
    "author": "imwisagist"
}
```

**`GET` | Getting a comment: `http://localhost/api/v1/news/<news_id>/comments/<comments_id>/`**

Response:
```
{
    "id": 17,
    "pub_date": "2023-07-04",
    "text": "Finally! The war is over.",
    "news": 14,
    "author": "imwisagist"
}
```

**`PUT` | Editing a comment: `http://localhost/api/v1/news/<news_id>/comments/<comments_id>/`**

Request:
```
{
    "text": "The war is over."
}
```
Response:
```
{
    "id": 15,
    "pub_date": "2023-07-04",
    "text": "The war is over.",
    "news": 14,
    "author": "imwisagist"
}
```

**`DELETE` | Deleting a comment: `http://localhost/api/v1/news/<news_id>/comments/<comments_id>/`**

Response:
```
{
    204 No Content
}
```

**`POST` | Like the news: `http://localhost/api/v1/news/<news_id>/like/`**

Response:
```
{
    201 Created
}
```

**`DELETE` | Remove your like from the news: `http://localhost/api/v1/news/<news_id>/like/`**

Response:
```
{
    204 No Content
}
```
</details>
