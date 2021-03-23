from flask import Flask, render_template

from controllers.class_controller import classes_blueprint
from controllers.member_controller import members_blueprint
from controllers.room_controller import rooms_blueprint
from controllers.instructor_controller import instructors_blueprint
from controllers.schedule_controller import schedule_blueprint

app = Flask(__name__)

app.register_blueprint(classes_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(rooms_blueprint)
app.register_blueprint(instructors_blueprint)
app.register_blueprint(schedule_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)