from lib.microdot import Microdot

app = Microdot()

@app.route('/', methods=['POST'])
def root():
