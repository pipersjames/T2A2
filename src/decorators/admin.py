# custom decorator to handle authorization
from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from models.users import User
from main import db

# used to ensure that the current user is admin
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        query = db.select(User).filter_by(email=current_user)
        user = db.session.scalar(query)
        
        if user and user.admin:
            return fn(*args, **kwargs)
        else:
            return jsonify({"message": "Access denied. Admin privileges required."}), 403  # 403 Forbidden

    return wrapper