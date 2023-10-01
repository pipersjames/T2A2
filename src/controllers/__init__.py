from controllers.auth import auths
from controllers.departments import departments
from controllers.items import items
from controllers.purchase_orders import purchase_orders
from controllers.purchases import purchases
from controllers.request_types import request_types
from controllers.requests import requests
from controllers.statuses import statuses
from controllers.suppliers import suppliers
from controllers.users import users


registered_controllers = (
    users,
    auths,
    suppliers,
    statuses,
    purchases,
    requests,
    purchase_orders,
    items,
    request_types,
    departments,
)