from git import Repo

from git_stats.commit import Commit

def build_from_path(path):
    commits = []

    first = True
    previous_commit = None
    diffindex = []

    for commit in reversed(list(repo.iter_commits())):
        if first:
            first = False
            previous_commit = commit
        else:
            diffindex = previous_commit.diff(commit)
            previous_commit = commit
        commits.append(Commit(commit, diffindex))

    return History(commits)

class History(object):

    def __init__(self, commits):
        self.commits = commits

    def dates(self):
        return [commit.date() for commit in self.commits]

    def file_changes(self):
        return [commit.file_change() for commit in self.commits]

    def code_changes(self):
        pass

    def authors(self):
        pass
