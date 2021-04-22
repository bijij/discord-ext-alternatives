from discord.webhook.async_ import Webhook
from discord.webhook.sync import SyncWebhook


async def _async_move_to(self, channel, *, reason=None):
    return await self.edit(reason=reason, channel=channel)


async def _sync_move_to(self, channel, *, reason=None):
    return self.edit(reason=reason, channel=channel)


Webhook.move_to = _async_move_to
SyncWebhook.move_to = _sync_move_to
