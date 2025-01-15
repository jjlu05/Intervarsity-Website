from app import app, db
from app.models import Course
import sqlalchemy as sa
import sqlalchemy.orm as so

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'Course': Course }

# We will use the following major data in later videos. 
majors = [{'name':'CS','department':'Computer Science'},
          {'name':'DS','department':'Computer Science'},
          {'name':'RBE','department':'Robotics Engineering'},
          {'name':'ME','department':'Mechanical Engineering'}, 
          {'name':'MATH','department': 'Mathematics'}  ]

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

    