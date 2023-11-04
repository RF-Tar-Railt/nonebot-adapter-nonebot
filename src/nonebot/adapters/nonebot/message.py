from nonebot_plugin_alconna.uniseg import At as At
from nonebot_plugin_alconna.uniseg import File as File
from nonebot_plugin_alconna.uniseg import Text as Text
from nonebot_plugin_alconna.uniseg import AtAll as AtAll
from nonebot_plugin_alconna.uniseg import Audio as Audio
from nonebot_plugin_alconna.uniseg import Emoji as Emoji
from nonebot_plugin_alconna.uniseg import Image as Image
from nonebot_plugin_alconna.uniseg import Other as Other
from nonebot_plugin_alconna.uniseg import Reply as Reply
from nonebot_plugin_alconna.uniseg import Video as Video
from nonebot_plugin_alconna.uniseg import Voice as Voice
from nonebot_plugin_alconna.uniseg import Target as Target
from nonebot_plugin_alconna.uniseg import RefNode as RefNode
from nonebot_plugin_alconna.uniseg.segment import Card as Card
from nonebot_plugin_alconna.uniseg import Reference as Reference
from nonebot_plugin_alconna.uniseg import CustomNode as CustomNode
from nonebot_plugin_alconna.uniseg import UniMessage as UniMessage
from nonebot_plugin_alconna.uniseg.fallback import FallbackSegment


class _Segment:
    text = Text
    at = At
    at_all = AtAll
    emoji = Emoji
    image = Image
    voice = Voice
    video = Video
    file = File
    reply = Reply
    other = Other
    audio = Audio
    custom = CustomNode
    ref = RefNode
    reference = Reference
    card = Card

    def __call__(self, type: str, data: dict):
        return Other(FallbackSegment(type, data))


MessageSegment = _Segment()
Message = UniMessage
