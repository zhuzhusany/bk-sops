# -*- coding: utf-8 -*-
from conf.default import SITE_URL, STATIC_URL

# 是否开启使用
USE_WEIXIN = True
# django 配置, 可使用自定义HOST
USE_X_FORWARDED_HOST = USE_WEIXIN
# 微信公众号的app id和app secret
WEIXIN_APP_ID = ''
WEIXIN_APP_SECRET = ''
# 该蓝鲸应用对外暴露的外网域名，即配置的微信能回调或访问的域名，如：test.bking.com
WEIXIN_APP_EXTERNAL_HOST = ''
# 应用授权作用域
# snsapi_base （不弹出授权页面，直接跳转，只能获取用户openid），
# snsapi_userinfo （弹出授权页面，可通过openid拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息 ）
WEIXIN_SCOPE = 'snsapi_base'

# 蓝鲸微信请求URL前缀
WEIXIN_SITE_URL = SITE_URL + 'weixin/'
# 蓝鲸微信本地静态文件请求URL前缀
WEIXIN_STATIC_URL = STATIC_URL + 'weixin/'
# 蓝鲸微信登录的URL
WEIXIN_LOGIN_URL = SITE_URL + 'weixin/login/'