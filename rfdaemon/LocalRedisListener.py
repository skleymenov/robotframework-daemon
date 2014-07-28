import redis
from datetime import datetime

class LocalRedisListener:
	ROBOT_LISTENER_API_VERSION = 2
	def __init__ (self,task_id):
		self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
		self.task_id = task_id
	def start_suite (self, name, attrs):
		self.redis.hset('task:' + self.task_id, 'status', 'running')
		self.tstart = datetime.now()
		self.redis.hset('task:' + self.task_id, 'start_time', str(self.tstart))
	def end_suite (self, name, attrs):
		self.redis.hset('task:' + self.task_id, 'status', attrs['status'])
		self.tend = datetime.now()
		self.redis.hset('task:' + self.task_id, 'end_time', str(self.tend))
		self.redis.hset('task:' + self.task_id, 'duration', str(self.tend - self.tstart))

