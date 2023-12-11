import requests
import re
from bs4 import BeautifulSoup
import json

def bruteforce_staff_id(id_start=0, id_end=61141001):

    for id in range(id_start, id_end):
        path = f"https://ssau.ru/rasp?staffId={id}"
        response = requests.get(path)
        # print(response)
        if response.status_code == 200:
            print(f"staff id successful: {id}")
            soup = BeautifulSoup(response.text, "html.parser")
            # print(response.text)
            main_block = soup.findAll('div', class_='info-block__main')
            if len(main_block) == 0:
                print(f"staff id {id} main_block empty")
                continue

            staff_fio = None
            staff_additional_info = None
            for child in main_block[0].children:
                # print(child)
                if not child.attrs:
                    continue
                if "info-block__title" in child.attrs['class']:
                    staff_fio = child.text
                    staff_fio = staff_fio.replace(" ", "")
                    staff_split_list = re.split("([А-Я])", staff_fio)
                    staff_fio = ""
                    conceited = 0
                    for staff_elem in staff_split_list:
                        if staff_elem == "":
                            continue
                        if conceited % 2 == 0 and conceited != 0:
                            staff_fio = staff_fio + " " +staff_elem
                        else:
                            staff_fio = staff_fio + staff_elem
                        conceited += 1
                elif "info-block__description" in child.attrs['class']:
                    print(child)
                    if child.text:
                        staff_additional_info = child.text[1:]


            main_block_soup = BeautifulSoup()
            # main_block_info_block_title =
            # info-block_title
            print(f"Обработал staff id {id}, ФИО: {staff_fio}, доп.информация: {staff_additional_info}")
            # print(main_block)


def get_groups_id(link_to_inst, course_start, course_end):
    group_and_id = []
    for course in range(course_start, course_end+1):
        path = link_to_inst + f"?course={course}"
        response = requests.get(path)
        if response.status_code >= 300:
            print(f"SKIPPED COURSE {course}")
        soup = BeautifulSoup(response.text, "html.parser")
        group_list_element = soup.findAll('div', class_='card-default group-catalog__item')
        group_a_elements = soup.findAll('a', class_="btn-text group-catalog__group")
        for group_element in group_a_elements:
            group = group_element.text
            group = group.replace(" ", "")
            group_id = group_element.attrs['href'].split('groupId=')[1]
            group_and_id.append({'id': group_id, 'group': group})
    return group_and_id


def get_all_faculty(rasp_link):
    list_of_faculties = []
    path = rasp_link
    response = requests.get(path)
    if response.status_code >= 300:
        raise AssertionError("https://ssau.ru/rasp is not reachable")
    soup = BeautifulSoup(response.text, "html.parser")
    faculties_items = soup.findAll("div", class_="card-default faculties__item")
    for faculty_item in faculties_items:
        children_a = faculty_item.findChildren("a", recursive=False)[0]
        faculty_id = children_a.attrs['href'].split('faculty/')[1]
        faculty_id = faculty_id.split('?course')[0]
        list_of_faculties.append({'id': faculty_id, 'faculty': children_a.text})
    return list_of_faculties


def get_all_staff(staff_link, start_page, end_page):
    list_of_staff = []
    for page in range(start_page, end_page+1):
        path = staff_link + f"?page={page}"
        response = requests.get(path)
        if response.status_code >= 300:
            print(f"SKIPPED STAFF PAGE {page}")
        soup = BeautifulSoup(response.text, "html.parser")
        list_items = soup.findAll('li', class_="list-group-item list-group-item-action")
        for list_item in list_items:
            # print(list_item)
            children_a = list_item.findChildren("a", recursive=False)[0]
            staff_id = children_a.attrs['href'].split('/staff/')[1]
            staff_id = staff_id.split('-')[0]
            staff_fio = children_a.text.replace('\n', '')
            list_of_staff.append({'id': staff_id, 'fio': staff_fio})
    print(list_of_staff)
    return list_of_staff


