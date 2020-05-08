#!/usr/bin/env python2.7
# -*- coding: utf-8

# @uthor: XXX
# class utulity: request DTM Oracle database
# version: 30/05/2018
# 
# rbo : 10/01/2019 adding execute_select_query2


# from config.InitConfig import *
import cx_Oracle
import sys
sys.path.append('C:\eric_python\jenkins-python\script')
#print ('\n'.join(sys.path))
from modules.configManager.ConfigManager import *


class Oracle:
    def __init__(self, mode="readonly"):
        if mode == "readonly":                
            self.oracle_config = ConfigManager.get_config_by_section_name(file_name="oracle.ini", section="oracle_readonly")
        elif mode == "admin":
            self.oracle_config = ConfigManager.get_config_by_section_name(file_name="oracle.ini", section="oracle_admin")
        self.connection = None
        self.cursor = None        
    
        
    def _connect(self):
        isconnet = False
        try:
            dsn_tns = cx_Oracle.makedsn(self.oracle_config.get('server'), self.oracle_config.get('port'), self.oracle_config.get('servicename'))            
            dsn_tns = dsn_tns.replace('SID=', 'SERVICE_NAME=')            
            self.connection = cx_Oracle.connect(user=self.oracle_config.get('user'), password=self.oracle_config.get('password'), dsn=dsn_tns)
            self.cursor = self.connection.cursor()
            isconnet = True            
        except Exception as ex:
            isconnet = False
            print("Error: during connection, cause : %s" % str(ex))
            self._close()            
        return isconnet
    
    
    def _close(self):        
        if self.cursor is not None:
            try:
                self.cursor.close()
            except Exception as ex:
                print("Error: during closing cursor, cause: %s" % ex)
        if self.connection is not None:
            try:
                self.connection.close()
            except Exception as ex:
                print("Error: during closing connection, cause: %s" % ex)
    
    
    def execute_select_query(self, request):
        res = None
        try:            
            self.cursor.execute(request)            
            res = self.cursor.fetchall()             
        except Exception as ex:                        
            raise Exception('Error: during executing Query, cause: %s' % ex)        
        return res
    
    
    def execute_select_query2(self, request):
        res = []
        try:            
            self.cursor.execute(request)           
            col_names = [row[0] for row in self.cursor.description]            
        
            for row in self.cursor.fetchall():
                res.append(dict(zip(col_names, list(row))))
                     
        except Exception as ex:                        
            raise Exception('Error: during executing Query, cause: %s' % ex)        
        return res
    
    
    def __del__(self):        
        self._close()
    
