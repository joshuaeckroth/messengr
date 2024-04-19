import redis
import sys

r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

def check_user_credentials(username, password):
    if r.hget('users', username) == password:
        return True
    return False

if sys.argv[1] == 'register':
    username = sys.argv[2]
    password = sys.argv[3]
    admin_password = input('Enter admin password: ')
    if check_user_credentials('admin', admin_password):
        r.hset('users', username, password)
        print('User registered successfully')
    else:
        print('Invalid admin password')
elif sys.argv[1] == 'send':
    from_username = sys.argv[2]
    to_username = sys.argv[3]
    message = sys.argv[4]
    from_password = input('Enter your password: ')
    if check_user_credentials(from_username, from_password):
        r.rpush(f'{to_username}_messages', f'{from_username} says {message}')
        print('Message sent successfully')
    else:
        print('Invalid password')
elif sys.argv[1] == 'read':
    username = sys.argv[2]
    password = input('Enter your password: ')
    if check_user_credentials(username, password):
        message = r.lpop(f'{username}_messages')
        while message:
            print(message)
            message = r.lpop(f'{username}_messages')
    else:
        print('Invalid password')

