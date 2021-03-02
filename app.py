from flask import Flask, request

app = Flask(__name__)

folders = {
    "test-git-webhooks": "this is path to folder"
}


@app.route("/", methods=['POST'])
def index():
    response = request.get_json()
    action = response["action"]
    merged = response["pull_request"]["merged"]
    base = response["pull_request"]["base"]["ref"]
    repository_name = response["repository"]["name"]

    if action == "closed" and merged is True and base == "dev":
        path_to_folder = folders[repository_name]
        print(path_to_folder)
        error = False
        message = 'trying to git pull'
    else:
        error = True
        message = 'something went wrong'

    return {
        'error': error,
        'message': message,
        'fields': {
            'action': action,
            'merged': merged,
            'repository_name': repository_name,
            'base': base
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
