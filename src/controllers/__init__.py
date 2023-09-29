from controllers.users import users
from controllers.auth import auths
from controllers.suppliers import suppliers
from controllers.statuses import statuses
from controllers.purchases import purchases

registered_controllers = (
    users,
    auths,
    suppliers,
    statuses,
    purchases,
)