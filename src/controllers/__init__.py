from controllers.users import users
from controllers.auth import auths
from controllers.suppliers import suppliers
from controllers.statuses import statuses
from controllers.purchases import purchases
from controllers.requests import requests
from controllers.purchase_orders import purchase_orders

registered_controllers = (
    users,
    auths,
    suppliers,
    statuses,
    purchases,
    requests,
    purchase_orders,
)