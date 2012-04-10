from django.template import Library
import urllib
import simplejson

register = Library()

@register.simple_tag
def twitter_status( username ):
    url = "http://twitter.com/statuses/user_timeline/%s.json?count=1" % username
    file  = urllib.urlopen(url)
    json_responce = file.read()
    twit = simplejson.loads(json_responce)
    return "%s" % twit[0]["text"]