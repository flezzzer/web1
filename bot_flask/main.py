from flask import Flask
from flask import request
import re
from flask.views import MethodView
import requests
from flask import jsonify
import os

app = Flask("__name__")



tg_url = f"https://api.telegram.org/bot7024338940:AAFfKkUPH-cj4F_j3ozi5hxo_tX58SsBcyM/sendMessage"


# @app.route('/', methods=['POST','GET'])
# def abc():
#     if request.method == 'POST':
#         response = request.get_json()
#         print(response)
#     return " "

api_url = 'http://127.0.0.1:8000/api/v1'

def get_from_request(command:str):
    if command[0]=='/':
        url = api_url+command+'/'
    else:
        command = command[1:]
        url = api_url+'/courses/?category='+command

    print(url)
    response = requests.Session()
    r = response.get(url=url).json()
    return r

def send_message(chat_id, text):
    session = requests.Session()
    r = session.get(tg_url, params={'chat_id': chat_id, 'text': text})
    return r.json()


def parse(command):
    message = ''
    r = '@\w+'
    if command:
        if '/start' in command:
            return 'Это тест бот для работы с апи моего pet-проекта для продажи курсов'
        elif '/help' in command:
            return 'Используй команду /categories, чтобы увидеть доступные категории, чтобы сделать поиск по категории используйте комманду "@name_of_category"'
        elif '/categories' in command:
            return [command]
        elif '@' in command:
            result = re.findall(r, command)
            strings = [s for s in result]
            return strings
        else:
            return 'Неверный запрос'
    return message
class BotAPI(MethodView):
    def get(self):
        return ""

    def post(self):
        response = request.get_json()
        chat_id = response['message']['chat']['id']
        text = response['message']['text']
        mes = parse(text)
        msg=''
        message=''
        if mes:
            if len(mes) > 10:
                send_message(chat_id, mes)
            else:
                response = get_from_request(mes[0])
                if response:
                    message = ''
                    if mes[0][0] == '@':
                        for i in response:
                            message += "Название: "+i['title']+'\n' + "Цена, в долларах: "+str(i['price'])+'\n' + "Количество учеников: "+str(i['students_qty'])+'\n'+"Количество отзывов: "+str(i['reviews_qty'])+'\n\n'
                    else:
                        for i in response:
                            message += i['title']+'\n'
                    if mes[0] == '/categories':
                        msg = 'Доступные категории: \n'
                    else:
                        msg = 'Доступные курсы по категории: \n'

            send_message(chat_id, msg+message)

        return ""
app.add_url_rule('/TOKEN/', view_func=BotAPI.as_view('bot'))


if __name__ == "__main__":
    app.run()