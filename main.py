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
    
def parse_activity(events):
    if not events:
        print("Nenhuma atividade encontrada.")
        return
    
    for event in events[:5]: 
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        action = ""

        if event_type == "PushEvent":
            action = f"Fez push de {len(event['payload']['commits'])} commits para {repo_name}"
        elif event_type == "IssuesEvent":
            action = f"Abriu uma nova issue em {repo_name}"
        elif event_type == "WatchEvent":
            action = f"Favoritou {repo_name}"
        else:
            action = f"Realizou ação ({event_type}) em {repo_name}"

        print(f"- {action}")


if __name__ == "__main__":
    print("Bem-vindo à Github_CLI! Use: github-cli <username>")