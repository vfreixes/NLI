from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import re


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionReadGroup(Action):
    def name(self) -> Text:
        return "read_group"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        split_name = name.split(" ")
         
        #Excel columns: NOMBRE, GRUPO, DESPACHO
        dataFrame = pd.read_excel('data/info.xlsx',sheet_name="info")
        rows, cols = dataFrame.shape

        group = ""

        name = name.upper()
        split_name = name.split(" ")
        split_name.sort()

        for row in range(0,rows):
            if not pd.isnull(dataFrame.loc[row,"NOMBRE"]):
                prof = dataFrame.loc[row,"NOMBRE"]
                prof_split = prof.split(",")
                prof = "".join(prof_split)
                prof_split = re.split(" +",prof)
                prof_split.sort()

                if split_name == prof_split:
                    group = dataFrame.loc[row,"GRUPO"]
            
        #dispatcher.utter_message(response = "utter_group",text=f"{group}")
        return [SlotSet("group", group)]

class ActionReadOffice(Action):
    def name(self) -> Text:
        return "read_office"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        split_name = name.split(" ")
         
        #Excel columns: NOMBRE, GRUPO, DESPACHO
        dataFrame = pd.read_excel('data/info.xlsx',sheet_name="info")
        rows, cols = dataFrame.shape

        office = ""

        name = name.upper()
        split_name = name.split(" ")
        split_name.sort()

        for row in range(0,rows):
            if not pd.isnull(dataFrame.loc[row,"NOMBRE"]):
                prof = dataFrame.loc[row,"NOMBRE"]
                prof_split = prof.split(",")
                prof = "".join(prof_split)
                prof_split = re.split(" +",prof)
                prof_split.sort()

                if split_name == prof_split:
                    office = dataFrame.loc[row,"DESPACHO"]
            
        #dispatcher.utter_message(response = "utter_office",text=f"{office}")
        return [SlotSet("office", office)]
