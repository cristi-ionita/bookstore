# Why this folder named like api since api it is a whole interface with all layers?

## Tasks for self learning:
1. what is API
2. what is RestAPI
3. profs and cons of layers
4. what is endpoint, path, route, domain name, segment or url?
5. HTTP methods (GET, POST, PUT, DELETE, PATCH need to know how to use since they are in rest api)


## Short description of our architecture
Our rest api contains from different layers.
* Application layer
* Domain layer
* Infrastructure layer
All of them part of api, so they are included into.
You could not use flat structure of files since you structure does not represent main idea and does not declare meaning.
Lets say book_store in root it is our api folder
Everything that placed inside are components of this api so not the best idea name application part like api.
It is not the same.

### API vs Application Layer
#### API (Application Programming Interface)
* What: The entire interface that external clients use to interact with your system
* Scope: The whole bookstore system exposed to outside world
* Includes: All layers working together (Application + Domain + Infrastructure)
* Example: /books, /authors, /orders endpoints
#### Application Layer
* What: One specific layer in clean architecture
* Scope: Orchestrates business logic and handles requests/responses
* Role: Coordinates between external requests and domain logic
* Example: BookService, AuthorService classes

* API = The entire book_store system
* Application Layer = Just the service/handler part inside the API
* Don't name a folder "api" when it's just the application layer


### Here is a desired structure

```
book_store/           # ← This IS your API
  application/        # Application layer
    services/
    handlers/
  domain/            # Domain layer
    models/
    repositories/
  infrastructure/    # Infrastructure layer
    database/
    external_apis/
  routes
```