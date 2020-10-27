# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection(object):
    """
    Collection of resource capacity trend.
    """

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
    #: This constant has a value of "CPU"
    RESOURCE_METRIC_CPU = "CPU"

    #: A constant which can be used with the resource_metric property of a SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
    #: This constant has a value of "STORAGE"
    RESOURCE_METRIC_STORAGE = "STORAGE"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
    #: This constant has a value of "CORES"
    USAGE_UNIT_CORES = "CORES"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
    #: This constant has a value of "GB"
    USAGE_UNIT_GB = "GB"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
    #: This constant has a value of "MBPS"
    USAGE_UNIT_MBPS = "MBPS"

    #: A constant which can be used with the usage_unit property of a SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
    #: This constant has a value of "PERCENT"
    USAGE_UNIT_PERCENT = "PERCENT"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type time_interval_end: datetime

        :param resource_metric:
            The value to assign to the resource_metric property of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
            Allowed values for this property are: "CPU", "STORAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_metric: str

        :param usage_unit:
            The value to assign to the usage_unit property of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
            Allowed values for this property are: "CORES", "GB", "MBPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type usage_unit: str

        :param item_duration_in_ms:
            The value to assign to the item_duration_in_ms property of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type item_duration_in_ms: int

        :param capacity_data:
            The value to assign to the capacity_data property of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type capacity_data: list[ResourceCapacityTrendAggregation]

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'resource_metric': 'str',
            'usage_unit': 'str',
            'item_duration_in_ms': 'int',
            'capacity_data': 'list[ResourceCapacityTrendAggregation]'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'resource_metric': 'resourceMetric',
            'usage_unit': 'usageUnit',
            'item_duration_in_ms': 'itemDurationInMs',
            'capacity_data': 'capacityData'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._resource_metric = None
        self._usage_unit = None
        self._item_duration_in_ms = None
        self._capacity_data = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def resource_metric(self):
        """
        **[Required]** Gets the resource_metric of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        Defines the type of resource metric (CPU, STORAGE)

        Allowed values for this property are: "CPU", "STORAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_metric of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :rtype: str
        """
        return self._resource_metric

    @resource_metric.setter
    def resource_metric(self, resource_metric):
        """
        Sets the resource_metric of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        Defines the type of resource metric (CPU, STORAGE)


        :param resource_metric: The resource_metric of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type: str
        """
        allowed_values = ["CPU", "STORAGE"]
        if not value_allowed_none_or_none_sentinel(resource_metric, allowed_values):
            resource_metric = 'UNKNOWN_ENUM_VALUE'
        self._resource_metric = resource_metric

    @property
    def usage_unit(self):
        """
        **[Required]** Gets the usage_unit of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        Identifies the units of the current resource metric (CORES, GB).

        Allowed values for this property are: "CORES", "GB", "MBPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The usage_unit of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :rtype: str
        """
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        """
        Sets the usage_unit of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        Identifies the units of the current resource metric (CORES, GB).


        :param usage_unit: The usage_unit of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type: str
        """
        allowed_values = ["CORES", "GB", "MBPS", "PERCENT"]
        if not value_allowed_none_or_none_sentinel(usage_unit, allowed_values):
            usage_unit = 'UNKNOWN_ENUM_VALUE'
        self._usage_unit = usage_unit

    @property
    def item_duration_in_ms(self):
        """
        **[Required]** Gets the item_duration_in_ms of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        Time duration in milliseconds between data points (one hour or one day).


        :return: The item_duration_in_ms of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :rtype: int
        """
        return self._item_duration_in_ms

    @item_duration_in_ms.setter
    def item_duration_in_ms(self, item_duration_in_ms):
        """
        Sets the item_duration_in_ms of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        Time duration in milliseconds between data points (one hour or one day).


        :param item_duration_in_ms: The item_duration_in_ms of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type: int
        """
        self._item_duration_in_ms = item_duration_in_ms

    @property
    def capacity_data(self):
        """
        **[Required]** Gets the capacity_data of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        Capacity Data with time interval


        :return: The capacity_data of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :rtype: list[ResourceCapacityTrendAggregation]
        """
        return self._capacity_data

    @capacity_data.setter
    def capacity_data(self, capacity_data):
        """
        Sets the capacity_data of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        Capacity Data with time interval


        :param capacity_data: The capacity_data of this SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection.
        :type: list[ResourceCapacityTrendAggregation]
        """
        self._capacity_data = capacity_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other