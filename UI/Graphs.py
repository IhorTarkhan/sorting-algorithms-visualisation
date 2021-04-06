import matplotlib.pyplot as plt
# from exper import a
import numpy as np


class Graphs:
    def __init__(self):
        self.labels = [
            'Brick',
            'Bubble',
            'Cocktail',
            'Marge',
            'Quick',
            'Radix'
        ]
        self.main_label = 'Algorythms'

    def draw_hist(self, y, color, label):
        pos = np.arange(len(self.labels))
        width = 0.8
        # gives histogram aspect to the bar diagram
        ax = plt.axes()
        ax.set_xticks(pos)
        ax.set_xticklabels(self.labels)

        plt.bar(pos, y, width, color=color)
        plt.xlabel(self.main_label)
        plt.ylabel(label)
        plt.show()

    def one_sample_graph(self, sorting_results):
        times = [x.time_usage for x in sorting_results]
        memory = [x.size_usage for x in sorting_results]
        self.draw_hist(times, 'b', 'Time spent')
        self.draw_hist(memory, 'g', 'Memory usage')

    def different_size_comparison_time(self):
        pass

    def different_size_comparison_memory(self):
        pass

    def different_size_comparison(self):
        self.different_size_comparison_time()
        self.different_size_comparison_memory()

# b = Graphs()
# b.one_sample_graph(a)
