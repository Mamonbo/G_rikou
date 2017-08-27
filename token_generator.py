#coding=UTF-8
import json
import mastodon

FilePointer=open('user.json','r')

#print(FilePointer)


Setting=json.load(FilePointer)
#print(Setting)
FilePointer.close()

# Register
# インスタンス毎に必要
mastodon.Mastodon.create_app(
    'global.rikou.don',
    api_base_url = Setting['url'],
    to_file = 'client_cred.txt'
)

# Login
# ユーザー毎のトークンも生成する
mstdn_handler=mastodon.Mastodon(
    client_id = 'client_cred.txt',
    api_base_url = Setting['url']
)

mstdn_handler.log_in(
    Setting['usermail'],
    Setting['password'],
    to_file = 'user_cred.txt'
)
