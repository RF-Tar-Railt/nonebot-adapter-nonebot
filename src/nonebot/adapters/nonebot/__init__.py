import nonebot

nonebot.load_plugin("nonebot_plugin_alconna")

from nonebot_plugin_alconna.uniseg import MsgId as MsgId
from nonebot_plugin_alconna.uniseg import Target as Target
from nonebot_plugin_alconna.uniseg import UniMsg as UniMsg
from nonebot_plugin_alconna.uniseg import MessageId as MessageId
from nonebot_plugin_alconna.uniseg import MsgTarget as MsgTarget
from nonebot_plugin_alconna.uniseg import MessageTarget as MessageTarget
from nonebot_plugin_alconna.uniseg import UniversalMessage as UniversalMessage
from nonebot_plugin_alconna.uniseg import UniversalSegment as UniversalSegment

from .bot import Bot as Bot
from .event import Event as Event
from .adapter import Adapter as Adapter
from .message import Message as Message
from .event import MessageEvent as MessageEvent
from .message import MessageSegment as MessageSegment
