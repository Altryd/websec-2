import os

import flask
import json
from flask import request, Blueprint, jsonify
from app.utility import get_week_schedule_by_rows, get_current_week_parse


api_routes = Blueprint('api_routes', __name__, template_folder='templates', url_prefix="/api")


@api_routes.route('/get_ok', methods=["GET"])
def get_ok():
    return jsonify(["ky"]), 200, {"Content-Type": "application/json"}


@api_routes.route('/search_group', methods=["GET"])
def search_group():
    args = request.args
    if 'group' in args:
        group_substr = args['group']
    else:
        group_substr = None
    with open(r"backend/groups_and_staff.json", "r", encoding='utf-8') as file:
        data = json.loads(file.read())
        groups = data['groups']
    if group_substr:
        groups = list(filter(lambda group: group_substr in group['group'], groups))
    pagination_ = 10
    return jsonify(groups), 200, {"Content-Type": "application/json"}


@api_routes.route('/search_staff', methods=["GET"])
def search_staff():
    args = request.args
    if 'fio' in args:
        fio_substr = args['fio']
    else:
        fio_substr = None
    print(os.getcwd())
    with open(r"backend/groups_and_staff.json", "r", encoding='utf-8') as file:
        data = json.loads(file.read())
        staff = data['staff']
    if fio_substr:
        staff = list(filter(lambda person: fio_substr in person['fio'], staff))
    return jsonify(staff), 200, {"Content-Type": "application/json"}

#test[' вторник 28.11.2023'][1]['value'].split("  ")  [' Компьютерная алгебра 608 - 18', 'Веричев А.В.', ' 6411-100503D', ' 6412-100503D ']
#test[' среда 29.11.2023'][3]['value'].split("  ")  [' веб-разработка 611 - 18', 'Чупшев Н.В.', ' Подгруппы: 2 ']
@api_routes.route('/get_week_schedule', methods=['GET'])
def get_schedule():
    args = request.args
    if "week" in args:
        week = args['week']
    else:
        week = get_current_week_parse()
    if "groupId" in args:
        groupId = args['groupId']
    else:
        groupId = None
    if "staffId" in args:
        staffId = args['staffId']
    else:
        staffId = None
    if not staffId and not groupId:
        groupId = 531030143

    print(f"week: {week}")
    rows = get_week_schedule_by_rows("https://ssau.ru/rasp", group_id=groupId, staff_id=staffId, week_number=week)
    return jsonify(rows), 200, {"Content-Type": "application/json"}


from time import sleep
@api_routes.route('/get_current_week', methods=['GET'])
def get_current_week():
    args = request.args
    current_week = get_current_week_parse()
    if current_week:
        return jsonify({"current_week": current_week}), 200, {"Content-Type": "application/json"}
    else:
        return jsonify({"current_week": None}), 404, {"Content-Type": "application/json"}

