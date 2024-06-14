import pydantic

class BlogPostRequest(pydantic.BaseModel):
    id: int
    title: str
    content: str
    
class BlogPostUpdateRequest(pydantic.BaseModel):
    title: str
    content: str