# SAFE: Parameterized Query using DB-API placeholders
query = "SELECT * FROM users WHERE username = %s AND status = %s"
cursor.execute(query, (request.form['user'], 'active'))