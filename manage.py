from info import create_app

app = create_app('develop')


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()