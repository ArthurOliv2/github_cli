import sys
import urllib.request
import json

def fetch_github_CLI(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except urllib.error.HTTPError as e:
        print(f"Erro ao buscar dados: {e.reason}")
        return None

if __name__ == "__main__":
    print("Bem-vindo à Github_CLI! Use: github-cli <username>")