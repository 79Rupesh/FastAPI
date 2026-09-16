# jwt = json web Tokens
# json = javascript object notation 


from jose import jwt

SECRET_KEY = "technoskill123"
ALGORITHM = "HS256"

data={
    "email":"rahul@gmail.com",
    "role":"admin"
}

token = jwt.encode(
    data,SECRET_KEY,
    algorithm=ALGORITHM
)

print(token)