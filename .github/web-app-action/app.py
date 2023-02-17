from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
