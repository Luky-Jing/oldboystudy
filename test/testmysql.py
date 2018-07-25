#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18年1月31日 上午9:29
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : testforeman.py
# @Software: PyCharm

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# 连接数据库
engine = create_engine("mysql+pymysql://test:123qwe@114.67.228.26/test", encoding='utf-8', echo=True)

Base = declarative_base()
# 创建表
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    # 为了下面print(my_user)，否则输出的是地址
    def __repr__(self):
        return "<User(name='%s', password='%s')>" %(self.name, self.password)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", backref='addresses')

    def __repr__(self):
        return "<Address(email_address='%s')>" %self.email_address

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address")
    shipping_address = relationship("Addresss")

Base.metadata.create_all(engine)

# 创建与数据库会话，返回的是一个class
Session_class = sessionmaker(bind=engine)
# 生成session实例
Session = Session_class()

# 添加
user_obj = User(name="li", password="123")
print(user_obj.name, user_obj.id)

Session.add(user_obj)
print(user_obj.name, user_obj.id)

address_obj = Address(email_address='623620767@qq.com',user_id='1')
print(address_obj.email_address, address_obj.user_id)

Session.add(address_obj)
print(address_obj.email_address, address_obj.user_id)
# 提交
Session.commit()

# 查询
my_user = Session.query(User).filter_by(name='li').first()
print(my_user)
print(my_user.id, my_user.name, my_user.password)

# 修改
my_user = Session.query(User).filter_by(name='li').first()
my_user.name = 'lipeijing'
Session.commit()
# ---------验证修改---------
my_user = Session.query(User).filter_by(name='lipeijing').first()
print(my_user)
print(my_user.id, my_user.name, my_user.password)

# 回滚
my_user = Session.query(User).filter_by(name='lipeijing').first()
my_user.password = 'aaa'
Session.rollback()
# ---------验证回滚---------
my_user = Session.query(User).filter_by(name='lipeijing').first()
print(my_user)
print(my_user.id, my_user.name, my_user.password)

# 获取全部数据
print(Session.query(User.name, User.id).all())

# 多条件查询
objs = Session.query(User).filter(User.id>1).filter(User.id<4).all()
print(objs)

# 统计和分组
count = Session.query(User).filter(User.name.like("li")).count()
print(count)

from sqlalchemy import func
print(Session.query(func.count(User.name), User.name).group_by(User.name).all())

# 外联关联
obj = Session.query(User).first()
for i in obj.addresses:
    print(i)

addr_obj = Session.query(Address).first()
print(addr_obj.user.name)

# 创建关联对象
obj = Session.query(User).filter(User.name=='li').all()[0]
print(obj.addresses)

obj.addresses = [Address(email_address='18434361814@163.com'),
                 Address(email_address='11111111111@163.com')]

Session.commit()

# 多外键关联
