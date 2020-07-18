from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .transaction import Transaction  # noqa: F401


class Wallet(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="wallets")

    currency = Column(String, default='USD', nullable=False)
    value = Column(DECIMAL, default=0, nullable=False)

    tx_transactions = relationship("Transaction", back_populates="src_wallet")
    rx_transactions = relationship("Transaction", back_populates="dst_wallet")
