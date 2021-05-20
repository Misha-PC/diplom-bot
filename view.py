# from models import User


def get_sites(user_id):
    pages = Site.query.filter(Site.member_id == user_id).all()
    print(pages)
    print(type(pages))
