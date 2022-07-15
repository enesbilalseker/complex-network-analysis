"""
SIR modeli
"""
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
from bokeh.io import output_notebook, show
import ndlib.models.epidemics as ep
import networkx as nx
import ndlib.models.ModelConfig as mc

g = nx.erdos_renyi_graph(1000, 0.1)
model = ep.SIRModel(g)

config = mc.Configuration()
config.add_model_parameter('beta', 0.001)
config.add_model_parameter('gamma', 0.01)
config.add_model_parameter("fraction_infected", 0.05)
model.set_initial_status(config)

iterations = model.iteration_bunch(555)
trends = model.build_trends(iterations)


viz = DiffusionTrend(model, trends)
p = viz.plot(width=666, height=666)
show(p)
