from typing import Optional
from datetime import datetime
from typing_extensions import override

from pydantic import Field
from nonebot.utils import escape_tag
from nonebot_plugin_alconna import Reply, UniMessage

from nonebot.adapters import Bot
from nonebot.adapters import Message
from nonebot.adapters import Event as BaseEvent


class Event(BaseEvent):
    @override
    def get_type(self) -> str:
        return ""

    @override
    def get_event_name(self) -> str:
        return self.__class__.__name__

    @override
    def get_event_description(self) -> str:
        return escape_tag(str(self.dict()))

    @override
    def get_message(self) -> Message:
        raise ValueError("Event has no message!")

    @override
    def get_user_id(self) -> str:
        raise ValueError("Event has no context!")

    @override
    def get_session_id(self) -> str:
        raise ValueError("Event has no context!")

    @override
    def is_tome(self) -> bool:
        return False

    @property
    def __uni_origin__(self) -> Optional[BaseEvent]:
        return None


class MessageEvent(BaseEvent):
    __universal__: bool = True

    to_me: bool = False
    reply: Optional[Reply] = None
    message: UniMessage = Field(default_factory=UniMessage)
    message_id: str = ""
    time: datetime = Field(default_factory=datetime.now)

    def __init__(self, origin: BaseEvent):
        super().__init__()
        self.to_me = origin.is_tome()
        self._origin = origin

    async def post_init(self, bot: Bot):
        self.message = await UniMessage.generate(message=self._origin.get_message(), bot=bot)
        self.message_id = UniMessage.get_message_id(self._origin, bot)
        if self.message.has(Reply):
            self.reply = self.message[Reply, 0]
            self.message = self.message.exclude(Reply)

    @override
    def get_type(self) -> str:
        return "message"

    @override
    def get_event_name(self) -> str:
        return self._origin.get_event_name()

    @override
    def get_event_description(self) -> str:
        return self._origin.get_event_description()

    @override
    def get_message(self) -> Message:
        return self._origin.get_message()

    @override
    def get_user_id(self) -> str:
        return self._origin.get_user_id()

    @override
    def get_session_id(self) -> str:
        return self._origin.get_session_id()

    @override
    def is_tome(self) -> bool:
        return self.to_me

    def get_uni_message(self) -> UniMessage:
        return self.message

    @property
    def __uni_origin__(self):
        return self._origin
