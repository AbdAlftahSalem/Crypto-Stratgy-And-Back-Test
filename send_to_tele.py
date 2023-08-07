import requests

token = '5150478513:AAEXOFPpo90hl3NtAPmMYFDNhp3Ohw-teHA'
chatId = "-1001767652609"


def sentToTelegram(msg):
    sendMessage = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatId + '&text=' + msg
    requests.get(sendMessage)
