from domain.user import User
from driven.api_rest.v1.bitbucket.models import UserResponse


class BitbucketMapper:

    @staticmethod
    def to_user_domain(user: UserResponse) -> User:
        return User(name=user.display_name, bitbucket_id=user.uuid)
