import subprocess

PASSWORD = "admin123"

def get_user(user_id):
      query = "SELECT * FROM users WHERE id = " + user_id
      return query

def run(cmd):
      subprocess.call(cmd, shell=True)

def read_file(path):
      f = open(path)
      return f.read()

def unused():
      x = 1

try:
      run("ls")
  except:
    pass
