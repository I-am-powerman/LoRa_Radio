from lib.microdot import Microdot
import json

app = Microdot()

# временное хранилище сообщений 
messages = []

# --- Маршрут 1: отдать HTML страницу ---
@app.route('/')
def index(request):
    with open('index.html', 'r') as f:
        html = f.read()
    return html, 200, {'Content-Type': 'text/html'}

# --- Маршрут 2: принять сообщение ---
@app.route('/send', methods=['POST'])
def send(request):
    data = request.json          # читаем тело запроса
    text = data['text']          # достаём текст
    messages.append(text)        # сохраняем
    return 'ok', 200             # отвечаем браузеру

# --- Маршрут 3: отдать список сообщений ---
@app.route('/messages')
def get_messages(request):
    return json.dumps(messages), 200, {'Content-Type': 'application/json'}

app.run(host='0.0.0.0', port=80)