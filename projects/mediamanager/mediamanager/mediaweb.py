"""
Module d'illustratin d'une interface web.
"""

from flask import Flask, render_template, request, redirect
from mediamanager import media_db
from mediamanager import conf

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('media_home.html')


@app.route('/shows/', methods=['GET', 'POST'])
def index_show():
    if request.method == "POST":
        show_title = request.form['new_show']
        media_db.TvShow(show_title, conf.SQLITE_PATH)
        return redirect("/shows/")

    else:
        _MY_SHOWS = media_db.MediaDao()
        _MY_SHOWS.get_shows()
        return render_template('series.html', series=_MY_SHOWS.get_shows())


@app.route('/show/<show_name>')
def view_show_details(show_name):
    show_name = show_name.replace('_', ' ')
    selected_show = media_db.TvShow(show_name, conf.SQLITE_PATH)
    return render_template('show_detail.html', title=selected_show.name,
                           episodes=selected_show.get_episodes())

@app.route('/show/<show_name>/new_episode/')
def add_episode(show_name):
    return render_template('show_add.html', title=show_name)

@app.route('/show/<show_name>/episodes/', methods=['GET', 'POST'])
def episode(show_name):
    show_name = show_name.replace('_', ' ')

    selected_show = media_db.TvShow(show_name, conf.SQLITE_PATH)

    if request.method == 'POST':
        episode_title = request.form['episode_title']
        episode_number = request.form['episode_number']
        episode_season = request.form['season_number']
        selected_show.add_episode(episode_title, episode_number, episode_season)
        return redirect(f"/show/{show_name}")
    else:
        return render_template('show_detail.html', title=selected_show.name,
                               episodes=selected_show.get_episodes())


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

if __name__ == '__main__':
    app.run()
