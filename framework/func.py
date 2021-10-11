from flask import request
from jsonschema import Draft6Validator

# this file is a validate file, validate all schema ( in schema.py) with input all html or rescilent ( with header Content-Type:application/json)
class xd:
    def xacdinh_m(todo_schema):                         # validate with input schemas have type   [{"key":"value","key":"value".....},{"key":"value","key":"value".....},...]
        list_request_error = []
        v = Draft6Validator(todo_schema)
        dict = request.get_json()
        for dict1 in dict :
            c= v.iter_errors(dict1)
            for error in c:
                list_request_error.append(error.message)
        return list_request_error
    def xacdinh(todo_schema):                            # validate with input schemas have type   {"key":"value","key":"value".....}
        list_request_error =[]
        v = Draft6Validator(todo_schema)
        dict1 = request.get_json()
        c= v.iter_errors(dict1)
        for error in c:
            list_request_error.append(error.message)
        return list_request_error


