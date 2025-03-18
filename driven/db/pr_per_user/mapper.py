from domain.user import User
from driven.api_rest.v1.rudo.models import UserRudoResponse


class DBPullRequestMapper:
    @staticmethod
    def to_user_domain(user: UserRudoResponse) -> User:
        return User(name=user.display_name, email=user.email)
