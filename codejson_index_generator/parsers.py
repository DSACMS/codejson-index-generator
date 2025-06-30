import json
from json.decoder import JSONDecodeError
import base64
import argparse
import os
import requests

from time import sleep, mktime, gmtime, time, localtime
from typing import Dict, Optional

RETRIES = 5


def hit_endpoint(url,token,method='GET'):
    headers = {"Authorization": f"bearer {token}"}

    attempts = 0
    while attempts < RETRIES:

        response = requests.request(method, url, headers=headers,timeout=10)

        try: 
            if response.status_code == 200:
                response_json = json.loads(response.text)
                break
            elif response.status_code in (403,429):
                #rate limit was triggered.
                wait_until = int(response.headers.get("x-ratelimit-reset"))
                wait_in_seconds = int(
                    mktime(gmtime(wait_until)) -
                    mktime(gmtime(time()))
                )
                wait_until_time = localtime(wait_until)

                print(f"Ran into rate limit sleeping for {self.name}!")
                print(
                    f"sleeping until {wait_until_time.tm_hour}:{wait_until_time.tm_min} ({wait_in_seconds} seconds)"
                )
                sleep(wait_in_seconds)

                response_json = {}
                attempts += 1

                if attempts >= REQUEST_RETRIES:
                    raise ConnectionError(
                        f"Rate limit was reached and couldn't be rectified after {attempts} tries"
                    )
            else:
                raise ConnectionError("Rate limit error!")
        except JSONDecodeError:
            response_json = {}
            attempts += 1
    
    return response_json
            
        




class IndexGenerator:
    def __init__(self, agency: str, version: str, token: Optional[str] = None,):

        # user can change agency and version depending on parameters
        self.index = {
            "agency": agency,
            "version": version,
            "measurementType": {
                "method": "projects"
            },
            "releases": []
        }

    def get_code_json(self, repo: str) -> Optional[Dict]:
        try:
            content = repo.get_contents("code.json", ref = repo.default_branch)
        except GithubException as e:
            print(f"GitHub Error: {e.data.get('message', 'No message available')}")
            return None

        try:
            decoded_content = base64.b64decode(content.content)
            return json.loads(decoded_content)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"JSON Error: {str(e)}")
            return None
    
    def save_code_json(self, repo: str, output_path: str) -> Optional[str]:
        
        res = self.get_code_json(repo)

        if res:
            with open(output_path, 'w') as f:
                json.dump(res, f, indent=2)
        else:
            print(f"Error getting codejson file!")
        
        return res

    def update_index(self, index: Dict, code_json: Dict, org_name: str, repo_name: str) -> None:
        baseline = {
            'organization': org_name,
            'name': repo_name
        }

        baseline.update(code_json)
    
        index['releases'].append(baseline)

    def get_org_repos(self, org_name: str) -> list[Organization]:
        try:
            org = self.github.get_organization(org_name)
            print(f"\nProcessing organization: {org_name}")

            total_repos = org.public_repos
            print(f"Found {total_repos} public repositories")

            return total_repos
        except GithubException as e:
            raise e

    def save_organization_files(self, org_name: str, codeJSONPath) -> None:
        raise NotImplementedError

    def process_organization(self, org_name: str, add_to_index=True, codeJSONPath=None) -> None:
        try:
            org = self.github.get_organization(org_name)
            total_repos = self.get_org_repos(org_name)
            
            for id, repo in enumerate(org.get_repos(type='public'), 1):
                print(f"\nChecking {repo.name} [{id}/{total_repos}]")
                
                if not codeJSONPath:
                    code_json = self.get_code_json(repo)
                else:
                    repoPath = os.path.join(codeJSONPath, (repo.name + '.json'))
                    code_json = self.save_code_json(repo,repoPath)

                if code_json and add_to_index:
                    print(f"✅ Found code.json in {repo.name}")
                    self.update_index(self.index, code_json, org_name, repo.name)
                elif not code_json:
                    print(f"❌ No code.json found in {repo.name}")
                    
        except GithubException as e:
            print(f"Error processing organization {org_name}: {str(e)}")

    def save_index(self, output_path: str) -> None:
        # sorts index by organizaiton then by name
        self.index['releases'].sort(key=lambda x: (x.get('organization', ''), x.get('name', '')))

        with open(output_path, 'w') as f:
            json.dump(self.index, f, indent=2)
