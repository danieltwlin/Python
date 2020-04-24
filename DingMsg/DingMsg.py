from dingtalkchatbot.chatbot import DingtalkChatbot

#WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=943d6b80848c94cb473d1e11234567890'

# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)

#Text消息@所有人
xiaoding.send_text(msg='我就是小丁，小丁就是我！', is_at_all=True)


