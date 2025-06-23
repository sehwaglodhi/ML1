import sys
import logging
import logger

# Step 1: Error message formatter
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Step 2: Custom Exception Class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        logging.error(self.error_message)  # 👈 This logs the formatted error

    def __str__(self):
        return self.error_message

# Step 3: Trigger exception to test
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero occurred")
        raise CustomException(e, sys)

