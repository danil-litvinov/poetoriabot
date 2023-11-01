from typing import Optional

from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import Users
from infrastructure.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def get_or_create_user(
        self,
        user_id: int,
        full_name: str,
        language: str,
        reg_date: int,
        upd_date: int,
        username: Optional[str] = None,
        phone: Optional[str] = None,
    ):
        """
        Creates or updates a new user in the database and returns the user object.
        :param user_id: The user's ID.
        :param full_name: The user's full name.
        :param language: The user's language.
        :param username: The user's username. It's an optional parameter.
        :return: User object, None if there was an error while making a transaction.
        'redis://:19581964@localhost:6379/0'
        """
        insert_stmt = (
            insert(Users)
            .values(
                user_id=user_id,
                username=username,
                full_name=full_name,
                language=language,
                reg_date=reg_date,
                upd_date=upd_date,
                phone=phone,
            )
            .on_conflict_do_update(
                index_elements=[Users.user_id],
                set_=dict(
                    username=username,
                    full_name=full_name,
                    upd_date=upd_date,
                    phone=phone,
                ),
            )
            .returning(Users)
        )
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one()
