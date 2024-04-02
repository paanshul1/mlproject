import sys              
import logging
from src.logger import logging
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_frame.f_lineno,str(error)
    
    )
    return error_message



class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


#######################################
    
#if __name__=="__main__":
#    try:
#        a=1/0
#    except Exception as e:
        #logger.logging("divide by zero has been reported")
#        logging.info("divide by zero has been reported")
 #       raise CustomException (e,sys)
    


#    Here, we have overridden the constructor of the Exception class to accept our own custom arguments salary and message.

#Then, the constructor of the parent Exception class is called manually with the self.message argument using super().

#The custom self.salary attribute is defined to be used later.

#The inherited __str__ method of the Exception class is then used to display the corresponding message when SalaryNotInRangeError is raised.