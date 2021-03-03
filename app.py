import subprocess
from flask import Flask, request

from config import repositories

app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    response = request.get_json()

    if 'action' not in response:
        return {'status': 'OK'}

    action = response["action"]
    merged = response["pull_request"]["merged"]
    base = response["pull_request"]["base"]["ref"]
    repository_name = response["repository"]["name"]

    if repository_name not in repositories or action != "closed" or merged is False:
        return {'status': 'OK'}

    repository = repositories[repository_name]
    branch = repository[base]

    for command in branch['commands']:
        print(command)
        subprocess.Popen(['sh', command, base], stdin=subprocess.PIPE)

    return {'status': 'OK', 'message': 'commands executed!'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
