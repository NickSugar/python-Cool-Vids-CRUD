from app import db, models

db.session.query(models.Vids).delete()
db.session.query(models.Users).delete()

user1 = models.Users(name='nick')
user2 = models.Users(name='bill')
user3 = models.Users(name='rob')
user4 = models.Users(name='joe')

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)

vid1 = models.Vids(
    user_id=1,
    title='The whitest kids you know S1E1',
    url='https://youtu.be/ME7smdgMVr4?list=PL1E7ADC0B6C30C1DF',
    year='2005')
vid2 = models.Vids(
    user_id=1,
    title='The whitest kids you know S1E2',
    url='https://youtu.be/ME7smdgMVr4?list=PL1E7ADC0B6C30C1DF',
    year='2005')
vid3 = models.Vids(
    user_id=2,
    title='Alfie Aesthetics',
    url='https://youtu.be/stIjgEaES60',
    year='2017')
vid4 = models.Vids(
    user_id=2,
    title='Alfie Aesthetics',
    url='https://youtu.be/EMKB6hPnMAk',
    year='2015')
vid5 = models.Vids(
    user_id=3,
    title='DJ Angelo',
    url='https://youtu.be/tr3ftsCVXhc',
    year='2011')
vid6 = models.Vids(
    user_id=3,
    title='DJ Lady Style',
    url='https://youtu.be/sFIS3ndfro0',
    year='2016')
vid7 = models.Vids(
    user_id=4,
    title='How a nuclear bombs work 1',
    url='https://youtu.be/zVhQOhxb1Mc',
    year='2013')
vid8 = models.Vids(
    user_id=4,
    title='How a nuclear bombs work 1',
    url='https://youtu.be/MnW7DxsJth0',
    year='2013')

db.session.add(vid1)
db.session.add(vid2)
db.session.add(vid3)
db.session.add(vid4)
db.session.add(vid5)
db.session.add(vid6)
db.session.add(vid7)
db.session.add(vid8)

db.session.commit()
