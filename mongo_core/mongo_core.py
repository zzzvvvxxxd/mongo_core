#! /usr/bin/env python2.7
# coding=utf-8
__author__ = 'bulu_dog'

# import area
import datetime
import re
from pymongo import MongoClient
from pymongo import ReturnDocument
from dispatch import dispatch

'''
Mongo类
版本：2015/06/22
建立连接，主要用于获取指定数据库内特定的collection
'''
class Mongo(object):
    def __init__(self, name, host="localhost", port=27017):
        """
        init
        :param name: db name
        :param host: db host
        :param port: db port
        """
        self.db = None
        self.name = name
        self.host = host
        self.port = port
        self.client = None
        self.initConnection(host, port)
        self.initDataBase()

    # get connection with MongoClient
    def initConnection(self, host="localhost", port=27017):
        self.client = MongoClient(host, port)
        # return self.client

	# get database with db name
    def initDataBase(self):
        self.db = self.client[self.name]

    # get collection by name
    def getCollection(self, cname):
        return self.db[cname]

    def close(self):
        self.client.close()