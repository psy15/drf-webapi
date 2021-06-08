# DRF WEB API
To Do list api with User Registration, Login and full CRUD functionality using REST APIs, JWTs and mssql database.

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

In our case, we have resource, `todocontroller`, so we will use the following URLS:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`getall/` | GET | READ | Get all tasks
`get/:id` | GET | READ | Get task
`create/`| POST | CREATE | Create task
`put/:id` | PUT | UPDATE | Update task
`delete/:id` | DELETE | DELETE | Delete task

Another api is AuthController which have APIs related to registration and login. TodoController is protected via authorization of the auth controller header and only
authenticated users will have access to the controller.

`/accounts/register/`
Takse a set of user registration credentials and then creates the user.

`api/token`
Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

`api/token/refresh`
Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.
