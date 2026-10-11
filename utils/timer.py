import time
from core.logger import logger
import functools
import inspect


def time_logger(func):
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start=time.time()
            result=await func(*args, **kwargs)
            end=time.time()
            logger.info(f'{func.__name__} took {end-start:.4f}seconds')
            return result
        return async_wrapper

    else:
        @functools.wraps(func)  
        def sync_wrapper(*args,**kwargs):
            start=time.time()
            result=func(*args, **kwargs)
            end=time.time()
            logger.info(f'{func.__name__} took {end-start:.4f}seconds')
            return result
        return sync_wrapper
    
    