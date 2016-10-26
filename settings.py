#coding:utf-8

template_variables = dict(
    title=u'Docker管理平台',
    name =u'Docker管理平台',
    username="",
)

DATABASES = dict(
    DB='shipman',
    USERNAME='root',
    PASSWORD='123456',
    HOST='localhost',
    PORT=3306,
)

NODE_LIST = ['node_ip', 'port']

COOKIE_NAME  = "user_id"