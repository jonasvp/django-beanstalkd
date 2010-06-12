"""
Example Beanstalk Job File.
Needs to be called beanstalk_jobs.py and reside inside a registered Django app.
"""
import os
import time

from django_beanstalkd import beanstalk_job


@beanstalk_job
def background_counting(arg):
    """
    Do some incredibly useful counting to the value of arg
    """
    value = int(arg)
    pid = os.getpid()
    print "[%s] Counting from 1 to %d." % (pid, value)
    for i in range(1, value+1):
        print '[%s] %d' % (pid, i)
        time.sleep(1)
