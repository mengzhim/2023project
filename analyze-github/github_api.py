import requests
import json

def get_commit_data(repo, owner, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Error:", response.status_code)
        return []

# 使用示例
#data = get_commit_data(repo="repository_name", owner="owner_name", token="your_personal_access_token")
