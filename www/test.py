from www.dbconnector import Video


def find_video_name_dic():
    print(Video.__dict__.keys())
    print(Video.id.name, Video.title_cn, Video.title_en, Video.g_path, Video.poster, Video.subtitle,
          Video.actors,
          Video.director, Video.total, Video.obtain_id)


if __name__ == "__main__":
    find_video_name_dic()
