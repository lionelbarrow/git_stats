from datetime import datetime

def unpair_authors(authors):
    return set(str(self.commit.author).split(" ")) - set(["and"])

class Commit(object):

    def __init__(self, commit, diffindex):
        self.commit = commit
        self.diffindex = diffindex

    def __repr__(self):
        return self.commit.hexsha

    def authors(self):
        return unpair_authors(self.commit.author)

    def file_change(self):
        new_files = filter(lambda d: d.a_mode == 0, self.diffindex)
        deleted_files = filter(lambda d: d.b_mode == 0, self.diffindex)
        return len(new_files) - len(deleted_files)

    def code_change(self):
        stats = self.commit.stats.total
        return stats["insertions"] - stats["deletions"]

    def date(self):
        return datetime.utcfromtimestamp(self.commit.committed_date)

class CSVCommit(object):

    def __init__(self, sha, timestamp, file_change, code_change, author):
        self.sha = sha
        self.timestamp = timestamp
        self.file_change = file_change
        self.code_change = code_change
        self.author = author

    def __repr__(self):
        return self.sha

    def authors(self):
        return unpair_authors(self.author)

    def file_change(self):
        return self.file_change

    def code_change(self):
        return self.code_change

    def date(self):
        return datetime.utcfromtimestamp(self.timestamp)
