# SAFE: Rate Limiter enforcement
@app.route('/login', methods=['POST'])
@limiter.limit('5 per minute')
def login(): return auth()