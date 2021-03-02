import subprocess
from flask import Flask, request

app = Flask(__name__)

repositories = {
    "test-blabla": {
        "shell_script_path": "/home/deploy/tests/pull_test.sh"
    }
}


@app.route("/", methods=['POST'])
def index():
    response = request.get_json()

    if 'action' in response:
        action = response["action"]
        merged = response["pull_request"]["merged"]
        base = response["pull_request"]["base"]["ref"]
        repository_name = response["repository"]["name"]

        if action == "closed" and merged is True and base == "dev":
            repository = repositories[repository_name]
            subprocess.Popen(repository['shell_script_path'])
            print(repository['shell_script_path'])
            print('Subprocess called!')

    return {'status': 'OK'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
