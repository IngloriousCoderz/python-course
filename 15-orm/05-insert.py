# @see https://docs.sqlalchemy.org/en/20/tutorial/data_insert.html

# create metadata module before going forward
from tables import engine, user_table, address_table
from classes import User
from sqlalchemy import insert, select

stmt = insert(user_table).values(
    name="spongebob", fullname="Spongebob Squarepants")
print(stmt)

compiled = stmt.compile()
print(compiled)  # same as before
print(compiled.params)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()

print(result.inserted_primary_key)

print(insert(user_table))  # insert generates the 'values' clause automatically

with engine.begin() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ],
    )

print(insert(user_table))
print(insert(user_table).values())
# inserts only the default values, not supported by all backends
print(insert(user_table).values().compile(engine))

# insert...returning
insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address
)
print(insert_stmt)

# insert...from select
select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
)
print(insert_stmt)

# with mapped classes
print(insert(User))
print(insert(User).values())
print(insert(User).values().compile(engine))
