import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("/Users/justinschuldt/code/python-testing/rounds-cd2e7-firebase-adminsdk-fkm4q-ca25076cc6.json")
firebase_admin.initialize_app(cred)

def main():
  print('hello world')
  def listener(event):
    print(event.event_type)  # can be 'put' or 'patch'
    print(event.path)  # relative to the reference, it seems
    print(event.data)  # new data at /reference/event.path. None if deleted
  
  db.reference('/games/one', url='https://rounds-cd2e7.firebaseio.com').listen(listener)

if __name__ == '__main__':
  main()
