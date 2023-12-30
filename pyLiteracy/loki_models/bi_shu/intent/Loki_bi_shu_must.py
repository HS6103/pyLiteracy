#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for bi_shu_must

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_bi_shu_must.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[bi_shu_must] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "必需你親自去":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT = {"status": True,
              "check": {"必須":[inputSTR]}, 
              "msg": "",
              "proofread": ""
              }
            pass

    if utterance == "必需要認真讀":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT = {"status": True,
              "check": {"必須":[inputSTR]}, 
              "msg": "",
              "proofread": ""
              }
            pass

    if utterance == "開車必需專心":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT = {"status": True,
              "check": {"必須":[inputSTR]}, 
              "msg": "",
              "proofread": ""
              }
            pass

    if utterance == "開車必需精神充足":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT = {"status": True,
              "check": {"必須":[inputSTR]}, 
              "msg": "",
              "proofread": ""
              }
            pass

    if utterance == "開車必需要認真":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT = {"status": True,
              "check": {"必須":[inputSTR]}, 
              "msg": "",
              "proofread": ""
              }
            pass
        
    if utterance == "必需以形象以及主觀意識的嚴重毀棄做為代價":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT = {"status": True,
              "check": {"必須":[inputSTR]}, 
              "msg": "",
              "proofread": ""
              }
            pass
    return resultDICT