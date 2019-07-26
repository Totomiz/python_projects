import asyncio

from www.dbconnector import Video, DBSession

mv1 = Video(title_cn='wo shi 1', )
mv2 = Video(title_cn='wo shi 2')
mv3 = Video(title_cn='wo shi 3')

print("---", mv1.title_cn, mv1)

mvList = [mv1, mv2, mv3]


def checkSame():
    see = DBSession()
    mv4 = Video(title_cn='wo shi 4')
    mv5 = Video(title_cn='wo shi 1')
    see.add(mv4)
    print('same-->mv4===', mv4)
    see.query(mv5)
    outUser = see.query(Video).filter_by(title_cn='wo shi 4').first()
    outUser2 = see.query(Video).filter_by(title_cn='wo shi 1').first()
    print('same-->out===', outUser)
    print('same-->', mv5 is outUser2)

    see.commit()
    see.close()


async def addMovie():
    see = DBSession()
    print("start --- add move")
    await asyncio.sleep(2)
    see.add_all(mvList)
    see.commit()
    see.close()
    # for mv in mvList:
    #     print("add-->", mv)
    print("end --- add move--end")
    checkSame()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(addMovie())

# @property
# def __repr__(self):
#     return "<Movie(title_cn='%s', title_en='%s', g_path='%s',director='%s',actors='%s',subtitle='%s',desc='%s'," \
#            "poster='%s')>" % (self.title_cn, self.title_en, self.g_path)
