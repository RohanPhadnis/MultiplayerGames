import pymongo

mongo = pymongo.MongoClient('mongodb+srv://anyone:xyz@flask.ngjrl.mongodb.net/MultiplayerGames?retryWrites=true&w=majority')
db = mongo['test']
col = db['game_objects']
d = {'name': 'x', 'num': 0, 'run': 0}
run = 0

while run < 30:
    for n in range(100):
        col.update_one({'name': 'x'}, {'$set': {'num': n, 'run': run}})
    run += 1

mongo.close()
