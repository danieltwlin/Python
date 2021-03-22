from dingtalkchatbot.chatbot import DingtalkChatbot

# Must install DingtalkChatbot 
# pip install DingtalkChatbot

def DingMsg(msg):
  #WebHook地址
  webhook = 'https://oapi.dingtalk.com/robot/send?access_token=xxxx'

  # 初始化机器人小丁
  xiaoding = DingtalkChatbot(webhook)

  #Text消息@所有人
  xiaoding.send_text(msg, is_at_all=True)


