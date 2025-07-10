import json
from json.decoder import JSONDecodeError
import base64
import argparse
import os
import requests
import re
import subprocess

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
                print(response.status_code)
                raise ConnectionError("Rate limit error!")
        except JSONDecodeError:
            response_json = {}
            attempts += 1
    
    return response_json
            
        
def get_repo_owner_and_name(repo_http_url):
    """ Gets the owner and repo from a url.

        Args:
            url: Github url

        Returns:
            Tuple of owner and repo. Or a tuple of None and None if the url is invalid.
    """

    # Regular expression to parse a GitHub URL into two groups
    # The first group contains the owner of the github repo extracted from the url
    # The second group contains the name of the github repo extracted from the url
    # 'But what is a regular expression?' ----> https://docs.python.org/3/howto/regex.html
    if 'github' in repo_http_url:
        regex = r"https?:\/\/github\.com\/([A-Za-z0-9 \- _]+)\/([A-Za-z0-9 \- _ \.]+)(.git)?\/?$"
    elif 'gitlab' in repo_http_url:
        regex = r"https?:\/\/gitlab\.com\/([A-Za-z0-9 \- _]+)\/([A-Za-z0-9 \- _ \.]+)(.git)?\/?$"
    elif 'bitbucket' in repo_http_url:
        regex = r"https?:\/\/bitbucket\.org\/([A-Za-z0-9 \- _]+)\/([A-Za-z0-9 \- _ \.]+)(.git)?\/?$"

    result = re.search(regex, repo_http_url)

    if not result:
        return None, None

    capturing_groups = result.groups()

    owner = capturing_groups[0]
    repo = capturing_groups[1]

    return owner, repo



class IndexGenerator:
    def __init__(self, agency: str, version: str, token: Optional[str] = None, bitbucket_user: Optional[str] = None, bitbucket_password: Optional[str] = None, gitlab_token: Optional[str] = None):

        # user can change agency and version depending on parameters
        self.index = {
            "agency": agency,
            "version": version,
            "measurementType": {
                "method": "projects"
            },
            "releases": []
        }

        self.token = token
        self.gitlab_token = gitlab_token
        self.bitbucket_user = bitbucket_user
        self.bitbucket_password = bitbucket_password

    def get_code_json_github(self,repo : str) -> Optional[Dict]:
        try:
            owner,name = get_repo_owner_and_name(repo)
            code_json_endpoint = f"https://api.github.com/repos/{owner}/{name}/contents/code.json"
            content_dict = hit_endpoint(code_json_endpoint,self.token)#repo.get_contents("code.json", ref = repo.default_branch)
        except Exception as e:
            print(f"GitHub Error: {e}")
            return None

        try:
            decoded_content = base64.b64decode(content_dict['content'])
            return json.loads(decoded_content)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"JSON Error: {str(e)}")
            return None
    
    def get_code_json_gitlab(self,repo: str) -> Optional[Dict]:
        try:
            owner,name = get_repo_owner_and_name(repo)
            code_json_endpoint = f"https://gitlab.com/api/v4/projects/{owner}%2F{name}/repository/files/code.json?ref=HEAD"
            content_dict = hit_endpoint(code_json_endpoint,self.gitlab_token)
        except Exception as e:
            print("Problem querying the Gitlab API")
            return None

        try:
            decoded_content = base64.b64decode(content_dict['content'])
            return json.loads(decoded_content)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"JSON Error {e}")
            return None

    def get_code_json_bitbucket(self,repo: str) -> Optional[Dict]:
        try:
            owner, name = get_repo_owner_and_name(repo)
            code_json_endpoint = f"https://bitbucket.org/{owner}/{name}/raw/HEAD/code.json"
            session = requests.Session()
            session.auth = (self.bitbucket_user,self.bitbucket_password)

            auth = session.post('http://bitbucket.org')
            response_dict = session.get(code_json_endpoint)
        except Exception as e:
            print(f"Exception when querying bitbucket.org: {e}")

        return json.loads(response_dict.text)

    def get_code_json(self, repo: str) -> Optional[Dict]:
        if 'github' in repo:
            return self.get_code_json_github(repo)
        elif 'gitlab' in repo:
            return self.get_code_json_gitlab(repo)
        elif 'bitbucket' in repo:
            return self.get_code_json_bitbucket(repo)
        else:
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

    def get_github_org_repos(self, org_name: str) -> list[Dict]:
        try:
            org_endpoint = f"https://api.github.com/orgs/{org_name}/repos"
            print(f"\nProcessing organization: {org_name}")

            repo_list = hit_endpoint(org_endpoint,self.token)


            total_repos = len(repo_list)
            print(f"Found {total_repos} public repositories")

            return repo_list
        except Exception as e:
            raise e

    def _enumerate_repo_orgs(self,id,org_name,repo_name, url, total_repos, codeJSONPath=None,add_to_index=True):
        print(f"\nChecking {repo_name} [{id}/{total_repos}]")
        
        if not codeJSONPath:
            code_json = self.get_code_json(url)
        else:
            repoPath = os.path.join(codeJSONPath, (repo_name + '.json'))
            code_json = self.save_code_json(url,repoPath)

        if code_json and add_to_index:
            print(f"✅ Found code.json in {repo_name}")
            self.update_index(self.index, code_json, org_name, repo_name)
        elif not code_json:
            print(f"❌ No code.json found in {repo_name}")

    def process_github_org_files(self, org_name: str, add_to_index=True, codeJSONPath=None) -> None:
        orgs = self.get_github_org_repos(org_name)
        total_repos = len(orgs)

        for id, repo in enumerate(orgs, 1):
            try:
                self._enumerate_repo_orgs(
                    id,org_name,repo['name'],repo['svn_url'],total_repos,codeJSONPath=codeJSONPath,add_to_index=add_to_index
                )
            except Exception as e:
                print(e)
    
    def get_gitlab_org_repos(self, org_name: str) -> list[Dict]:
        try:
            url_encoded_org_name = org_name.replace("/","%2F")
            org_endpoint = f"https://gitlab.com/api/v4/groups/{url_encoded_org_name}/projects"
            
            repo_list = hit_endpoint(org_endpoint,self.gitlab_token)

            total_repos = len(repo_list)
            print(f"Found {total_repos} public repositories")
            
            return total_repos
        except Exception as e:
            print(f"Ran into Exception when querying Gitlab Repos in group {org_name}: {e}")
            return None

    def process_gitlab_org_files(self, org_name: str, add_to_index=True, codeJSONPath=None) -> None:
        try:
            orgs = self.get_gitlab_org_repos(org_name)
            total_repos = len(orgs)
            
            for id, repo in enumerate(orgs, 1):
                self._enumerate_repo_orgs(
                    id,org_name,repo['name'],repo['web_url'],total_repos,codeJSONPath=codeJSONPath,add_to_index=add_to_index
                )
                    
        except Exception as e:
            print(f"Error processing organization {org_name}: {str(e)}")

    def save_index(self, output_path: str) -> None:
        # sorts index by organization then by name
        self.index['releases'].sort(key=lambda x: (x.get('organization', ''), x.get('name', '')))

        with open(output_path, 'w') as f:
            json.dump(self.index, f, indent=2)
