import asyncio
from typing import Any
from typing_extensions import override

from nonebot.message import handle_event

from nonebot import Driver, on
from nonebot.adapters import Bot, Event
from nonebot.adapters import Adapter as BaseAdapter

from .event import MessageEvent
from .bot import Bot as UniversalBot


class Adapter(BaseAdapter):
    @classmethod
    def get_name(cls) -> str:
        return "Universal"

    async def _call_api(self, bot: Bot, api: str, **data: Any) -> Any:
        raise NotImplementedError

    @override
    def __init__(self, driver: Driver, **kwargs: Any):
        super().__init__(driver, **kwargs)

        def _filter(event: Event):
            return not hasattr(event, "__universal__")

        self.matcher = on(priority=-1, block=True, rule=_filter)
        self.tasks = set()

        @self.matcher.handle()
        async def hack(event: Event, bot: Bot):
            bot = self.bots[bot.self_id] = UniversalBot(self, bot)
            try:
                event.get_message()
            except ValueError:
                setattr(event, "__universal__", False)
            else:
                event = MessageEvent(event)
                await event.post_init(bot._origin)
            task = asyncio.create_task(handle_event(bot, event))
            self.tasks.add(task)
            task.add_done_callback(self.tasks.discard)
            await self.matcher.finish()

        self.driver.on_shutdown(self.shutdown)

    async def shutdown(self):
        for task in self.tasks:
            task.cancel()
        self.tasks.clear()
        self.bots.clear()
        self.matcher.destroy()
