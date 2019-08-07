from www.dbconnector import Video, genres_dict
from www.dbdao import init_genres


def find_video_name_dic():
    print(Video.__dict__.keys())
    print(Video.id.name, Video.title_cn, Video.title_en, Video.g_path, Video.poster, Video.subtitle,
          Video.actors,
          Video.director, Video.total, Video.obtain_id)


list1 = set()
for k, v in genres_dict.items():
    print(k, v)
    list1.add(v)
    print(list1)

if __name__ == "__main__":
    find_video_name_dic()
    # print(genres_dict.items())
    # list=genres_dict.values()
    # for k,v in
    # list=genres_dict.items()
    # print( list[0])
    init_genres()
