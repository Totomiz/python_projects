import xlrd

from www.dbconnector import Video, Sources, DBSession, genres_dict

book = xlrd.open_workbook('E:\docments\媒资.xls')
print('num of sheet is {0}'.format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))

print(set(sh.col_values(4)))
print(sh.row_values(0))
# print(sh.row_values(5000))
# for x in sh.row_values(0):
#     print(x)
# for rx in sh.col_values(1,0):
#     print(rx)


titleList = ['编号', '影片名称', '英文名称', '集数', '影片类型', '导演', '演员', '子标题', '影片描述', '片源']
lastRow = [3857.0, '贺少的闪婚暖妻第2季', 'heshaodeshanhunnuanqidi2ji', 0.0, '动漫', '未知', '内详', '做我贺乔宴的女人，必须满足三',
           '做我贺乔宴的女人，必须满足三个条件：喜欢被呵宠、喜欢被疼爱、喜欢被无微不至的照顾。这个女人恰好满足了所有要求，就要有只属于他的觉悟。',
           '第01集$https://bili.meijuzuida.com/20190607/16995_727c288e/index.m3u8$zuidam3u8#第02集$https://bili'
           '.meijuzuida.com/20190607/16994_ae730b9c/index.m3u8$zuidam3u8#第03集$https://bili.meijuzuida.com/20190607'
           '/16993_b22e8077/index.m3u8$zuidam3u8#第04集$https://bili.meijuzuida.com/20190607/16992_2b7224e1/index'
           '.m3u8$zuidam3u8#第05集$https://bili.meijuzuida.com/20190607/16991_7789a21d/index.m3u8$zuidam3u8#第06集$https'
           '://bili.meijuzuida.com/20190607/16990_bfa27a95/index.m3u8$zuidam3u8#第07集$https://bili.meijuzuida.com'
           '/20190607/16989_78ce53c7/index.m3u8$zuidam3u8#第08集$https://bili.meijuzuida.com/20190607/16987_f3182a8c'
           '/index.m3u8$zuidam3u8#第09集$https://bili.meijuzuida.com/20190614/17783_8456030a/index.m3u8$zuidam3u8#第10'
           '集$https://iqiyi.qq-zuidazy.com/20190620/12566_242553de/index.m3u8$zuidam3u8#第11集$https://bili.meijuzuida'
           '.com/20190627/19441_7e940845/index.m3u8$zuidam3u8#第12集$https://bili.meijuzuida.com/20190706'
           '/20162_c188c556/index.m3u8$zuidam3u8#第13集$https://wuji.zhulong-zuida.com/20190712/1718_889e7914/index'
           '.m3u8$zuidam3u8#第14集$https://yanzishan.shuhu-zuida.com/20190719/371_0481aa55/index.m3u8$zuidam3u8']


def read_xls_not_empty_value(save_db_func):
    count = 0
    for rx in range(sh.nrows):
        if rx == 0:
            print('skip first row->>', sh.row(rx))
            continue
            # 跳过空的
        if sh.cell_value(rx, sh.ncols - 1) == "":
            continue
        else:
            # print("All not empty row= ",rx，' item= ',sh.row_values(rx))
            save_db_func(sh.row_values(rx))
            count += 1
    print("All not empty item count=", count)


def parse_source_to_list(src_str, obtain_id):
    source = []
    strList = src_str.split('#')
    for item in strList:
        # assert isinstance(item.split, st)
        assert isinstance(item, str)
        subInfo = item.split('$')
        if subInfo[1].startswith('暂缺'):
            print('skip with 暂缺', subInfo)
            print('skip with 暂缺 obtain_id->', obtain_id)
            continue
        if not subInfo[1].startswith('http'):
            print('find one not start with http:-->', subInfo, obtain_id, src_str)
            print('find one not start with obtain_id:->', obtain_id)
        assert subInfo[1].startswith(('http'))
        item = Sources(name=subInfo[0], src=subInfo[1], video_obtain_id=obtain_id)
        source.append(item)
    return source


# 读取一行值，写入数据库
def import_all_video(value):
    movieList = []
    # ['编号', '影片名称', '英文名称', '集数', '影片类型', '导演', '演员', '子标题', '影片描述', '片源']
    ob_id = '@{}!{}'.format(value[1], value[5])
    source = value[9]
    mv = Video(title_cn=value[1], title_en=value[2], total=int(value[3]), g_path=genres_dict.get(value[4]),
               director=value[5], actors=value[6], subtitle=value[7], desc=value[8], obtain_id=ob_id)
    mv.sources = parse_source_to_list(source, ob_id)
    # print("insert-->", mv)
    movieList.append(mv)

    se = DBSession()
    se.add_all(movieList)
    se.commit()
    se.close()


read_xls_not_empty_value(import_all_video)
