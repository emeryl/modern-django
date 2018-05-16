from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='wyqnr0mgkn_c4!4g)mii54_0ja1z1iy=ki_=x1tvcqaxl(@=c+')

DEBUG = env.bool('DJANGO_DEBUG', True)
