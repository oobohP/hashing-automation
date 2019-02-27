import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

# TODO:
# create a way to generalize and strip out uneeded data and write this to another file
# python cannot do the same things sed does but can simulate it. otherwise the option below will be used

set_threshold = 30


def read_csv_to_dataframe():
    # Reads CSV Fle and creates a dataframe with 3 columns
    # graphical heatmap    18x182.txt for body match returns dataset in pandas and threshold
    pd.set_option('max_colwidth', 800)

    dataframe = pd.read_csv('18x18body.txt', usecols=[0, 1, 2],
                            names=['emlgroup1', 'emlgroup2', 'scores'])
    return dataframe


def get_heatmaps(dataframe):
    # creates numerical heatmap
    numerical_heatmap = pd.pivot_table(dataframe, index='emlgroup1',
                                       columns='emlgroup2', values='scores')
    color_heatmap = sns.heatmap(numerical_heatmap)
    print numerical_heatmap
    return plt.show(color_heatmap)


def form_clusters(dataframe, set_threshold):
    # creates a new dataframe where there are no duplicates
    # and the data correlates to the threshold
    cluster_threshold = dataframe.loc[(dataframe['emlgroup1'] !=
                                      dataframe['emlgroup2']) &
                                      (dataframe['scores'] > set_threshold)]

    # generates clusters created from the dataframe cluster_under_threshold
    G = nx.from_pandas_edgelist(cluster_threshold,
                                'emlgroup1', 'emlgroup2')
    series_of_clusters = list(nx.connected_components(G))
    clusters = pd.Series(series_of_clusters).to_frame('Clusters')
    return clusters


if __name__ == "__main__":
    print form_clusters(read_csv_to_dataframe(), set_threshold)
    #get_heatmaps(read_csv_to_dataframe())
