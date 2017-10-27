# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:10:03 2017

@author: ligong

@description:这是生成训练和测试数据的程序
"""
import random
import redis
import math
import json
def process(N =1000000):
    alpha = 0.01
    beta = 1
    lambda_1 = 0.1
    lambda_2 = 1
    train_redis = redis.Redis.from_url('redis://127.0.0.1:6379/3')
    predict_redis = redis.Redis.from_url('redis://127.0.0.1:6379/4')
    T = 10
    for i in range(N):
        x = random.random()
        dd = {}
        for j in range(T):
            dd['key_%s' % j] = pow(x,j)
        y = 1 if math.sin(x) > 0.5 else 0
        job = {'alpha':alpha,'beta':beta,'lambda_1':lambda_1,'lambda_2':lambda_2,'label':y,'data':dd}
        job_str = json.dumps(job)
        if random.random() > 0.7:
            predict_redis.rpush('PREDICT_JOB_QUEUE',job_str)
        else:
            train_redis.rpush('TRAIN_JOB_QUEUE',job_str)
            
if __name__ == '__main__':
    process()
