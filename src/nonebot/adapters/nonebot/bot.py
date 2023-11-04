from typing import TYPE_CHECKING, Any, Union, Optional

from nonebot_plugin_alconna.uniseg import Target, Segment, UniMessage

from nonebot.adapters import Bot as BaseBot
from nonebot.adapters import Event, Message, MessageSegment

if TYPE_CHECKING:
    from .adapter import Adapter


class Bot(BaseBot):
    adapter: "Adapter"
    _origin: BaseBot

    def __init__(self, adapter: "Adapter", origin: BaseBot):
        super().__init__(adapter, origin.self_id)
        self._origin = origin

    async def send(
        self,
        event: "Event",
        message: Union[str, UniMessage, Segment, "Message", "MessageSegment"],
        **kwargs: Any,
    ) -> Any:
        if isinstance(message, Segment):
            message = UniMessage(message)
        if isinstance(message, UniMessage):
            message = await message.export(self._origin)
        if getattr(event, "__uni_origin__", None) is not None:
            event = event.__uni_origin__  # type: ignore
        return await self._origin.send(event, message, **kwargs)

    async def send_to(
        self,
        target: Union[Target, "Event"],
        message: Union[str, UniMessage, Segment, "Message", "MessageSegment"],
        fallback: bool = True,
        at_sender: Union[str, bool] = False,
        reply_to: Optional[str] = None,
    ):
        if isinstance(message, (str, MessageSegment)):
            message = Message(message)
        if isinstance(message, Message):
            message = UniMessage.generate(message=message, bot=self._origin)
        if isinstance(message, Segment):
            message = UniMessage(message)
        if getattr(target, "__uni_origin__", None) is not None:
            target = target.__uni_origin__  # type: ignore
        return await message.send(
            target,
            self._origin,
            fallback=fallback,
            at_sender=at_sender,
            reply_to=reply_to,
        )
