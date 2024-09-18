from sqlalchemy import (Column, String, Integer, ForeignKey)
from models.models import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer(), primary_key = True)
    acc_number = Column(Integer())
    acc_type = Column(String())
    balance = Column(Integer())
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    def __repr__(self):
        return f'Account(id={self.id}, ' + \
            f'acc_number={self.acc_number}, ' + \
            f'acc_type={self.acc_type}, ' + \
            f'balance={self.balance}, ' + \
            f'customer_id={self.customer_id})'