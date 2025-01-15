from typing import Optional
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from app import db

 
class Course(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    coursenum : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(4), index = True)   

    def __repr__(self):
        return '<Course id: {} - coursenum: {}>'.format(self.id,self.coursenum)

