from bottle import get, request, run
import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='bottle_login',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor,
                             )


def is_right_credentials():
    name = request.json.get("name")
    hashed_password = request.json.get("hashed_password")

    try:
        with connection.cursor() as c:
            c.execute('SELECT TIME_TO_SEC(TIMEDIFF(current_timestamp, (select last_login_attempt from users where name = %s))) diff;',
                      (name))
            if c.fetchone()["diff"] < 5:
                return False
            c.execute(' SELECT * FROM users WHERE name = %s AND hashed_password = %s',
                      (name, hashed_password))
            if not c.fetchone():
                c.execute('UPDATE users SET last_login_attempt = CURRENT_TIMESTAMP WHERE name = %s;  ',
                          (name))
                return False
            return True
    except:
        return False


@get('/')
def secret_file():
    if not is_right_credentials():
        return 'Please send correct Username and password'
    else:
        return 'This is the secret content'


run(host='localhost', port=6500, reloader=True, debug=True)
