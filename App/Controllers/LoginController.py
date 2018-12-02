# -*- coding: utf-8 -*-
from App import app
from flask import request, jsonify
import lang as LANG
import helper as help


@app.route('/api/auth/login', methods=['POST'])
# TODO: Принимает login, password
# TODO: Возвращает token
def login_user():
    if not request.json:
        return jsonify({'desc': LANG.user['jsonError']}), 500
    try:
        import App.Entity.Users as User
        user = User.Users.where(id=request.json['login']).first()
        if not user:
            return jsonify({'desc': LANG.user['notFind']}), 500
        if user.password == request.json['password']:
            if not len(user.token):
                token = user.token
            else:
                token = user.token[0]
            from datetime import datetime, timedelta
            import uuid as hash
            date = datetime.now() + timedelta(hours=1)
            date = date.strftime('%Y-%m-%d %H:%M:%S')
            if not token:
                # create TOKEN
                token = User.Tokens(
                    user_id=user.id,
                    token=hash.uuid4().hex,
                    date_life=date)
                help.session.add(token)
                help.session.commit()
                return jsonify({'token': token.token, 'user': {
                    'first_name': user.fname,
                    'last_name': user.lname,
                    'second_name': user.sname,
                    'status': user.status
                }})
            else:
                # update TOKEN
                token.update(
                    token=hash.uuid4().hex,
                    date_life=date)
                help.session.commit()
                return jsonify({'token': token.token, 'user': {
                    'first_name': user.fname,
                    'last_name': user.lname,
                    'second_name': user.sname,
                    'status': user.status
                }})
        else:
            return jsonify({'desc': LANG.user['incPassword']}), 500
    except KeyError as e:
        return jsonify({'desc': str(e)}), 500


@app.route('/api/auth/logout', methods=['POST'])
# TODO: Принимает token
# TODO: Возвращает status-code
def logout_user():
    if not request.json:
        return jsonify({'desc': LANG.user['jsonError']}), 500
    try:
        import App.Entity.Users as User
        token = request.json['token']
        user = User.Tokens.where(token=token).first()
        if not user:
            return jsonify({'desc': LANG.user['notFind']}), 500
        else:
            user.update(token='')
            help.session.commit()
            return jsonify({'desc': LANG.user['logout']}), 200
    except KeyError as e:
        return jsonify({'desc': str(e)}), 500
