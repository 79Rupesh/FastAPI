# python Error 

# 1 name error
# variable exits nhi hota hai

# 2. Import error 
# module to mill gaya per. usme se requsted , thing nhi , mili



# 1. Database se releted Errors(POSTGRE SQL )

#  connention Refused

#  database start karne ke baad ye error aa sakata hai

# possible reasons:

# 1. database ka server down
# 2. Wrong Host
# 3. wrong Port
# 4. Wrong connection URL
# 5. Intenal / network problem


# 2. Athetication Failed

#  posibles reasons :
#

# 1. wrong username
# 2. wrong password
# 3. wrong database credetials


# 3. table does not exit

# select * FROM students;

# lekin table ka name :
#  student




# 4. colomn does not Exits.

# SELECT phone prom student;

# lekin phone colomn me hai hi nhi.

# ye error aayega "colomn Does not exit"




# 5. Duplicate Key

# email VARCHAR(100) UNIQUE
# rahul@gmail.com

#  duplicate key error aayega.


# rahul@gmail.com



# 6. not null violation

# name varchar(100) NOT NULL

# INSERT INTO students(name)
# VALUES(NULL)






