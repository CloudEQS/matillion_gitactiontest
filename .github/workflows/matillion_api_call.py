# import time
import requests
import json
import sys
import os
print("Arguments passed")
print(sys.argv)  # Print the list of command-line arguments

user = ""
password = ""
project_env = ""
group = ""
version = ""
instance = ""
repo_username = ""
reps_password = ""
commitid = ""
#commitid = os.environ.get("COMMIT_ID")
#print(commitid)

arglength = len(sys.argv)
print("Arguments passed")
print(sys.argv)
print(arglength)

if arglength > 0:
    user = sys.argv[1]
    password = sys.argv[2]
    project = sys.argv[3]
    group = sys.argv[4]
    version = sys.argv[5]
    instance = sys.argv[6]
    repo_username = sys.argv[7]
    reps_password = sys.argv[8]
    commitid = sys.argv[9]
    


# code to pull the latest job code from Azure repos to matillion

azrepopull_url = '{0}/rest/v1/group/name/{1}/project/name/{2}/scm/fetch'.format(instance, group, project)
body = {
    "auth": {
        "authType": "HTTPS",
        "username": repo_username,
        "password": reps_password
    },
    "fetchOptions": {
        "removeDeletedRefs": "true",
        "thinFetch": "true"
    }
}
res_azrepo = requests.post(azrepopull_url, json=body, auth=(str(user), str(password)), verify=False)

azrepo_status = json.loads(res_azrepo.text)
print(azrepo_status)


