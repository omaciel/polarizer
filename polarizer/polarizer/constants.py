
from collections import OrderedDict
from rows import fields


PLAN_WSDL = '{}/ws/services/PlanningWebService?wsdl'
SESSION_WSDL = '{}/ws/services/SessionWebService?wsdl'
TRACKER_WSDL = '{}/ws/services/TrackerWebService?wsdl'

PLAN_FIELDS = OrderedDict([
    ('id', fields.TextField),
    ('author', fields.TextField),
    ('test_cases', fields.TextField),
])
