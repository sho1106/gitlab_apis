import pip

pip.main(["install","python-gitlab"])

import gitlab
from datetime import datetime, timedelta
from config import GITLAB_TOKEN, GITLAB_URL

ACTION_KEY = "action_name"
TARGET_TYPE = "target_type"

class GitLabStats:
    def __init__(self, username):
        self.gl = gitlab.Gitlab(GITLAB_URL, private_token=GITLAB_TOKEN)
        self.username = username
        self.user = self.gl.users.list(username=self.username)[0]
        
    def get_action_nums(self, since):
        events = self.gl.user_activities(self.user.get_id(), since=since)
        
        output = dict()
        
        for event in events:
            action = event[ACTION_KEY] if ACTION_KEY in event else None
            target = event[TARGET_TYPE] if TARGET_TYPE in event else None
            
            key = f"{action}:{target}"
            
            if key not in output:
                key[output] = 0
            key[output] += 1
        return output