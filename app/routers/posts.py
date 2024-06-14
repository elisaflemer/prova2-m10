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
    LOGGER.info({'message':'Creating post', 'post':blog_post, 'status_code':status_code, 'status':'success', 'method':'POST', 'url':'/blog'})
    try: 
        post = BlogPost(id=blog_post.id, title=blog_post.title, content=blog_post.content)
        blog_posts.append(post)
        return {'status':'success'}
    
    except KeyError:
        LOGGER.warning(msg='Invalid request')
        raise HTTPException(status_code=400, detail='Invalid request')
    
    except Exception as e:
        LOGGER.error(msg=f'Error creating post: {str(e)}')
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/")
def get_blog_posts():
    LOGGER.info(msg='Getting all blog posts')
    LOGGER.debug(msg=f'Posts: {blog_posts}')
    return [post.toJson() for post in blog_posts]

@router.get("/{id}")
def get_blog_post(id: int):
    LOGGER.info(msg=f'Getting post with id: {id}')
    for post in blog_posts:
        if post.id == id:
            return post.toJson()
    LOGGER.warning(msg='Post not found')
    raise HTTPException(status_code=404, detail='Post not found')

@router.delete("/{id}")
def delete_blog_post(id: int):
    
    for index, post in enumerate(blog_posts):
        if post.id == id:
            blog_posts.pop(index)
            return {'status':'success'}
    LOGGER.warning(msg='Post not found')
    raise HTTPException(status_code=404, detail='Post not found')

@router.put("/{id}")
def update_blog_post(id: int, blog_post: BlogPostUpdateRequest):
    try: 
        LOGGER.info(msg=f'Updating post with id: {id}')
        LOGGER.debug(msg=f'Updated post: {blog_post}')
        for post in blog_posts:
            if post.id == id:
                post.title = blog_post.title
                post.content = blog_post.content
                return {'status':'success'}
    except KeyError:
        LOGGER.warning(msg='Invalid request')
        raise HTTPException(status_code=400, detail='Invalid request')
    except Exception as e:
        LOGGER.error(msg=f'Error updating post: {str(e)}')
        raise HTTPException(status_code=500, detail=str(e))
    