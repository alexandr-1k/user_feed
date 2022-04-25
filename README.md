# Test task

#### Available at: http://211563.fornex.cloud:1337/api/
#### The task is in task.txt 

### To run localy:
```commandline
docker-compose up -d
```

### Testing API:

1. To create user : **POST /createuser/** with following payload:
```json
{
  "email": "tester@com.com",
  "password": "somepass1",
  "role": "A",
  "first_name": "Alex",
  "last_name": "Tester"
}
```
Where **role** can be **A** (Author) or **S** (Subscriber). If role is not specified - **S** is in use.
*first_name* and *last_name* can be removed from payload.

2. To get list of articles: **GET /articles/**. The result depends on whether the user is authenticated or not.
3. To create a new article: **POST/PUT /articles/**. Use following payload:
```json
{
  "title": "Funny article",
  "content": "Very important text",
  "public": "false"
}
```
Articles can be public or not. Non-authenticated users do not see non-public articles.
**public**
4. To delete second article: **DELETE /articles/2/**
