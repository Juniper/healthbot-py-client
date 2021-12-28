from pprint import pprint
from jnpr.healthbot.swagger.models.pin_graphs_query import PinGraphsQuery
from jnpr.healthbot.swagger.models.pin_graphs import PinGraphs

from jnpr.healthbot import HealthBotClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'


with HealthBotClient(ip, gui_username, gui_password, port=8080) as hb:
    # Adding a new canvas with a single graph
    q1 = PinGraphsQuery(group_name='dg-junos', device_name="d2", measurement_name="system.commit/commit-history",
                        transformation=None, field_name="l1-threshold", field_aggregation="mean",
                        where=[{'key': "comment", "operator": '=', "value": "abcd"}],
                        group_by_interval="1s", group_by_fill="fill(null)", group_by_tag_key=[])
    g1 = PinGraphs(graph_name="graph1", graph_description=None, graph_type="Heatmap",
                   time_range='3h', query=[q1], y_label=None, y_max=None,
                   y_min=None, unit_type=None, decimals=None)
    hb.charts.add_canvas(canvas_name="mycanvas1", graphs=g1)
    hb.commit()
    # pprint(hb.charts.get_canvas("mycanvas1"))

