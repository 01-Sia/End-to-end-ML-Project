import sys 
''' Imagine you’re driving and your GPS alerts you to a wrong turn instead of 
letting you get lost. 
Similarly, custom exceptions provide clear guidance when something goes wrong.
'''

def error_message(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  
    ''' first blank = type or error -value , type etc .. , 2 blank = actual exception instance 
     exc_tb = the trceback object '''
    file_name = exc_tb.tb_frame.f_code.co_filename
    message = "Error occured in python script [{0}], line number [{1}], and giving the error [{2}]".format(file_name,exc_tb.tb_lineno, str(error))
    return message 



class CustomException(Exception):       
    '''here we call the exception as base class for 
    importing the built -in exception functionalities.'''

    def __init__(self,message,error_detail:sys):
        super().__init__(message)
        self.message = error_message(message, error_detail=error_detail)


    def __str__(self):
        return self.message
