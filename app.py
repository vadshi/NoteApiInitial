from api import app
from config import Config


if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
