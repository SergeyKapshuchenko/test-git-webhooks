import subprocess
from flask import Flask, request

app = Flask(__name__)

repositories = {
    "test-git-webhooks": {
        "shell_script_path": "/home/deploy/tests/pull_test_git_webhooks.sh"
    }
}


@app.route("/", methods=['POST'])
def index():
    response = request.get_json()
    action = response["action"]
    merged = response["pull_request"]["merged"]
    base = response["pull_request"]["base"]["ref"]
    repository_name = response["repository"]["name"]

    if action == "closed" and merged is True and base == "dev":
        repository = repositories[repository_name]
        subprocess.Popen(repository['shell_script_path'])

    return {'status': 'OK'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
