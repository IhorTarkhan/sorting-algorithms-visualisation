import matplotlib.pyplot as plt
# from exper import a
import numpy as np

from entity.SortAlgorithmEnum import SortAlgorithmEnum


class Graphs:
    def __init__(self):
        self.labels = [
            'Brick',
            'Bubble',
            'Cocktail',
            'Merge',
            'Quick',
            'Insertion'
        ]
        self.main_label = 'Algorythms'

        self.colors = [
            'bo', 'go', 'ro', 'yo', 'co', 'ko'
        ]

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
        self.draw_hist(times, 'b', 'Time spent(ms)')
        self.draw_hist(memory, 'g', 'Memory usage(CU)')

    def draw_a_line(self, x, y, y_label):
        plt.plot(x, y, y_label)

    def split_by_algorythms(self, statistic, index):
        def get_proper_field(object, index):
            if index == 0:
                return object.ascending_time
            if index == 1:
                return object.random_time
            if index == 2:
                return object.descending_time
            if index == 3:
                return object.ascending_size
            if index == 4:
                return object.random_size
            else:
                return object.descending_size

        res = []
        for alg in range(len(self.labels)):
            res.append([])
        for item in statistic:
            if item.algorithm == SortAlgorithmEnum.BRICK:
                res[0].append((get_proper_field(item, index), item.array_size))
            elif item.algorithm == SortAlgorithmEnum.BUBBLE:
                res[1].append((get_proper_field(item, index), item.array_size))
            elif item.algorithm == SortAlgorithmEnum.COCKTAIL:
                res[2].append((get_proper_field(item, index), item.array_size))
            elif item.algorithm == SortAlgorithmEnum.MERGE:
                res[3].append((get_proper_field(item, index), item.array_size))
            elif item.algorithm == SortAlgorithmEnum.QUICK:
                res[4].append((get_proper_field(item, index), item.array_size))
            else:
                res[5].append((get_proper_field(item, index), item.array_size))
        return res

    def split_by_fields(self, statistic):
        asc_t = []
        rand_t = []
        desc_t = []
        asc_m = []
        rand_m = []
        desc_m = []
        for item in statistic:
            if item.ascending_time != None:
                asc_t.append(item)
            if item.random_time != None:
                rand_t.append(item)
            if item.descending_time != None:
                desc_t.append(item)
            if item.ascending_size != None:
                asc_m.append(item)
            if item.random_size != None:
                rand_m.append(item)
            if item.descending_size != None:
                desc_m.append(item)

        return asc_t, rand_t, desc_t, asc_m, rand_m, desc_m

    def get_xy_array(self, array):
        x = []
        y = []
        for item in array:
            y.append(item[0])
            x.append(item[1])
        return x, y

    def different_algorythms_comparison(self, statistic_sorting_result):
        graphs = [self.split_by_fields(statistic_sorting_result)]
        for graph_index in range(len(graphs)):
            graphs_separated = self.split_by_algorythms(graphs[graph_index])
            for alg_index in range(len(graphs_separated)):
                x, y = self.get_xy_array(graphs_separated[alg_index])
                self.draw_a_line(x, y, self.colors[alg_index])
            plt.show()

# b = Graphs()
# b.one_sample_graph(a)
