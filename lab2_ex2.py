import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
import matplotlib.pyplot as plt
import numpy as np

### CITE NETWORKX AND NDLIB !!!!!
def give_mean(data):
    return np.mean(list(data.values()))

def give_properties(G):
    # Model properties
    clustering_coefficient = give_mean(nx.clustering(G, nodes=None, weight=None))
    closeness_centrality = give_mean(nx.closeness_centrality(G, u=None, distance=None, wf_improved=True))
    betweenness_centrality = give_mean(nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None))
    degree_centrality = give_mean(nx.degree_centrality(G))
    average_shortest_path_length = nx.average_shortest_path_length(G, weight=None, method=None)

    properties = np.matrix([clustering_coefficient, closeness_centrality, betweenness_centrality, degree_centrality, average_shortest_path_length])

    return(properties)

def evaluate(beta, gamma, mu, I, n_iterations, G, export_name="untitled.pdf", vis=False):
    # Model selection
    model = ep.SIRModel(G)

    # Model Configuration
    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', beta)
    cfg.add_model_parameter('gamma', gamma)
    cfg.add_model_parameter('mu', mu)
    cfg.add_model_parameter("fraction_infected", I)
    model.set_initial_status(cfg)

    # Simulation execution
    iterations = model.iteration_bunch(n_iterations)
    trends = model.build_trends(iterations)
    print(trends)

    # Visualization
    if vis == True:
        viz = DiffusionTrend(model, trends)
        viz.plot(export_name)




n = 100
p = 0.1
k = int(n * p)
m = int(n * p)

beta, gamma, mu, I = 1, 1/3, 1/60, 0.1
n_iterations = 50

er = nx.erdos_renyi_graph(n, p, seed=None)   
ws = nx.watts_strogatz_graph(n, k, p, seed=None)
ba = nx.barabasi_albert_graph(n, m, seed=None, initial_graph=None)

evaluate(beta, gamma, mu, I, n_iterations, er, export_name="untitled.pdf", vis=True)

runs=5
properties_er = np.zeros((5,runs))
for i in range(0, runs):
    seed=int(i)
    er = nx.erdos_renyi_graph(n, p, seed)   
    properties_er[:,i] = give_properties(er)

print(properties_er)