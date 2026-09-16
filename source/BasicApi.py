# Topic 1 :

# What is Backend ?

# Koi Bhi Full Stack Website 4 Components se milkr bnti hai 

# Data lena , Database se baat krna , Response  dena


# Frontend - > HTML CSS JS React JS
# API (Waiter) - > FastApi ya phir Node js
# Backend - > api kee request ko process krna - > Node js , fastapi , django
# Database - > NoSql , SQL



# NOSQL,SQL

# SQL - > PostGreSQL , MYsql , Sqllite3
# NOSQL - > MongoDB - collection ke form



# Topic 2:
# What is API ?

# API (Application Programming Interface)
# Frontend aur backend ko connect krta hai , dono
# ke bich communication ka kaaam krta hai ?


# Topic 3
# Client & Server


# Client -> Request - > Server -> Response -> Client


# Topic 4 :
# HTTP REQUEST

# HTTP Request ek message hai jo client (Browser/ Mobile App) Server ko bhjeta hai , 
# data maangne yaa data bhejne ke liye

# Browser - > Request - > Server - > Response 


# HTTP rquest ke 4 parts

# 1. Method
# 2. URL : http://127.0.0.1:8000/dashboard
# 3. Headers
# 4. Body

# Method :
# get
# post
# put
# delete
# patch

# URL :

# http://127.0.0.1:8000/dashboard

# Batata hai kee kis resources par request bhejna hai

# Headers:

# Extra info

# Content-type : applocation/json
# Authorization : Bearrer Token

# Body :


# {
#   "name": "mohit",
#   "email": "mohit@gmail.com",
#   "password": "mohit",
#   "role": "members"
# }






# post method
# client -> post/member -> new member data ->  Database

# request body :
# {
#     "name":rahul
#     "age":22

# }



# put


# database update krne ke liye
# client -> put /member/1 -> update data

# patch 
# data ko partail uodate karne ke liye
# 


#  dalete
# delete karne ke liye

# client -> delete /memberd/1 -> delete member


#  mobile app example 
#  instragram app -> ge/posts -> instragram server -> posts -> mobile screen 

# 



#  Topic 5 : 
#  install Fastapi
#  pip install fastapi
# pip install uvicorn 

#  Topic 6: swagger
#  open
# http://127.0.0.1:8000/dashboard

# 1.  intractive  api dashboard
# 2.  test Apis 
# 3. postman not needed


# Topic 7:  API Anatomy

# @app.get("/student")
# def get_student():
#     return { "message " : "hello"}


# 1. @app.get

# get method
#  2. students
# route

# def grt_student()

# function

# 4. response
# return

# Topic 08: JSON

# {
#     "name":"rahul",
#     "age":22
# }

# json rules :
# 1. keys always string
# 2. value string/int/bool/list/object

# Topic 9:

#  return type
# return "hello"

# return 100
# return{
#     "name":"Rupedh"

# }


# return[
#     {
#         "name":"Rahul"
#     },
#     {
#         "name":"Amit"
#     }
# ]


# status code : 

# 200 K - success
# 404 - Not found
# 500 - Internal erver Error

# 503 - server band hai

# Topic 10
# Uvicorn :
# ASGI server hai jo fastapi application ko run karta hai.
#  ASGI - asnchronus , server , gatway , Interface
#  fastapi aur uvicorn ko connect 