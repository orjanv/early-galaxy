#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple command-line tool for posting to Blogger.

Usage:
  $ python blogger.py --title "TITLE" --labels "label1, label2" --src SOURCEFILE 
"""

from __future__ import print_function
from oauth2client import client
from googleapiclient import sample_tools
import sys, argparse

# The blog id we are posting to
myblogid = 8032756911295504398

def main(argv):
    # Set up the optional and required arguments for posting to blogger
    parent = argparse.ArgumentParser(add_help=False, conflict_handler='resolve')
    group = parent.add_argument_group('standard')
    parent.add_argument("-t", "--title", help="Title for the blog post", required = True)
    parent.add_argument("-l", "--labels", help="Labels for the blog post")
    parent.add_argument("-s", "--src", help="Sourcefile for the blog post content", required = True)
    args = parent.parse_args()

    # Assign argument values to variables
    flags = parent.parse_args(argv[1:])
    blogtitle = flags.title
    blogtags = flags.labels
    blogfilename = flags.src
    
    try:
        with open(blogfilename, 'r') as f:
            blogcontent = f.read()
        f.close()
    except:
        print("Sourcefile not found.")
        exit(1)
    
    # Authenticate and construct service, also inclue argparse arguments
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger',
        parents=[parent])
    try:
        # Make the POST request
        posts = service.posts()
        request = posts.insert(blogId=myblogid, body=
            {"kind": "blogger#post", 
            "blog": {"id": myblogid}, 
            "title": blogtitle, 
            "labels": blogtags,
            "content": blogcontent})
        response = request.execute()
        print ('Posted: %s (%s)' % (response['title'], response['url']))

    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run'
            'the application to re-authorize')

if __name__ == '__main__':
    main(sys.argv)
