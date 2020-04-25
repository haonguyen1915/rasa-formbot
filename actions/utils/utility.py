import collections
import numbers
import urllib.request as urlreq
import urllib.parse
import os
import re
from typing import Dict, Text, List, Optional, Set, Tuple
import aiohttp

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher


def utter_wrong_cuisine(dispatcher: CollectingDispatcher, value: Text, *args):
    method = "template"

    if method == "text":
        dispatcher.utter_message(f"cuisine type: {value} is not in the database, please try again")
    elif method == "json":
        dispatcher.utter_message(json_message={
            "text": f"cuisine type: {value} is not in the database, please try again",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Sai hết rồi!",
                    "payload": '/query_knowledge_base{"object_type": null}',
                }
            ],
        })
    elif method == "elements":
        product_list_template = [{"text": f"cuisine type: {value} is not in the database, please try again"}]
        dispatcher.utter_message(elements=product_list_template)
    elif method == "template":
        print(f"test method: {method}")
        dispatcher.utter_message(template="utter_wrong_cuisine_")


def utter_wrong_num_people(dispatcher: CollectingDispatcher):
    dispatcher.utter_message(template="utter_wrong_num_people")


def utter_wrong_outdoor_seating(dispatcher: CollectingDispatcher):
    dispatcher.utter_message(template="utter_wrong_num_people")
