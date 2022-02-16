from jnpr.healthbot.swagger.models.datastore_schema import DatastoreSchema
from jnpr.healthbot.swagger.models.panel_schema import PanelSchema
from jnpr.healthbot.swagger.models.panel_data_schema import PanelDataSchema
from jnpr.healthbot.swagger.models.hb_graphs import HbGraphs
from jnpr.healthbot.swagger.models.hb_graphs_query import HbGraphsQuery
from jnpr.healthbot.swagger.models.panel_data_schema_add_group_by_tag \
    import PanelDataSchemaAddGroupByTag
from jnpr.healthbot.swagger.models.panel_data_schema_add_where_condition \
    import PanelDataSchemaAddWhereCondition
from jnpr.healthbot.swagger.models.panel_data_schema_add_where_condition_key_or_field \
    import PanelDataSchemaAddWhereConditionKeyOrField
from jnpr.healthbot.swagger.models.panel_data_schema_add_where_condition_key_or_field_value \
    import PanelDataSchemaAddWhereConditionKeyOrFieldValue
from jnpr.healthbot.swagger.models.panel_data_schema_add_where_condition_operator \
    import PanelDataSchemaAddWhereConditionOperator
from jnpr.healthbot.swagger.models.panel_data_schema_group_by_fill \
    import PanelDataSchemaGroupByFill
from jnpr.healthbot.swagger.models.panel_data_schema_group_by_time \
    import PanelDataSchemaGroupByTime
from jnpr.healthbot.swagger.models.panel_data_schema_selected_aggregation \
    import PanelDataSchemaSelectedAggregation
from jnpr.healthbot.swagger.models.panel_data_schema_selected_field \
    import PanelDataSchemaSelectedField
from jnpr.healthbot.swagger.models.panel_data_schema_selected_group \
    import PanelDataSchemaSelectedGroup
from jnpr.healthbot.swagger.models.panel_data_schema_selected_topic \
    import PanelDataSchemaSelectedTopic
from jnpr.healthbot.swagger.models.panel_data_schema_selected_transformation \
    import PanelDataSchemaSelectedTransformation
from jnpr.healthbot.swagger.models.panel_data_schema_selected_device \
    import PanelDataSchemaSelectedDevice
from jnpr.healthbot.swagger.models.panel_schema_panel_type \
    import PanelSchemaPanelType
from jnpr.healthbot.swagger.models.panel_schema_time_range import PanelSchemaTimeRange
from jnpr.healthbot.swagger.models.panel_schema_unit_type import PanelSchemaUnitType
from jnpr.healthbot.exception import NotFoundError
from jnpr.healthbot.modules import BaseModule
from uuid import uuid4
import logging

logger = logging.getLogger(__file__)


