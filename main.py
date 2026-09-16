from fastapi import FastAPI , HTTPException

from database import conn , cursor

from passlib.context import CryptContext

from models import Member, Plan , Trainer , Attendence ,Payment ,User ,Login

from fastapi.middleware.cors import CORSMiddleware

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/members")
def add_member(member:Member):
    cursor.execute(

        """
        INSERT INTO members(name,mobile,plan,fees)
        VALUES(%s,%s,%s,%s)
        """,
        (
            member.name,
            member.mobile,
            member.plan,
            member.fees
        )

    )
    conn.commit()

    return {
        "message" "Member Added Succesfully"
    }

#  get all members


@app.get("/members")
def get_members():

    cursor.execute("SELECT * FROM members")

    members = cursor.fetchall()

    data = []


    for member in members:

        data.append({

            "id":member[0],
            "name":member[1],
            "mobile":member[2],
            "plan":member[3],
            "fees":float(member[4])
        })

    return data




# get member by id

@app.get("/members/{id}")
def get_member(id:int):

    cursor.execute(
        "SELECT * FROM members WHERE id=%s",
        (id,)
    )

    member = cursor.fetchone()

    if member is None:

        raise HTTPException(
            status_code=404,
            detail="Member Not Found"
        )
    
    return {

        "id":member[0],
        "name":member[1],
        "mobile":member[2],
        "plan":member[3],
        "fees":float(member[4])

    }


# ----- UPDATE MEMBER ------


@app.put("/members/{id}")
def update_member(id:int, member: Member):

    cursor.execute(

        """
        UPDATE members
        SET name=%s,
            mobile=%s,
            plan=%s,
            fees=%s
        WHERE id = %s
        """,

        (
            member.name,
            member.mobile,
            member.plan,
            member.fees,
            id
        )
    )

    conn.commit()

    return {
        "message" : "Member Updated Succesfully"
    }


# ------ Delete Member --------

@app.delete("/members/{id}")

def delete_member(id:int):

    cursor.execute(
        "DELETE FROM members WHERE id=%s",
        (id,)
    )

    conn.commit()

    if cursor.rowcount==0:
        raise HTTPException(
            status_code=404,
            detail="Member Not Found"
        )

    return {
        "message" : "Member Deleted Succesfully"
    }




# ------- MEMBERSHIP PLANS APIS -----------

# plans add

@app.post("/plans")
def add_plan(plan : Plan):

    cursor.execute (
        """
        INSERT INTO plans
        (plan_name,duration_months,price,description)
        VALUES(%s,%s,%s,%s)
        """,

        (
            plan.plan_name,
            plan.duration_months,
            plan.price,
            plan.description
        )
    )

    conn.commit()

    return {"message" : "Plan Added Succesfully"}

# plans get all plans

@app.get("/plans")
def get_plans():

    cursor.execute("SELECT * FROM plans")

    plans = cursor.fetchall()

    data = []


    for plan in plans:

        data.append({
            "id":plan[0],
            "plan_name":plan[1],
            "duration_month":plan[2],
            "price":plan[3],
            "description":plan[4]
        })
        
    return data


# Get plan by id

@app.get("/plans/{id}")

def get_plan(id : int):

    cursor.execute(
        "SELECT * FROM plans WHERE id=%s",
        (id,)
    )

    plan = cursor.fetchone()
    if plan is None:
        raise HTTPException(
            status_code=404,
            detail="Plan Not Found"

        )
    return {

            "id":plan[0],
            "plan_name":plan[1],
            "duration_month":plan[2],
            "price":plan[3],
            "description":plan[4]

    }


# ------- Trainer APIS ----------


@app.post("/trainers")
def add_trainer(trainer: Trainer):

    cursor.execute(
        """

        INSERT INTO trainers
        (name,mobile,specialization,experience,salary)
        VALUES(%s,%s,%s,%s,%s)

        """,
        (
            trainer.name,
            trainer.mobile,
            trainer.specialization,
            trainer.experience,
            trainer.salary
        )
    )

    conn.commit()

    return {"message" : "Trainer Added Succesfully"}   

@app.get("/trainers")
def get_trainers():

    cursor.execute("SELECT * FROM trainers")
    trainers = cursor.fetchall()

    data = []

    for trainer in trainers:

        data.append({
            "id":trainer[0],
            "name":trainer[1],
            "mobile":trainer[2],
            "specialization":trainer[3],
            "experience":trainer[4],
            "salary":trainer[5]
        })

    return data


# ------- attendence start here -------

