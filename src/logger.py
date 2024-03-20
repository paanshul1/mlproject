import logging
import os

from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
filename=LOG_FILE_PATH,
format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
level=logging.INFO
)

############################################################
#def myFunction():
#    print ('The value of __name__ is ' + __name__)
#def main():    myFunction()
#if __name__ == '__main__':    main() #https://www.freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8/
#https://www.youtube.com/watch?v=sugvnHA7ElY

#if __name__=="__main__":
#    logging.info("loggin has started")