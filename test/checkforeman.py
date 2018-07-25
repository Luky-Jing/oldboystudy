#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18年2月1日 上午9:22
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : testforeman.py
# @Software: PyCharm

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, VARCHAR, BigInteger, DateTime
import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import time
import datetime

engine = create_engine("mysql+pymysql://test:123qwe@114.67.228.26/puppet_foreman",
                       encoding='utf-8',
                       echo=True)

Base = declarative_base()

class Messages(Base):
    __tablename__ = 'messages'
    id = Column(BigInteger, primary_key=True)
    value = Column(Text)
    digest = Column(VARCHAR)

    def __repr__(self):
        return "<Messages(id='%s',value='%s',digest='%s')>" %(self.id, self.value, self.digest)

class Sources(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    value = Column(Text)
    digest = Column(VARCHAR)

    def __repr__(self):
        return "<Sources(id='%s',value='%s',digest='%s')>" %(self.id, self.value, self.digest)
class Hosts(Base):
    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    last_compile = Column(DateTime)
    last_report = Column(DateTime)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)
    root_pass = Column(VARCHAR)
    architecture_id = Column(Integer)
    operatingsystem_id = Column(Integer)
    environment_id = Column(Integer)
    ptable_id = Column(Integer)
    medium_id = Column(Integer)
    build = Column(Integer)
    comment = Column(Text)
    disk = Column(Text)
    installed_at = Column(DateTime)
    model_id = Column(Integer)
    hostgroup_id = Column(Integer)
    owner_id = Column(Integer)
    owner_type = Column(VARCHAR)
    enabled = Column(Integer)
    puppet_ca_proxy_id = Column(Integer)
    managed = Column(Integer)
    use_image = Column(Integer)
    image_file = Column(VARCHAR)
    uuid = Column(VARCHAR)
    compute_resource_id = Column(Integer)
    puppet_proxy_id = Column(Integer)
    certname = Column(VARCHAR)
    image_id = Column(Integer)
    organization_id = Column(Integer)
    location_id = Column(Integer)
    type = Column(VARCHAR)
    otp = Column(VARCHAR)
    realm_id = Column(Integer)
    compute_profile_id = Column(Integer)
    provision_method = Column(VARCHAR)
    grub_pass = Column(VARCHAR)
    global_status = Column(Integer)
    lookup_value_matcher = Column(VARCHAR)
    pxe_loader = Column(VARCHAR)

class Reports(Base):
    __tablename__ = 'reports'
    id = Column(BigInteger, primary_key=True)
    host_id = Column(Integer, ForeignKey('hosts.id'))
    reported_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(BigInteger)
    metrics = Column(Text)
    type = Column(VARCHAR)

    host = relationship("Hosts", backref='reports')

    def __repr__(self):
        return "<Reports(id='%s',host_id='%s',status='%s')>" %(self.id, self.host_id, self.status)

class Logs(Base):
    __tablename__ = 'logs'
    id = Column(BigInteger, primary_key=True)
    source_id = Column(Integer, ForeignKey('sources.id'))
    message_id = Column(Integer, ForeignKey('messages.id'))
    report_id = Column(Integer, ForeignKey('reports.id'))
    level_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    source = relationship("Sources", backref='log')
    message = relationship("Messages", backref='log')
    report = relationship("Reports", backref='log')

    def __repr__(self):
        return "<Logs(source_id='%s',message_id='%s',report_id='%s',level_id='%s',updated_at='%s')" %(self.source_id,
                                                                                                      self.message_id,
                                                                                                      self.report_id,
                                                                                                      self.level_id,
                                                                                                      self.updated_at)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

nowdate = datetime.datetime.now()
checkdate = nowdate - datetime.timedelta(hours=1)

# 查错误的日志
log_objs = Session.query(Logs.source_id, Logs.message_id, Logs.report_id, Logs.level_id, Logs.updated_at)\
    .filter(Logs.level_id == 4).filter(Logs.updated_at >= checkdate).all()
#log_objs = Session.query(Logs.source_id, Logs.message_id, Logs.report_id, Logs.level_id, Logs.updated_at)\
    .filter(Logs.level_id == 4).all()
# print(log_objs)

# 查报错内容
message_objs = Session.query(Messages.value, Messages.digest).all()
# print(message_objs)

# 查规则
source_objs = Session.query(Sources.value, Sources.digest).all()
# print(source_objs)

#
reports_objs = Session.query(Reports.host_id, Reports.reported_at, Reports.created_at, Reports.updated_at,
                             Reports.status, Reports.metrics, Reports.type).all()
# print(reports_objs)

hosts_objs = Session.query(Hosts.name, Hosts.last_report).all()
# print(hosts_objs)

print("查询超时的主机")
for host in hosts_objs:
    hostlasttime = host[1]
    if (nowdate-hostlasttime).seconds >= 3600:
        print(host[0]+" 超时")

print("查询错误的主机")
result=""
for log in log_objs:
    source = Session.query(Sources).filter_by(id=log[0]).first()
    message = Session.query(Messages).filter_by(id=log[1]).first()
    report = Session.query(Reports).filter_by(id=log[2]).first()
    host = Session.query(Hosts).filter_by(id=report.host_id).first()
    result = "错误主机为：" + host.name + "\n错误规则为：" + source.value + "\n报错信息为：" + message.value + "\n"
    print(result)
