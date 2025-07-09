from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mood_journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    mood = db.Column(db.String(20), nullable=False)
    journal = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    entries = MoodEntry.query.order_by(MoodEntry.timestamp.desc()).all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    mood = request.form['mood']
    journal = request.form['journal']
    entry = MoodEntry(mood=mood, journal=journal)
    db.session.add(entry)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run()