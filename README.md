# COMP2001-Information-Management

ProfileService is a RESTful microservice developed for the COMP2001 Information Management and Database.
It manages user profile data for the Trail Application, provivind CRUD (Create, Read, Update, Delete)

Features
- Create new user profiles
- Update exisiting profile records
- Delete profiles
- Docker containerisation for deployment


Technologies Used
- Python 3
- Flask
- Docker
- Postman (for API testing)


API Endpoints

Method  Endpoint  Description
POST     /profiles Create a new profile
GET     /profiles  Retreive all profile
PUT     /profiles/{id} Update an exisiting profile
DELETE  /profiles/{id} Delete a profile

Testing
The API was tested using Postman and a web browser to validate all CRUD operations.
Each request returns structured JSON responses
