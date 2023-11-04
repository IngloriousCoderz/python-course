# @see https://docs.sqlalchemy.org/en/20/tutorial/data_select.html
from tables import engine, user_table
from classes import Address, User
from sqlalchemy import insert, select
from sqlalchemy.orm import Session

with engine.begin() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "spongebob", "fullname": "Spongebob Squarepants"},
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ],
    )

# with tables
stmt = select(user_table).where(user_table.c.name == "spongebob")
print(stmt)

with engine.begin() as conn:
    for row in conn.execute(stmt):
        print(row)

# with mapped classes
stmt = select(User).where(User.name == "spongebob")
with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)
    session.commit()

# select specific columns
print(select(user_table))
print(select(user_table.c.name, user_table.c.fullname))

# with mapped classes
print(select(User))
print(select(User.name, User.fullname))

# take only the first element
with Session(engine) as session:
    row = session.execute(select(User)).first()
    print(row)  # still a tuple
    print(row[0])
    session.commit()

# scalars returns one element (a scalar result)
with Session(engine) as session:
    row = session.scalars(select(User)).first()
    print(row)
    session.commit()

# selecting columns will necessarily return a tuple instead of a User object
with Session(engine) as session:
    row = session.execute(select(User.name, User.fullname)).first()
    print(row)
    session.commit()

# combining tuples with full objects:

# first we need to insert some addresses
select_stmt = select(User.id, User.name + "@aol.com")
insert_stmt = insert(Address).from_select(
    ["user_id", "email_address"], select_stmt
)
with Session(engine) as session:
    session.execute(insert_stmt)
    session.commit()

# here we return tuples of strings and Address objects
with Session(engine) as session:
    row = session.execute(
        select(User.name, Address).where(
            User.id == Address.user_id).order_by(Address.id)
    ).all()
    print(row)
    session.commit()

# show where clause in docs: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#the-where-clause
