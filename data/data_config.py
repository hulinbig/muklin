# coding=utf-8

class global_var:
    #case_id
    ID = 0
    url = 2
    run = 6
    request_way = 4
    header = 5
    case_depend = 7
    data_depend = 8
    field_depend = 9
    data = 3
    expect = 10
    actual_result = 11

#获取caseid
def get_id():
    return global_var.ID

def get_url():
    return global_var.url

def get_run():
    return global_var.run

def get_request_way():
    return global_var.request_way

def get_header():
    return global_var.header

def get_case_depend():
    return global_var.case_depend

def get_data_depend():
    return global_var.data_depend

def get_field_depend():
    return global_var.field_depend

def get_data():
    return global_var.data

def get_expect():
    return global_var.expect

def get_result():
    return global_var.actual_result

def get_header_value():
    header = {}