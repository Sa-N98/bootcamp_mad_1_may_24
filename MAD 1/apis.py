from flask_restful import Resource, reqparse
from model import *



class playList(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('playlist_name', required=True, help="Playlist name is required")
        parser.add_argument('options', action='append', required=True, help="At least one song must be selected")
        parser.add_argument('use_ID',  required=True)


        args = parser.parse_args()

        playlist_name = args['playlist_name']
        song_ids = args['options']
        user_Id =args['use_ID']

        songs= ''.join(song_ids)
        # print(songs)

        if playlist.query.filter(playlist.playlistName ==  playlist_name).first():
            return { 'massage' : "playlist already exists. please use a differen name "}


        newPlaylist = playlist(playlistName= playlist_name, songList = songs) 
        db.session.add(newPlaylist)
        db.session.commit()  

        pl= playlist.query.filter(playlist.playlistName ==  playlist_name).first()
    

        new_relation = user_playlist(playlist_id = pl.id  , user_id= user_Id)
        db.session.add(new_relation)
        db.session.commit()  
        
        print( 'playlist_name ' ,  playlist_name)
        print('song_ids ', song_ids )
        return { 'massage' : "playlist created succesfully "}
    

class testAPI(Resource):
    # def post ()                   # c
    # def get()                     # r
    # def put()                     # u
    # def delete()                  # d


    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('num1', type=str)
        parser.add_argument('num2', type=str)
        parser.add_argument('opper', type=str)

        args = parser.parse_args()

        # print(args['num1'])
        # print(args['num2'])
        # print(args['opper'])

        if args['opper'] == "+":
            add = int(args['num1']) + int(args['num2'])
            return {'massage': add}
        elif args['opper'] == "-":
            diff = int(args['num1']) - int(args['num2'])
            return {'massage': diff}
        elif args['opper'] == "x":
            product = int(args['num1']) * int(args['num2'])
            return {'massage':product}
        elif args['opper'] == "/":
            div = int(args['num1']) / int(args['num2'])
            return {'massage':div}
        else:
            return  {'massage':"invalid opperation"}
    
    def get(self, i):
        massage = 'THIS STRING' + i +  'WAS MODEFIED IN THE APIS '
        print(i)
        print(massage)
        return {'massage': massage}
        