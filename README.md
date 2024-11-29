# Fastapi_learnings
Learning fastapi level by level
200-Successful
400-Bad Request
500-internal server error
404-Not found


#  JWT Token
# Step 1: Install Required Libraries
To use JWT in FastAPI, you need the fastapi, pydantic, python-jose, and passlib libraries. Install them with:


#### pip install fastapi uvicorn python-jose passlib
python-jose: Used for encoding and decoding JWTs.
passlib: Useful for hashing and verifying passwords securely.

# Step 2: JWT Basics
A JWT has three parts:

##### Header: Specifies the algorithm used (e.g., HS256).
##### Payload: Contains claims (data, like user ID).
##### Signature: Verifies the token's integrity.
