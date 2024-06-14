from fastapi import APIRouter, HTTPException, status
from models.blog_posts import BlogPost
from models.schemas import BlogPostRequest, BlogPostUpdateRequest

from typing import List

import logging

LOGGER = logging.getLogger(__name__)

blog_posts = []

router = APIRouter(tags=['blog'])

class BlogPost:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
    def __str__(self) -> str:
        return f'{self.id} - {self.title} - {self.content}'
    
    def toJson(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}


@router.post("/")
def create_blog_post(blog_post: BlogPostRequest, status_code=status.HTTP_201_CREATED):
    LOGGER.info({'message':'Creating post', 'post':blog_post, 'status':'success', 'method':'POST', 'url':'/blog'})
    try: 
        post = BlogPost(id=blog_post.id, title=blog_post.title, content=blog_post.content)
        blog_posts.append(post)
        return {'status':'success'}
    
    except KeyError:
        LOGGER.warning({'message':'Invalid request', 'status':'error', 'method':'POST', 'url':'/blog'})
        raise HTTPException(status_code=400, detail='Invalid request')
    
    except Exception as e:
        LOGGER.error({'message':'Error creating post', 'status':'error', 'method':'POST', 'url':'/blog', 'error':str(e)})
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/")
def get_blog_posts():
    LOGGER.info({'message':'Getting posts', 'status':'success', 'method':'GET', 'url':'/blog'})
    LOGGER.debug(msg=f'Posts: {blog_posts}')
    return [post.toJson() for post in blog_posts]

@router.get("/{id}")
def get_blog_post(id: int):
    LOGGER.info({'message':'Getting post', 'id':id, 'status':'success', 'method':'GET', 'url':'/blog'})
    for post in blog_posts:
        if post.id == id:
            return post.toJson()
    LOGGER.warning({'message':'Post not found', 'id':id, 'status':'error', 'method':'GET', 'url':'/blog'})
    raise HTTPException(status_code=404, detail='Post not found')

@router.delete("/{id}")
def delete_blog_post(id: int):
    
    for index, post in enumerate(blog_posts):
        if post.id == id:
            blog_posts.pop(index)
            return {'status':'success'}
    LOGGER.warning({'message':'Post not found', 'id':id, 'status':'error', 'method':'DELETE', 'url':'/blog'})
    raise HTTPException(status_code=404, detail='Post not found')

@router.put("/{id}")
def update_blog_post(id: int, blog_post: BlogPostUpdateRequest):
    try: 
        LOGGER.info({'message':'Updating post', 'id':id, 'status':'success', 'method':'PUT', 'url':'/blog'})
        LOGGER.debug(msg=f'Updated post: {blog_post}')
        for post in blog_posts:
            if post.id == id:
                post.title = blog_post.title
                post.content = blog_post.content
                return {'status':'success'}
    except KeyError:
        LOGGER.warning({'message':'Invalid request', 'status':'error', 'method':'PUT', 'url':'/blog'})
        raise HTTPException(status_code=400, detail='Invalid request')
    except Exception as e:
        LOGGER.error({'message':'Error updating post', 'id':id, 'status':'error', 'method':'PUT', 'url':'/blog', 'error':str(e)})
        raise HTTPException(status_code=500, detail=str(e))
    