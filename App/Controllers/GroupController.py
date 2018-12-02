# -*- coding: utf-8 -*-
from App import app
from flask import request, jsonify
import lang as LANG
import helper as help


@app.route('/api/group/get', methods=['POST'])
# TODO: Принимает token
# TODO: Возвращает {
# TODO: если вы учитель - СПИСОК ГРУПП в которых вы преподаете
# TODO: если вы студент - СПИСОК СТУДЕНТОВ И ПРЕПОДАВАТЕЛЕЙ вашей группы
# TODO: }
def group_user():
    if not request.json:
        return jsonify({'desc': LANG.user['jsonError']}), 500
    try:
        import App.Entity.Users as User
        user = User.Tokens.where(token=request.json['token']).first()
        if not user:
            return jsonify({'desc': LANG.user['notFind']}), 500
        if user.user.status == 1:
            # teacher
            arr = {'groups': []}
            groups = User.Group_User.where(user_id=user.user.id).all()
            for group in groups:
                arr['groups'].append({
                    'id': group.group_id,
                    'name': group.group.name
                })
            return jsonify(arr), 200
        elif user.user.status == 0:
            #student
            arr = {'teachers': [], 'students': []}
            for item in user.user.group:
                if len(item.group.group_user):
                    for student in item.group.group_user:
                        if student.user.status == 1:
                            arr['teachers'].append({
                                'id': student.user.id,
                                'first_name': student.user.fname,
                                'last_name': student.user.lname,
                                'second_name': student.user.sname
                            })
                        elif student.user.status == 0:
                            arr['students'].append({
                                'id': student.user.id,
                                'first_name': student.user.fname,
                                'last_name': student.user.lname,
                                'second_name': student.user.sname
                            })
            return jsonify(arr), 200
    except KeyError as e:
        return jsonify({'desc': str(e)}), 500
