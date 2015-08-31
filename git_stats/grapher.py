import matplotlib.pyplot as plt

class Grapher(object):

    def __init__(self, history):
        self.history = history

    def files_over_time(self):
        file_changes = self.history.file_changes()
        dates = self.history.dates()

        cumulative_files = 0
        file_counts = []
        for delta in file_changes:
            cumulative_files += delta
            file_counts.append(cumulative_files)

        plt.plot(dates, file_counts, color="r", label="Files in the codebase")
        plt.legend()
        plt.show()