@app.post("/attendence")
def mark_attendence(attendence: Attendence):

    cursor.execute(
        """

        INSERT INTO attendence
        (member_id,attendence_date,check_in,check_out)
        VALUES(%s,%s,%s,%s)

        """,
        (
            attendence.member_id,
            attendence.attendence_date,
            attendence.check_in,
            attendence.check_out,

        )
    )

    conn.commit()

    return {"message" : "Attendence Marked Succesfully"}  


#  ------- POST Payment ---------

@app.post("/payments")
def add_payment(payment: Payment):

    cursor.execute(

        """
        INSERT INTO payments
        (member_id,amount,payment_date,payment_method,status)
        VALUES(%s,%s,%s,%s,%s)
        """,

        (
            payment.member_id,
            payment.amount,
            payment.payment_date,
            payment.payment_method,
            payment.status

        )
    )

    conn.commit()

    return {
        "message" : "Payment added successfully"
    }


# Get all payments

@app.get("/payments")
def get_payments():

    cursor.execute("SELECT * FROM payments")

    payments = cursor.fetchall()

    data = []

    for payment in payments:

        data.append({

            "id":payment[0],
            "member_id":payment[1],
            "amount":float(payment[2]),
            "payment_date":str(payment[3]),
            "payment_method":payment[4],
            "status":payment[5]
        }

        )

    return data



# ----- Payment History ------

@app.get("/members/{id}/payments")

def member_payments(member_id:int):

    cursor.execute(
        "SELECT * FROM payments WHERE member_id=%s",
        (member_id,)
    )

    payments = cursor.fetchall()

    data = []

    for payment in payments:

        data.append({
            "id":payment[0],
            "amount":float(payment[1]),
            "payment_date":str(payment[2]),
            "payment_method":payment[3],
            "status":payment[4]

        })

    return data

# today's attendence

@app.get("/attendence/today")
def today_attenence():

    cursor.execute(

        """
        SELECT * FROM attendence
        WHERE attendence_date = CURRENT_DATE
        """
    )

    records = cursor.fetchall()

    data = []

    for record in records:
        data.append({
            "id":record[0],
            "member_id":record[1],
            "attendence_date":str(record[2]),
            "check_in":str(record[3]),
            "check_out":str(record[4]) if record[4] else None

        })

# Total Present members

@app.get("/attendence/count")
def attendence_count():

    cursor.execute(

        """
        SELECT COUNT(*)
        from attendence
        WHERE attendence_date = CURRENT_DATE
        """
    )

    total = cursor.fetchone()

    return {
        "present_members": total[0]
    }

# ------- Dashboard Api  -------

@app.get("/dashboard")
def dashboard():

    cursor.execute("SELECT COUNT(*) FROM members")
    total_members = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM trainers")
    total_trainers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM plans")
    total_plans = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendence
        WHERE attendence_date = CURRENT_DATE
        """
    )
    today_attendence = cursor.fetchone()[0]

    # cursor.execute("""
    #                 SELECT SUM(amount)
    #                 from payments
    #                 WHERE status="paid"
    #                 """)

    # revenue = cursor.fetchone()[0]

    return {
        "total_members":total_members,
        "total_trainers":total_trainers,
        "total_plans":total_plans,
        "today_attendence":today_attendence,
        # "total_revenue":float(revenue or 0)
    }


#  ---- Login---

@app.post("/register")
def register(user : User):

    hashed_password = pwd_context.hash(user.password)

    cursor.execute(
        "SELECT * FROM users WHERE email =%s",
        (user.email,)

    )

    # existing_user = cursor.fetchone()

    # IF EXISTING_USER


    # hashed_password = pwd_context.hash(user.password)

    cursor.execute(
        """
            INSERT INTO users
            (name,email,password,role)
            VALUES(%s,%s,%s,%s)
        """,

        (
            user.name,
            user.email,
            hashed_password,
            user.role
        )
    )

    conn.commit()

    return{
        "message":"user Register succefully"
    }

# ---login Api--

@app.post("/login")
def login(login :Login):

    cursor.execute(
        """
            SELECT * FROM users
            WHERE email=%s
            AND password=%s

        """,
        (
            login.email,

            login.password
        )


    )

    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email or password"
        )

    stored_password = user[3]

    if not pwd_context.verify(
        login.password,
        stored_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    return{
        "message":"Login succefully",

        "user":{
            "id":user[0],
            "name":user[1],
            "email":user[2],
            "role":user[3]
        }
    }


# --- Get All Users ---

@app.get("/users")
def get_users():

    cursor.execute(
        "SELECT * FROM users"
    )


    users=cursor.fetchall()

    data=[]

    for user in users:
        data.append(
            {
                "id":user[0],
                "name":user[1],
                "email":user[2],
                "role":user[3]
            }
        )

    return data


