from app.extensions import db

from app.persistence.repository import Repository



class SQLAlchemyRepository(Repository):
    """
    SQLAlchemy repository implementation.
    """


    def __init__(self, model):
        self.model = model



    def add(self, obj):

        db.session.add(obj)

        db.session.commit()

        return obj



    def get(self, obj_id):

        return self.model.query.get(
            obj_id
        )



    def get_all(self):

        return self.model.query.all()



    def update(self, obj_id, data):

        obj = self.get(obj_id)


        if not obj:
            return None


        for key, value in data.items():

            setattr(
                obj,
                key,
                value
            )


        db.session.commit()


        return obj



    def delete(self, obj_id):

        obj = self.get(obj_id)


        if not obj:
            return False


        db.session.delete(obj)

        db.session.commit()


        return True
