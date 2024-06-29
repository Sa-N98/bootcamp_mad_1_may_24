from flask import request, render_template as rt , redirect , url_for
from model import *

def router (app):
    @app.route('/', methods=['GET','POST'])
    def home():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            
            user_data = users.query.filter(users.email == email).first()
            print(user_data.username, user_data.email, user_data.password)
            print()
            if user_data:
                if user_data.password == password:
                    
                    if user_data.user_type == 'consumers':
                        global current_userID
                        current_userID = user_data.id
                        return redirect(url_for('user_dashbord'))

                    if user_data.user_type == 'artist':
                        print('hit')
                        return redirect(url_for('artist_dashbord'))
                return rt('home.html', massage= "Wrong email or password")
        return rt('home.html')


    @app.route('/signup', methods=['GET','POST'])
    def signup():
        if request.method == 'POST':

            if request.form['type'] == 'artist':
                if not users.query.filter(users.email == request.form['email']).all():
                    newUser = users(username = request.form['username'], email = request.form['email'] , password = request.form['password'], user_type = request.form['type']) 
                    db.session.add(newUser)
                    db.session.commit()           


            if request.form['type'] == 'consumers':
                if not users.query.filter(users.email == request.form['email']).all():
                    newUser = users(username = request.form['username'], email = request.form['email'] , password = request.form['password'], user_type = request.form['type'])
                    db.session.add(newUser)
                    db.session.commit()
                
        return rt('signup.html')


    @app.route('/user_dashbord', methods=['GET'])
    def user_dashbord():
        return rt('userDashbord.html')

    @app.route('/search', methods=['GET', 'POST'])
    def search():
        if request.method == 'POST':
            search_tag = request.form['search_tag']
            query = request.form['search_query']
            if search_tag == 'Song':
                data = songs.query.filter(songs.name.like('%'+query+'%')).all()
                return rt('results.html', search_data = data, userID= current_userID)
            elif search_tag == 'Artist':
                data = songs.query.filter(songs.artist.like('%'+query+'%')).all()
                return rt('results.html', search_data = data, userID= current_userID)
            elif search_tag == 'Album':
                data = songs.query.filter(songs.album.like('%'+query+'%')).all()
                return rt('results.html', search_data = data, userID= current_userID)
        return 'search'




    @app.route('/artist_dashbord', methods=['GET'])
    def artist_dashbord():
        return rt("artistDashbort.html")



    @app.route('/test', methods=['GET', 'POST'])
    def test():
        return rt('apitesting.html')
