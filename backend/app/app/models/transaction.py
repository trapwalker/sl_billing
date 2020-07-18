from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .wallet import Wallet  # noqa: F401


class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, index=True)
    value = Column(DECIMAL, default=0, nullable=False)

    src_wallet_id = Column(Integer, ForeignKey("wallet.id"))
    dst_wallet_id = Column(Integer, ForeignKey("wallet.id"))
    src_wallet = relationship("Wallet", back_populates="tx_transactions")
    dst_wallet = relationship("Wallet", back_populates="rx_transactions")
