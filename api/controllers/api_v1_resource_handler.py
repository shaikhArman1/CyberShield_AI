# SAFE: DB-API Parameterized Query placeholder
query = "SELECT * FROM records WHERE user_input = %s"
cursor.execute(query, (request.args.get('q'),))