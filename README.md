# nonebot-adapter-nonebot

一个试验性的 NoneBot 适配器，用于将其他适配器的消息事件规范化后再传递给 NoneBot 事件系统。

规范后的消息事件：

```python
class MessageEvent(BaseEvent):
    to_me: bool
    reply: Optional[Reply]
    message: UniMessage
    message_id: str
    time: datetime

    def get_uni_message(self) -> UniMessage:
        """获取通用消息对象"""

    @property
    def is_private(self) -> bool:
        """是否为私聊消息"""

    @property
    def is_channel(self) -> bool:
        """是否为频道消息"""

    @property
    def chat_id(self) -> str:
        """获取聊天场景 ID，私聊为用户 ID，频道为子频道 ID，群聊为群 ID"""

    @property
    def guild_id(self) -> Optional[str]:
        """针对频道的频道 ID"""
```

## 注意事项

此适配器需要与其他任意适配器一起使用

此适配器只对能够获取消息的事件做修改，其余事件会原样返回


## 示例

```python
from nonebot import on_command
from nonebot.adapter.nonebot import Bot, MessageEvent, Message

test = on_command("test")

@test.handle()
async def _(event: MessageEvent):
    await event.message.send(at_sender=True)

@test.handle()
async def _():
    msg = Message.text("test").image(url="https://i0.hdslb.com/bfs/article/8b6b7b7b0b0b0b0b0b0b0b0b0b0b0b0b0b0b.jpg")
    receipt = await msg.send()
    await receipt.recall(5)

@test.handle()
async def _(bot: Bot, event: MessageEvent):
    print(event.channel_id)
    print(event.message_id)
    print(event.message)
    await bot.send(event, Message.text("test"))
```