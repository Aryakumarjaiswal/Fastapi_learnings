from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Custom exception class
class MyCustomException(Exception):
    def __init__(self, message: str):
        self.message = message

# Custom exception handler that returns a string
@app.exception_handler(MyCustomException)
async def custom_exception_handler(request: Request, exc: MyCustomException):
    # Return a string message using PlainTextResponse
    return PlainTextResponse(content=exc.message, status_code=400)

# Endpoint to trigger the custom exception
@app.get("/trigger-error")
def trigger_error():
    raise MyCustomException("This is a custom error message returned as a string.")

