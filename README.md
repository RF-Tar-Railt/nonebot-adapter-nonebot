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
```
