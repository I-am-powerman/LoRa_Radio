import asyncio
import json

# Временное хранилище сообщений
messages = []

def handle_request(request_text):
    """Разобрать запрос и вернуть ответ"""
    try:
        first_line = request_text.split('\r\n')[0]
        method = first_line.split(' ')[0]
        path   = first_line.split(' ')[1]
    except:
        return b'HTTP/1.1 400 Bad Request\r\n\r\n'

    # --- GET / → отдать HTML страницу ---
    if method == 'GET' and path == '/':
        with open('index.html', 'r') as f:
            html = f.read()
        response  = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type: text/html\r\n\r\n'
        response += html
        return response.encode()

    # --- GET /messages → список сообщений ---
    if method == 'GET' and path == '/messages':
        body      = json.dumps(messages)
        response  = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type: application/json\r\n\r\n'
        response += body
        return response.encode()

    # --- POST /send → принять сообщение ---
    if method == 'POST' and path == '/send':
        body = request_text.split('\r\n\r\n')[1]
        data = json.loads(body)
        msg = {
            'text':   data['text'],
            'sender': 'me',
            'time':   data.get('time', '--:--')
        }
        messages.append(msg)
        print('Новое сообщение:', msg['text'])
        return b'HTTP/1.1 200 OK\r\n\r\nok'

    return b'HTTP/1.1 404 Not Found\r\n\r\nNot found'


async def handle_connection(reader, writer):
    """Вызывается автоматически на каждое новое подключение"""
    try:
        request = await reader.read(4096)
        response = handle_request(request.decode('utf-8'))
        writer.write(response)
        await writer.drain()
    except Exception as e:
        print('Ошибка:', e)
    finally:
        writer.close()
        await writer.wait_closed()

async def run_web(host='0.0.0.0', port=80):
    server = await asyncio.start_server(handle_connection, host, port)
    print(f'Веб сервер запущен на {host}:{port}')
    await server.wait_closed()