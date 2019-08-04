import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }, { 'a' : 2, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }]
data1 = {'status':200,'code':'sss','result':data}

json1 = json.dumps(data)
json2 = json.dumps(data1)
print(json1)
print(json2)