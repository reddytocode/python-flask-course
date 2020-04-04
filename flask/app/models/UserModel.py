from ..db.db_extension import db


class UserModel(db.Document):
    username = db.StringField()
    password = db.StringField()
    
    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter(cls.username == username).first()
        return user

    @classmethod
    def register(cls, username, password):
        try:
            user_with_id_exist = cls.find_by_username(username)
            if user_with_id_exist:
                return 401
            user = UserModel(
                username = username, 
                password = password
                )
            user.save()
            return 200
        except Exception as e:
            print(e)
            return 401