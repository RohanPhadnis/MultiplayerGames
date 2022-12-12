import pymongo

mongo = pymongo.MongoClient('mongodb+srv://anyone:xyz@flask.ngjrl.mongodb.net/MultiplayerGames?retryWrites=true&w=majority')
db = mongo['test']
col = db['game_objects']
d = dict(col.find_one({'name': 'x'}))

while d['run'] < 19:
    print(d)
    d = dict(col.find_one({'name': 'x'}))
