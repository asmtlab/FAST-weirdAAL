'''
This file is used to list volumes of ec2 instances
'''

import boto3
import botocore

import json
import urllib
import logging
import sys,os
import pprint

pp = pprint.PrettyPrinter(indent=5, width=80)

from ec2.ec2 import *

#insert AWS key, will figure out how to pull this in from a single file for all scripts

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''


get_instance_volume_details(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
get_instance_volume_details2(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)