import json

code_dict = {'200': 'success', '400': 'Failed'}

success_dic = {'code': code_dict.get('200'), 'status': 'success', 'data': None}


def success_wrap_data(arg):
    dic = {'code': code_dict.get('200'), 'status': 'success', 'data': arg}
    st = json.dumps(dic)
    print(st)
    return st

def success_wrap_data2(arg):
    L=[]
    for x in arg:
        L.append(x.__repr__())
    print('LIST==',L)
    L2=['Genres(id=1,name=电视剧,path=1,)', 'Genres(id=2,name=连续剧,path=2,)', 'Genres(id=3,name=电影,path=3,)', 'Genres(id=4,name=综艺,path=4,)', 'Genres(id=5,name=教育,path=5,)']
    dic = {'code': code_dict.get('200'), 'status': 'success', 'data': L.__str__()}
    print('dic=',dic.__repr__())
    return dic



