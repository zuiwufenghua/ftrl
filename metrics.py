# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:23:29 2017

@author: admin
"""
import redis
from sklearn import metrics

if __name__ == '__main__':
    predictjob_redis_conn = redis.Redis.from_url('redis://127.0.0.1:6379/4')
    y,y_test = [],[]
    for item in predictjob_redis_conn.lrange('AUC_CACHE',0,-1):
        try:
            t = eval(item)
        except:
            continue
        y.append(t[0])
        y_test.append(t[1])

    tmp = map(lambda _:1 if _ > 0.5 else 0 ,list(y_test))
    precision = metrics.precision_score(y, tmp)  
    recall = metrics.recall_score(y, tmp) 
    print 'precision:',precision
    print 'recall:',recall
    print 'f1:', 2.0/(1.0/precision+1.0/recall)
    print 'auc:',metrics.roc_auc_score(y,y_test)
