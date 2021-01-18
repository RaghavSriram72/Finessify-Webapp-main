from cs50 import SQL

db = SQL("sqlite:///users.db")

rows = db.execute("SELECT * FROM users WHERE username = :username", username = "praneeth_041")

print(rows)