#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine,text,update
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:123456@127.0.0.1:3306/shipman',max_overfow=5)
Base = declarative_base()

class UserDB(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    node_ip = Column(String(32))


class NodeDB(Base):
    __tablename__ = 'node'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    node_ip = Column(String(32))
    port = Column(String(32))
    cpus = Column(String(32))
    mem = Column(String(32))
    images = Column(String(32))
    state = Column(String(32))
    node_group = Column(String(32))
    containers = Column(String(32))
    os_version = Column(String(32))
    docker_version = Column(String(32))

class ConUsageDB(Base):
    __tablename__ = 'con_usage'
    id = Column(Integer,primary_key=True)
    con_id = Column(Integer)
    con_addr = Column(String(32))
    node_ip = Column(String(32))
    username = Column(String(32))
    con_app = Column(String(32))
    con_desc = Column(String(256))











