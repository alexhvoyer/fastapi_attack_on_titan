from fastapi.exceptions import HTTPException

def create_404_error(detail = "NotFound"):
    return HTTPException(status_code=404, detail=detail)