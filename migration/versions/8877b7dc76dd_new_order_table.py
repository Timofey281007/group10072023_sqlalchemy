"""new Order table

Revision ID: 8877b7dc76dd
Revises: 2f08f5d8ed02
Create Date: 2023-08-31 16:34:58.755365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8877b7dc76dd'
down_revision: Union[str, None] = '2f08f5d8ed02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
