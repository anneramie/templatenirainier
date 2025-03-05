from website import create_website, db, socketio
from website.extensions import ip_address


app = create_website()




if __name__ == "__main__":
    socketio.run(app, debug=True)
