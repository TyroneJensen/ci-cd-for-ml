import datetime

def main():
  print('Hello world! with env variables')

  current_time = datetime.datetime.now()
  print(f'Current time: {current_time}')

if __name__ == "__main__":
  main()
