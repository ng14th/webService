# all input on HTML or Restclient all following type {"key":"value","key":"value".....} or if input required list of dict => [{"key":"value","key":"value".....},{"key":"value","key":"value".....}]


traicay = {
    "User": [
    {
    "username": {},
    "xoai": {"type":"number","minimum": 0},
    "cam": {"type":"number","minimum": 0},
    "vai": {"type":"number","minimum": 0},
    "tao": {"type":"number","minimum": 0}
  },
    ],
    "additionalUser":False,
    "required": ["username"]   
}

username = {
    "properties":
    {
        "username":{}
    },
    "additionalProperties":False,
    "required":["username"]
}

money_add = {
    "add": [
    {
        "username":{},
        "money":{"type":"number","minimum":1}
    },
    ],
    "additionalAdd":False,
    "required":["username","money"]
}

date = {
    "properties":
    {
        "date_start":{},
        "date_end":{}
    },
    "additionalProperties":False,
    "required":["date_start","date_end"]
}

table = {
    "properties":
    {
        "table":{},
        "keep":{"type":"number","minimum":1}
    },
    "additionalProperties":False,
    "required":["table","keep"]
}

date_money = {
    "properties":
    {
        "string_input":{},
        "salary_start":{},
        "salary_end":{}
    },
    "additionalProperties":False
}
