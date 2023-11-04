# @see https://docs.sqlalchemy.org/en/20/intro.html
# show architectural diagram

# import sqlalchemy
# print(sqlalchemy.__version__)

# @see https://docs.sqlalchemy.org/en/20/tutorial/engine.html

from sqlalchemy import create_engine, text

# no connection is established yet (lazy)
engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

# @see https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html

# operation is already framed inside of a transaction
# ROLLBACK ends the transaction, which is not committed automatically
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

# "commit as you go": need to explicitly commit transaction
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE points (x int, y int)"))
    conn.execute(text("INSERT INTO points (x, y) VALUES (:x, :y)"), [
                 {'x': 1, 'y': 1}, {'x': 2, 'y': 4}])
    conn.commit()

# "begin once": the begin method auto-commits
with engine.begin() as conn:
    conn.execute(text("INSERT INTO points (x, y) VALUES (:x, :y)"), [
                 {'x': 6, 'y': 8}, {'x': 9, 'y': 10}])

# fetching data
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM points"))
    for x, y in result:
        print(f"x: {x}  y: {y}")
    # for row in result:
    #     print(f"x: {row[0]}  y: {row[1]}")
    # for row in result:
    #     print(f"x: {row.x}  y: {row.y}")
    # for dict_row in result.mappings():
    #     print(f"x: {dict_row['x']}  y: {dict_row['y']}")

# sending parameters
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT x, y FROM points WHERE y > :y"), {"y": 2})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
