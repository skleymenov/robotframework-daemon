import subprocess
import os
import redis
from flask import Flask, g, request, render_template
app = Flask(__name__)

WAT_TIME = 20

def request_wants_json():
	best = request.accept_mimetypes \
			.best_match(['application/json', 'text/html'])
	return best == 'application/json' and \
			request.accept_mimetypes[best] > request.accept_mimetypes['text/html']

def connect_db():
	"""Connects to the specific database"""
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	return r

def get_db():
	"""Opens a new database connection if there is none yet for the current application context."""
	if not hasattr(g, 'redis_db'):
		g.redis_db = connect_db()
	return g.redis_db

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/suites')
def list_suites():
	files = os.listdir('/var/lib/rfdaemon/suites')
	if request_wants_json():
		suites_json = '{'
		for f in files:
			suites_json = suites_json + '"' + f +'",'
		suites_json = suites_json + '}'
		return suites_json
	return render_template('suites.html', suites = files)

@app.route('/suites/__version')
def get_version():
	version_json = subprocess.Popen(['git', '-p', 'log', '-n1', '--pretty={"%H":{"author":"%aN <%aE>","date":"%aD","title":"%s"}}'],
			cwd='/var/lib/rfdaemon/suites',stdout=subprocess.PIPE).communicate()[0]
	return version_json

@app.route('/suites/<suite>/run',methods=['PUT'])
def run_suite(suite):
	r = get_db()
	task_id = r.incr('tasks')
	task_data = { 'suite' : suite, 'status' : 'queued'}
	r.hmset('task:%s' % task_id, task_data)
	task_pid = subprocess.Popen(['pybot','--listener', '/root/ta-rfdaemon/LocalRedisListener.py:%s' % task_id, suite + '.html'], cwd = '/var/lib/rfdaemon/suites').pid
	r.hset('task:%s' % task_id, 'pid', task_pid)

	return 'Task created - %s' % suite, 202

@app.route('/tasks')
def task_list():
	r = get_db()
	tids = r.keys('task:*')
	tasks = map(r.hgetall, tids)


	return render_template('tasks.html', tasks = tasks)




if __name__ == '__main__':
	app.run()


