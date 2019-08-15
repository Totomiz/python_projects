from www.ApiDataConvert import success_wrap_data
from www.dbdao import *

# 主页style(style=1 banner)/(style=2 没有第一条头部的style)/(style=2 第一条数据独占一格的style)

main_types_item = [['Banner', 1, "某某干嘛了"], ['今日热点', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                   ['天线宝宝', 3, '这就是巨星']]

dianshi_types_item = [['Banner', 1, "某某干嘛了"], ['电视', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                      ['天线宝宝', 3, '这就是巨星']]
lianxu_types_item = [['Banner', 1, "某某干嘛了"], ['电视', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                     ['天线宝宝', 3, '这就是巨星']]
movie_types_item = [['Banner', 1, "某某干嘛了"], ['电视', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                    ['天线宝宝', 3, '这就是巨星']]
zongyi_types_item = [['Banner', 1, "某某干嘛了"], ['电视', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                     ['天线宝宝', 3, '这就是巨星']]
jiaoyu_types_item = [['Banner', 1, "某某干嘛了"], ['电视', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                     ['天线宝宝', 3, '这就是巨星']]
yinyue_types_item = [['Banner', 1, "某某干嘛了"], ['电视', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                     ['天线宝宝', 3, '这就是巨星']]
jilupian_types_item = [['Banner', 1, "某某干嘛了"], ['电视', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                       ['天线宝宝', 3, '这就是巨星']]
dongman_types_item = [['Banner', 1, "某某干嘛了"], ['电视', 2, "某某干嘛了"], ['热剧点播', 3, '这就是描述'], ['乱世巨星', 3, '这就是巨星'],
                      ['天线宝宝', 3, '这就是巨星']]

# 推荐style(21 竖条,三栏一行)
# 推荐栏目的项目数,暂只有1条
recommend_types_all_item = [['今日影片推荐', 21, "本周热门排行"]]

# genres_dict = {'推荐': '0,', '电视剧': '1,', '连续剧': '2,', '电影': '3,', '综艺': '4,', '教育': '5,', '音乐': '6,', '记录片': '7,',
#                '动漫': '8,'}


category_dict = {
    '0,': main_types_item,
    '1,': dianshi_types_item,
    '2,': lianxu_types_item,
    '3,': movie_types_item,
    '4,': zongyi_types_item,
    '5,': jiaoyu_types_item,
    '6,': yinyue_types_item,
    '7,': jilupian_types_item,
    '8,': dongman_types_item,
}

# 按分类推荐的数据，暂统一设为recommend_types_all_item
recommend_category_dict = {
    '0,': recommend_types_all_item,
    '1,': recommend_types_all_item,
    '2,': recommend_types_all_item,
    '3,': recommend_types_all_item,
    '4,': recommend_types_all_item,
    '5,': recommend_types_all_item,
    '6,': recommend_types_all_item,
    '7,': recommend_types_all_item,
    '8,': recommend_types_all_item,
}


def get_genres():
    return '{}'.format(success_wrap_data(get_all_genres()))


# 获取主页第一页推荐数据
def get_home_main(g_path="1,"):
    result_dict = {}
    genres = get_all_genres()
    result_dict['genres'] = genres
    dataList = []
    for idx, valueList in enumerate(main_types_item):
        data_item_dict = {}
        # item = query_video_by_simple('电视剧', 4)
        offset = 0
        if valueList[1] == 3:  # 需要获取5个
            offset = 1
        item = query_video_by_slice('电视剧', idx * 4 + offset, idx * 4 + offset + 4 + offset)
        data_item_dict['name'] = valueList[0]
        data_item_dict['style'] = valueList[1]
        data_item_dict['message'] = valueList[2]
        data_item_dict['g_path'] = g_path
        data_item_dict['item'] = item
        dataList.append(data_item_dict)
    result_dict['channel'] = dataList
    return '{}'.format(success_wrap_data(result_dict))


def get_home_category_data(g_path):
    if g_path == '0,':
        return get_home_main(g_path)
    result_dict = {}
    genres = get_all_genres()
    result_dict['genres'] = genres
    dataList = []
    for idx, valueList in enumerate(category_dict[g_path]):
        data_item_dict = {}
        # item = query_video_by_simple('电视剧', 4)
        offset = 0
        if valueList[1] == 3:  # 需要获取5个
            offset = 1
        item = query_video_by_path_slice(g_path, idx * 4 + offset, idx * 4 + offset + 4 + offset)
        data_item_dict['name'] = valueList[0]
        data_item_dict['style'] = valueList[1]
        data_item_dict['message'] = valueList[2]
        data_item_dict['g_path'] = g_path
        data_item_dict['item'] = item
        dataList.append(data_item_dict)
    result_dict['channel'] = dataList
    return '{}'.format(success_wrap_data(result_dict))


# 获取推荐数据
def get_api_recommend_data(g_path, length):
    result_dict = {}
    dataList = []

    # 获取recommend_category_dict 中g_path对应的数据
    for idx, valueList in enumerate(recommend_category_dict[g_path]):
        data_item_dict = {}
        # item = query_video_by_simple('电视剧', 4)
        item = query_recommend_video_by_path(g_path, length)
        data_item_dict['name'] = valueList[0]
        data_item_dict['style'] = valueList[1]
        data_item_dict['message'] = valueList[2]
        data_item_dict['g_path'] = g_path
        data_item_dict['item'] = item
        dataList.append(data_item_dict)
    result_dict['channel'] = dataList
    return '{}'.format(success_wrap_data(result_dict))


# 获取分类分页数据
def get_api_group_page_data(g_path, page):
    result_dict = {}
    # 15 个条目为一组
    page_length = 15
    query_result = query_group_page_data_by_path(g_path, page, page_length)
    item = query_result[0]
    total_page = query_result[1] / page_length
    result_dict['totalPage'] = int(total_page)
    result_dict['item'] = item
    return '{}'.format(success_wrap_data(result_dict))


# 无channel 分类数据，未使用
def get_home_type(g_path):
    # result_dict = {}
    # genres = get_all_genres()
    # result_dict['genres'] = genres
    # dataList = []
    # for name in main_types_item:
    #     data_item_dict = {}
    #     item = query_video_by_path_and_limit(g_id, 4)
    #     data_item_dict['name'] = name
    #     data_item_dict['item'] = item
    #     dataList.append(data_item_dict)
    # result_dict['channel'] = dataList
    result_dict = {'item': query_video_by_path_simple(g_path, 4)}
    return '{}'.format(success_wrap_data(result_dict))


def get_detail(obtain_id):
    return '{}'.format(success_wrap_data(query_detail_video_by_obtain_id(obtain_id)))
