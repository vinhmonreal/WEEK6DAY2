from flask import request, jsonify

from . import bp
from app.models import User

# Verify User
# @bp.route('/verify-user',methods=['POST'])
# same as above
@bp.post('/verifyuser')
def verify_user():
  content = request.json
  print(content)
  username= content['username']
  password= content['password']
  user = User.query.filter_by(username=username).first()
  if user and user.check_password(password):
    return jsonify([{'user token': user.token}])
  return jsonify([{'message':'Invalid User Info'}]) 
