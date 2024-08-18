import requests

token = '5150478513:AAEXOFPpo90hl3NtAPmMYFDNhp3Ohw-teHA'
CHAT_ID = "-1001767652609"
CHAT_SIGNAL_ID = 186
CHAT_BACK_TEST_ID = 187
CHAT_CHAT_ID = 188
CHAT_OUT_PUT_ID = 358
CHAT_FUTURE_SCALPING_ID = 394


def send_message_to_telegram(msg):
    sendMessage = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + CHAT_ID + '&text=' + msg
    requests.get(sendMessage)


def send_message_to_topic(message, topicId):
    url = f'https://api.telegram.org/bot{topicId}/sendMessage'
    requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'},
                  data=f'chat_id={CHAT_ID}&text=${message}&message_thread_id={CHAT_ID}')


def send_signals_to_telegram(message):
    send_message_to_topic(message, CHAT_SIGNAL_ID)


def sendBackTestToTelegram(message):
    send_message_to_topic(message, CHAT_BACK_TEST_ID)


def sendGeneralToTelegram(message):
    send_message_to_telegram(message)


def sendChatToTelegram(message):
    send_message_to_topic(message, CHAT_CHAT_ID)


def sendOutPutToTelegram(message):
    send_message_to_topic(message, CHAT_OUT_PUT_ID)


def send_future_scalping_to_telegram(message):
    send_message_to_topic(message, CHAT_FUTURE_SCALPING_ID)


def setup_messages(ticker, enterPrice, takeProfit, stopLoss, interval, signalType):
    message = f"{'🟠' if signalType == 'Short' else '🟢'}{ticker} || {signalType}\n"
    message += f"⚡ Enter at : {enterPrice}\n"
    message += f"⏰ Interval : {interval}\n"
    message += f"💰 TP : {takeProfit}\n"
    message += f"😅 SL : {stopLoss}\n\n"
    message += "⚡ BOT BUILD BY : @abd_alftah_al_shanti ⚡"
    return message