class HBCharts(BaseModule):

    def __init__(self, hbot):
        """
        :param object hbot: :class:`jnpr.healthbot.HealthBotClient` client instance
        """
        super().__init__(hbot)

    def get_add_canvas_schema(self, canvas_name, graphs):
        # TODO Add comments

        def _get_database_name(group_name, group_type="device", device_name=None):
            if group_type == "network":
                return 'hb-{tenant_name}:__network:{group_name}'\
                    .format(tenant_name=self.hbot.tenant, group_name=group_name)
            else:
                return 'hb-{tenant_name}:{group_name}:{device_name}'\
                    .format(tenant_name=self.hbot.tenant, group_name=group_name,
                            device_name=device_name)

        def _get_panel_uid():
            return str(uuid4().hex)[0:20]

        def _get_panel_query(panel_data_list):
            queries = []
            for panel in panel_data_list:
                logical_operator = panel.selected_logical_operator
                time = panel.group_by_time.value
                fill = panel.group_by_fill.value
                key = panel.add_group_by_tag
                time_filter = "$timeFilter"
                db_name = _get_database_name(group_type=panel.group_type,
                                             group_name=panel.selected_group.value,
                                             device_name=panel.selected_device.value)
                retention_policy = panel.selected_topic.retention_policy

                # Select expression
                select_expr = '"{panel_selected_field_value}"'\
                    .format(panel_selected_field_value=panel.selected_field.value)
                if panel.selected_aggregation.value is not None:
                    select_expr = panel.selected_aggregation.value + \
                                  "({select_expr})".format(select_expr=select_expr)
                if panel.selected_transformation != "":
                    select_expr = panel.selected_transformation.value + \
                                  "({select_expr})".format(select_expr=select_expr)

                # From expression
                from_expr = '\"{db_name}"."{retention_policy}"."{panel_selected_topic_value}"'\
                    .format(db_name=db_name, retention_policy=retention_policy,
                            panel_selected_topic_value=panel.selected_topic.value)

                # Where expression
                where_expr = ''
                where_count = len(panel.add_where_condition)
                for count in range(0, where_count):
                    key_or_field = panel.add_where_condition[count].key_or_field
                    operator = panel.add_where_condition[count].operator
                    key_or_field_value = panel.add_where_condition[count].key_or_field_value
                    opr_value = operator.value
                    logic_operator = ""
                    if count != (where_count - 1):
                        logic_operator = logical_operator[count - 0]
                    if (opr_value == "=~") or (opr_value == "!~"):
                        where_expr = '{where_expr} {logic_operator}'.format(where_expr=where_expr,
                                                                            logic_operator=logic_operator)
                        where_expr = '{where_expr} "{key_or_field_value}" {opr_value} /{key_or_field_value.value} / '\
                            .format(where_expr=where_expr, key_or_field_value=key_or_field.value,
                                    opr_value=opr_value, key_or_field_value_value=key_or_field_value.value)
                    elif key_or_field.data_type == "number":
                        where_expr = '{where_expr} {logic_operator}'.format(where_expr=where_expr,
                                                                            logic_operator=logic_operator)
                        where_expr = '{where_expr} "{key_or_field_value}" {opr_value} {key_or_field_value_value}'\
                            .format(where_expr=where_expr, key_or_field_value=key_or_field.value, opr_value=opr_value,
                                    key_or_field_value_value=key_or_field_value.value)
                    else:
                        where_expr = '{where_expr} {logic_operator}'.format(where_expr=where_expr,
                                                                            logic_operator=logic_operator)
                        where_expr = '''{where_expr} "{key_or_field_value}" {opr_value} '{key_or_field_value_value}' '''\
                            .format(where_expr=where_expr, key_or_field_value=key_or_field.value,
                                    opr_value=opr_value, key_or_field_value_value=key_or_field_value.value)

                    if where_expr != "":
                        where_expr = '{time_filter} AND ({where_expr})'\
                            .format(time_filter=time_filter, where_expr=where_expr.rstrip().lstrip())
                    else:
                        where_expr = '{time_filter}'.format(time_filter=time_filter)

                # Group by Expression
                group_by_expr = 'time({time}) fill({fill})'.format(time=time, fill=fill)
                if len(key) > 0:
                    group_by_expr = ""
                    for k in key:
                        group_by_expr = group_by_expr + ', "{k_value}"'.format(k_value=k.value)
                    group_by_expr = 'time({time}) {group_by_expr} fill({fill})'\
                        .format(time=time, group_by_expr=group_by_expr, fill=fill)

                query_string = "SELECT {select_expr} FROM {from_expr} WHERE {where_expr} GROUP BY {group_by_expr}"\
                    .format(select_expr=select_expr, from_expr=from_expr,
                            where_expr=where_expr, group_by_expr=group_by_expr)
                queries.append(query_string)

            return queries

        def _get_panel_data(graph):
            group_by_fill_mapping = {
                "fill(null)": 'null',
                "none": 'none'
            }
            panel_data_list = []
            for query in graph.query:
                add_group_by_tag = []
                group_by_keys = query.group_by_tag_key
                for key in group_by_keys:
                    add_group_by_tag.append(
                        PanelDataSchemaAddGroupByTag(data_type='string', label=key, type="key", value=key))

                add_where_condition = []
                selected_logical_operator = []
                for condition in query.where:
                    # Validate if key or field and exists
                    if condition.get('key') in query.key_dict.keys():
                        type = 'key'
                        datatype = 'string'
                        label = condition.get('key')
                        value = condition.get('value')
                        # Validate value of tags #TODO
                    else:
                        field_exists = False
                        for field in query.field_list:
                            if field['name'] == condition.get('key'):
                                current_field = field
                                field_exists = True
                                break
                        if not field_exists:
                            raise ValueError("The field {0} does not exists for the measurement "
                                             "{1}, please configure valid measurement"
                                             .format(query.field_name, query.measurement_name))
                        type = 'field'
                        datatype = current_field['type']
                        label = condition.get('key')
                        value = condition.get('value')

                    add_where_condition.append(PanelDataSchemaAddWhereCondition(
                        key_or_field=PanelDataSchemaAddWhereConditionKeyOrField(data_type=datatype, label=label,
                                                                                type=type, value=label),
                        key_or_field_value=PanelDataSchemaAddWhereConditionKeyOrFieldValue(label=value, value=value),
                        operator=PanelDataSchemaAddWhereConditionOperator(label=condition.get("operator"),
                                                                          value=condition.get("operator"))
                    ))
                    logical_operator = condition.get('logical_operation', None)
                    if logical_operator is not None:
                        selected_logical_operator.append(logical_operator)

                transformation = ""
                if query.transformation is not None:
                    transformation = PanelDataSchemaSelectedTransformation(label=query.transformation,
                                                                           value=query.transformation)

                panel_data = PanelDataSchema(
                    add_group_by_tag=add_group_by_tag,
                    add_where_condition=add_where_condition,
                    change_where_key_field=[],
                    group_by_fill=PanelDataSchemaGroupByFill(label=query.group_by_fill,
                                                             value=group_by_fill_mapping[query.group_by_fill]),
                    group_by_time=PanelDataSchemaGroupByTime(label=query.group_by_interval,
                                                             value=query.group_by_interval),
                    group_type=query.group_type,
                    selected_aggregation=PanelDataSchemaSelectedAggregation(label=str(query.field_aggregation) + "()",
                                                                            value=query.field_aggregation),
                    selected_device=PanelDataSchemaSelectedDevice(label=query.device_name, value=query.device_name),
                    selected_dropdown=[],
                    selected_field=PanelDataSchemaSelectedField(label=query.field_name, value=query.field_name),
                    selected_group=PanelDataSchemaSelectedGroup(label=query.group_name, type=query.group_type,
                                                                value=query.group_name),
                    selected_logical_operator=selected_logical_operator,
                    selected_topic=PanelDataSchemaSelectedTopic(label=query.measurement_name,
                                                                retention_policy=query.retention_policy,
                                                                type=query.measurement_type,
                                                                value=query.measurement_name),
                    selected_transformation=transformation
                )
                panel_data_list.append(panel_data)
            return panel_data_list

        def _get_snake_case(string):
            temp = string.split('_')
            return temp[0] + ''.join(ele.title() for ele in temp[1:])

        def _get_json(json_data):
            keys = list(json_data.keys())
            for key in keys:
                if isinstance(json_data[key], dict):
                    json_data[key] = _get_json(json_data[key])
                elif isinstance(json_data[key], list):
                    for i in range(0, len(json_data[key])):
                        if isinstance(json_data[key][i], dict):
                            json_data[key][i] = _get_json(json_data[key][i])
                json_data[_get_snake_case(key)] = json_data.pop(key)

            return json_data

        def _validate_data(canvas_name, graphs):
            """
            Validating if the following compulsory fields are passed by user:
            Compulsory fields: canvas_name, graph_name, graph_type, time_range,
            group_name, device_name, measurement_name, field_name

            If the required arguments are not passed return False with the error message
            """
            # Sample submission link
            sample_submission = " For more details, please refer the sample submission here {link}"\
                .format(link="")
            if (canvas_name is None) or (canvas_name == ""):
                return False, "Please enter a valid canvas name."

            for graph in graphs:
                if (graph.graph_name is None) or (graph.graph_name == ""):
                    return False, "Please enter a valid graph name"

                if not isinstance(graph, HbGraphs):
                    return False, "Graphs is not of type HbGraphs Schema." + sample_submission

                if graph.time_range is None:
                    return False, " `time_range` parameter missing in HbGraphs object." + sample_submission
                if graph.graph_type is None:
                    return False, " `graph_type` parameter missing in HbGraphs object." + sample_submission

                if (graph.query is None) or (graph.query is []):
                    return False, "`query` parameter missing in HbGraphs object." + sample_submission

                for query in graph.query:
                    if not isinstance(query, HbGraphsQuery):
                        return False, "Query value(s) are not of type HbGraphsQuery Schema." + sample_submission

                    if query.group_name is None:
                        return False, " `group_name` parameter missing in HbGraphs object." + sample_submission

                    if query.measurement_name is None:
                        return False, " `measurement_name` parameter missing in HbGraphs object." + sample_submission
                    if query.field_name is None:
                        return False, " `field_name` parameter missing in HbGraphs object." + sample_submission
                    if query.where is not None:
                        if not isinstance(query.where, list):
                            return False, "Query's where parameters value(s) must be a list." + sample_submission

                        for where_condition in query.where:
                            keys = ["key", "value", "operator"]
                            for key in keys:
                                if key not in where_condition.keys():
                                    return False, 'Invalid input for where condition. Sample: where=' \
                                                  '[{"key":"abc","operator":"==","value":"gbha", ' \
                                                  '"logical_operation":"and"}.' + sample_submission

                            valid_operators = ["=", "!=", "=~", "!="]
                            if where_condition['operator'] not in valid_operators:
                                return False, 'Invalid operator value for in where parameter of Query, ' \
                                              'valid operators: "=", "!=", "=~", "!=" .' + sample_submission
                        if len(query.where) > 1:
                            for where_condition in query.where[:-1]:
                                if 'logical_operation' not in where_condition.keys():
                                    return False, 'Invalid input for where condition. Sample: where=' \
                                                  '[{"key":"abc","operator":"==","value":"gbha", ' \
                                                  '"logical_operation":"and"}.' + sample_submission
                                valid_logical_operation_keys = ['AND', 'OR']
                                if where_condition['logical_operation'] not in valid_logical_operation_keys:
                                    return False, 'Invalid logical_operation value for in where parameter ' \
                                                  'of Query, valid operators: "AND", "OR" .' + sample_submission

            return True, "Validation successful!"

        def _get_response(url):
            response = self.api.get(url)

            if response.status_code == 404:
                return []

            response_json = response.json()
            if response.status_code != 200:
                logger.error(response.text)
                raise NotFoundError(response_json)
            return response_json

        def _set_default_values(graphs):
            dg_list = _get_response(self.hbot.urlfor.device_group_list())
            ng_list = _get_response(self.hbot.urlfor.network_group_list())
            for graph in graphs:
                for query in graph.query:
                    if query.where is None:
                        query.where = []
                    query.field_list = []
                    query.key_dict = {}
                    if query.group_type is None:
                        if query.group_name in dg_list:
                            query.group_type = "device"
                        elif query.group_name in ng_list:
                            query.group_type = "network"
                        else:
                            raise ValueError("The group : {} does not exist, please configure a "
                                             "valid device/network group".format(query.group_name))

                    if query.group_type == "device":
                        if query.group_name not in dg_list:
                            raise ValueError("The device group : {} does not exist".format(query.group_name))

                        if query.device_name is None:
                            raise ValueError("No device configured for graph {}"
                                             .format(graph.graph_name))
                        else:
                            device_list = _get_response(self.hbot.urlfor.device())
                            if query.device_name not in device_list:
                                raise ValueError("Device {} does not exist, please configure "
                                                 "valid device".format(query.device_name))
                            measurements_details = _get_response(self.hbot.urlfor.dg_measurements_list
                                                                 (device_id=query.device_name,
                                                                  device_group=query.group_name))
                            measurement_exists = False
                            for measurement in measurements_details:
                                if measurement['name'] == query.measurement_name:
                                    current_measurement = measurement
                                    measurement_exists = True
                                    break
                            if not measurement_exists:
                                raise ValueError("The measurement {0} not present for the device group {1} and "
                                                 "device {2}, please configure a valid measurement".format
                                                 (query.measurement_name, query.group_name, query.device_name))
                            query.measurement_type = current_measurement['type']
                            query.retention_policy = current_measurement['retention_policy']
                            fields_list = _get_response(self.hbot.urlfor.dg_measurement_fields(
                                device_id=query.device_name, device_group=query.group_name,
                                table_name=query.measurement_name))
                            query.field_list = fields_list
                            field_exists = False
                            for field in fields_list:
                                if field['name'] == query.field_name:
                                    current_field = field
                                    field_exists = True
                                    break
                            if not field_exists:
                                raise ValueError("The field {0} does not exists for the measurement "
                                                 "{1}, please configure valid measurement"
                                                 .format(query.field_name, query.measurement_name))
                            query.field_type = current_field['type']

                            tags_dict = _get_response(self.hbot.urlfor.dg_measurement_tags(
                                device_id=query.device_name, device_group=query.group_name,
                                table_name=query.measurement_name))
                            query.key_dict = tags_dict

                    elif query.group_type == "network":
                        if query.group_name not in ng_list:
                            raise ValueError("The network group : {} does not exist".format(query.group_name))
                        measurements_details = _get_response(self.hbot.urlfor.ng_measurements_list
                                                             (network_group=query.group_name))
                        measurement_exists = False
                        for measurement in measurements_details:
                            if measurement['name'] == query.measurement_name:
                                current_measurement = measurement
                                measurement_exists = True
                                break
                        if not measurement_exists:
                            raise ValueError("The measurement {0} not present for the network group {1} "
                                             ", please configure a valid measurement".format
                                             (query.measurement_name, query.group_name))
                        query.measurement_type = current_measurement['type']
                        query.retention_policy = current_measurement['retention_policy']
                        fields_list = _get_response(self.hbot.urlfor.ng_measurement_fields(
                            network_group=query.group_name, table_name=query.measurement_name))
                        query.fields_list = query.fields_list + fields_list
                        field_exists = False
                        for field in fields_list:
                            if field['name'] == query.field_name:
                                current_field = field
                                field_exists = True
                                break
                        if not field_exists:
                            raise ValueError("The field {0} does not exists for the measurement "
                                             "{1}, please configure valid measurement"
                                             .format(query.field_name, query.measurement_name))
                        query.field_type = current_field['type']

                        tags_dict = _get_response(self.hbot.urlfor.dg_measurement_tags(
                            device_id=query.device_name, device_group=query.group_name,
                            table_name=query.measurement_name))
                        query.key_dict = tags_dict

                    if query.group_by_tag_key is  None:
                        query.group_by_tag_key = []
                    else:
                        if not isinstance(query.group_by_tag_key, list):
                            raise ValueError("group_by_tag_key is not a list, please configure a list")

                    # validate tag #TODO
                    if query.group_by_interval is None:
                        query.group_by_interval = "$__interval"
                    if query.group_by_fill is None:
                        query.group_by_fill = "fill(null)"
                    if query.field_aggregation is None:
                        query.field_aggregation = "mean"

            return graphs

        if not isinstance(graphs, list):
            graphs = [graphs]

        ret_val, msg = _validate_data(canvas_name, graphs)
        if not ret_val:
            raise ValueError(msg)

        graphs = _set_default_values(graphs)

        panel_list = []
        graph_type_mapping = {
            "Time Series": "timeseries",
            "Heatmap": "heatmap",
            "Histogram": "histogram"
        }
        unit_value_mapping = {
            "Short": "short",
            "Percentage(0-100)": "percentage",
            "Bits": "bits",
            "Bytes": "bytes",
            "Kilobytes": "kilobytes",
            "Megabytes": "megabytes",
            "Gigabytes": "gigabytes",
            "Parts per million(ppm)": "ppm",
            "Parts per billion(ppb)": "ppb"
        }

        panel_data_list = []
        for graph in graphs:
            panel_data = _get_panel_data(graph)
            panel_data_list = panel_data_list + panel_data
            db = _get_database_name(group_name=graph.query[0].group_name, group_type=graph.query[0].group_type,
                                    device_name=graph.query[0].device_name)
            decimals = graph.decimals
            panel_data = panel_data_list
            panel_name = graph.graph_name
            panel_query = _get_panel_query(panel_data_list)
            panel_type = PanelSchemaPanelType(label=graph.graph_type, value=graph_type_mapping[graph.graph_type])
            panel_uid = _get_panel_uid()
            time_range = PanelSchemaTimeRange(label=graph.time_range, value=graph.time_range)
            unit_type = ""
            if graph.unit_type is not None:
                unit_type = PanelSchemaUnitType(label=graph.unit_type, value=unit_value_mapping[graph.unit_type])

            panels = PanelSchema(db=db, decimals=decimals, panel_data=panel_data, panel_name=panel_name,
                                 panel_query=panel_query, panel_type=panel_type, panel_uid=panel_uid,
                                 time_range=time_range, unit_type=unit_type, y_label=graph.y_label,
                                 y_max=graph.y_max, y_min=graph.y_min)
            panels_value = _get_json(panels.to_dict())
            panel_list.append(panels_value)

        value = {
            "createdAt": "2021-10-11T09:10:30",
            "description": "",
            "name": canvas_name,
            "panels": panel_list,
            "updatedAt": "2021-10-26T04:49:56"
        }
        schema = DatastoreSchema(group_name='grafana', key=canvas_name, value=value)
        return schema

    def get_canvas(self, canvas_name: str = None):
        if canvas_name is not None:
            hb_chart_url = self.hbot.urlfor.data_store_schema(canvas_name)
            # if uncommitted:
            #     hb_chart_url += self.hbot.apiopt_candidate
            response = self.api.get(hb_chart_url)
            if response.status_code != 200:
                logger.error(response.text)
            response.raise_for_status()
            if response.status_code == 404:
                return None
            return response.text
        else:
            print("Please specify the canvas name")

    def add_canvas(self, canvas_name, graphs):
        schema = self.get_add_canvas_schema(canvas_name, graphs)
        payload = self.hbot._create_payload(schema)
        hb_chart_url = self.hbot.urlfor.data_store_schema(canvas_name)
        response = self.api.post(hb_chart_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def update_canvas(self, canvas_name, graphs):
        schema = self.get_add_canvas_schema(canvas_name, graphs)
        payload = self.hbot._create_payload(schema)
        hb_chart_url = self.hbot.urlfor.data_store_schema(canvas_name)
        response = self.api.put(hb_chart_url, json=payload)
        if response.status_code != 200:
            logger.error(response.text)
        response.raise_for_status()
        return True

    def delete_canvas(self, canvas_name: str = None):
        hb_chart_url = self.hbot.urlfor.data_store_schema(canvas_name)
        response = self.api.delete(hb_chart_url)
        if response.status_code != 204:
            logger.error(response.text)
        response.raise_for_status()

        return True

