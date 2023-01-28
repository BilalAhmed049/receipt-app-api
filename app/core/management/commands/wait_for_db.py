"""
Djando command wait for t he database to be available
"""
from django.core.management.base import BaseCommand
import time
from django.db.utils import OperationalError
from psycopg2 import OperationalError as psycopg2Error

class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self,*args,**options):
        pass