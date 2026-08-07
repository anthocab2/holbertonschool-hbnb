from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


from app.persistence.repository_sqlalchemy import (
    SQLAlchemyRepository
)



class HBnBFacade:
    """
    Main business logic facade.
    """



    def __init__(self):

        self.user_repo = (
            SQLAlchemyRepository(User)
        )

        self.place_repo = (
            SQLAlchemyRepository(Place)
        )

        self.review_repo = (
            SQLAlchemyRepository(Review)
        )

        self.amenity_repo = (
            SQLAlchemyRepository(Amenity)
        )



    # USERS

    def create_user(
        self,
        user
    ):

        return self.user_repo.add(
            user
        )



    def get_user(
        self,
        user_id
    ):

        return self.user_repo.get(
            user_id
        )



    def get_users(self):

        return self.user_repo.get_all()



    # PLACES

    def create_place(
        self,
        place
    ):

        return self.place_repo.add(
            place
        )



    def get_places(self):

        return self.place_repo.get_all()



    def get_place(
        self,
        place_id
    ):

        return self.place_repo.get(
            place_id
        )



    # REVIEWS

    def create_review(
        self,
        review
    ):

        return self.review_repo.add(
            review
        )



    def get_reviews(self):

        return self.review_repo.get_all()



    # AMENITIES

    def create_amenity(
        self,
        amenity
    ):

        return self.amenity_repo.add(
            amenity
        )



    def get_amenities(self):

        return self.amenity_repo.get_all()