def get_week_schedule(link, group_id, week_number):
    path = link + f"?groupId={group_id}&selectedWeek={week_number}"
    response = requests.get(path)
    if response.status_code >= 300:
        print(f"CANNOT PARSE WEEK SCHEDULE FOR GROUP {group_id} week {week_number}")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    schedule_head = soup.findAll('div', class_="schedule__head")
    schedule_times = soup.findAll('div', class_="schedule__time")
    schedule_time_and_head_dict = {}
    for schedule_time in schedule_times:
        day = 1
        schedule_time_text = schedule_time.text
        sibling = schedule_time.next_sibling
        while sibling and 'schedule__time' not in sibling.attrs['class']:
            day_name = schedule_head[day].text
            if day_name not in schedule_time_and_head_dict:
                schedule_time_and_head_dict[day_name] = [{"time": schedule_time_text, "value": sibling.text}]
            else:
                schedule_time_and_head_dict[day_name].append({"time": schedule_time_text, "value": sibling.text})
            sibling = sibling.next_sibling
            day += 1
    print(schedule_time_and_head_dict)
    return schedule_time_and_head_dict


def get_week_schedule_by_rows(link, group_id, week_number):
    path = link + f"?groupId={group_id}&selectedWeek={week_number}"
    response = requests.get(path)
    if response.status_code >= 300:
        print(f"CANNOT PARSE WEEK SCHEDULE FOR GROUP {group_id} week {week_number}")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    schedule_head = soup.findAll('div', class_="schedule__head")
    schedule_times = soup.findAll('div', class_="schedule__time")
    schedule_time_and_head_dict = {}
    rows = list()
    heads_list = []
    for schedule_head_item in schedule_head:
        schedule__text = schedule_head_item.text[1:] if len(schedule_head_item.text) > 0 else schedule_head_item.text
        schedule__text = "\n".join(schedule__text.split(" "))
        heads_list.append({"text": schedule__text})
    rows.append({"row_data": heads_list})

    for row_id, schedule_time in enumerate(schedule_times):
        day = 0
        sibling = schedule_time.next_sibling
        schedule_time_text = schedule_time.text[1:] if len(schedule_time.text) > 0 else schedule_time.text
        list_to_add = [{"text":schedule_time_text}]
        while sibling and 'schedule__time' not in sibling.attrs['class']:
            sibling_text = sibling.text[1:] if len(sibling.text) > 0 else sibling.text
            if len(sibling_text) > 1:
                sibling_soup = BeautifulSoup(str(sibling), "html.parser")
                schedule_place = sibling_soup.findAll("div", class_="schedule__place")
                if schedule_place:
                    schedule_place_text = schedule_place[0].text[1:]
                    sibling_text = sibling_text.replace(schedule_place_text, "  " + schedule_place_text)
            sibling_text = "\n".join(sibling_text.split("  "))
            print(sibling_text)
            list_to_add.append({"text": sibling_text})
            sibling = sibling.next_sibling
            day += 1
        rows.append({"row_data": list_to_add})
    print(schedule_time_and_head_dict)
    return rows



if __name__ == "__main__":
    # get_week_schedule("https://ssau.ru/rasp", 531030143, 14)
    # get_week_schedule("https://ssau.ru/rasp", 530994406, 15)
    get_week_schedule_by_rows("https://ssau.ru/rasp", 531030143, 15)
    staff_list = get_all_staff("https://ssau.ru/staff", 1, 121)
    faculties = get_all_faculty("https://ssau.ru/rasp")
    print(faculties)
    all_groups = []
    for faculty_dict in faculties:
        faculty_id = faculty_dict['id']
        groups_and_id = get_groups_id(f"https://ssau.ru/rasp/faculty/{faculty_id}", 1, 7)
        all_groups += groups_and_id
        print(f"for faculty {faculty_dict['faculty']}, id: {faculty_id} :")
        print(groups_and_id, end='\n\n')
    to_json = {"groups": all_groups, "staff": staff_list}
    with open(r'groups_and_staff.json', 'w', encoding='utf-8') as f:
        json.dump(to_json, f, ensure_ascii=False, indent=4)
    # bruteforce_staff_id(664000000, 664018050)  # [664017039;664018100] - only 664017039 is good (not sure) 664018323 - good 664019682 - good

