import os, pickle, csv

from git_stats.history import History, build_from_path
from git_stats.commit import CSVCommit

class Cache(object):

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def fetch_history(self):
        cache_path = self._csv_path()

        if os.path.isfile(cache_path):
            return self._load_cached_history()
        else:
            history = build_from_path(self.repo_path)
            self._store_history(history)
            return history

    def _load_cached_history(self):
        with open(self._csv_path()) as csv_file:
            reader = csv.DictReader(csv_file)

            commits = [CSVCommit(row["SHA"], row["Timestamp"], row["File Delta"],
                row["Code Delta"], row["Author"])
                for row in reader]

            return History(commits)

    def _store_history(self, history):
        with open(self._csv_path(), "w+") as csv_file:
            writer = csv.DictWriter(csv_file,
                    ["SHA", "Timestamp", "Author", "File Delta", "Code Delta"])
            writer.writeheader()
            for commit in history.commits:
                writer.writerow({"SHA": commit.commit.hexsha,
                    "Timestamp": commit.commit.committed_date,
                    "Author": commit.commit.author,
                    "File Delta": commit.file_change(),
                    "Code Delta": commit.code_change()})

    def _csv_path(self):
        cwd = os.getcwd()
        base_path = os.path.basename(self.repo_path)
        return cwd + base_path + "_cache.csv"
