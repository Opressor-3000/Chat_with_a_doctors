


git checkout yusif 
&& 
git add . && git commit -m 'install pydantic-settings' 
&& 
git push origin yusif 
&& 
git checkout dev && git merge origin yusif && git checkout yusif 

run server 

uvicorn main:app --reload 


class Person(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('person.id', ondelete='RESTRICT'))
    parent    = db.relationship('Person', remote_side=[id], back_populates='children')
    children  = db.relationship('Person', back_populates='parent', passive_deletes='all')


    # is_active:Mapped[bool] = mapped_column(Boolean, default=True, server_default=True)


from sqlalchemy import CheckConstraint, func, String
from sqlalchemy.event import listen_for
from sqlalchemy.orm import mapper

@listens_for(mapper, "instrument_class")
def add_string_length_constraint(mapper, cls):
    table = cls.__table__

    for column in table.columns:
        if isinstance(column.type, String):
            length = column.type.length

            if length is not None:
                CheckConstraint(
                    func.length(column) <= length,
                    table=column,
                    _autoattach=False,
                )
