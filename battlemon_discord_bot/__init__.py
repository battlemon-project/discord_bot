__version__ = '0.1.0'

import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!earyaccess'):
            embed = discord.Embed(title="sign in",
                                  url="https://wallet.testnet.near.org/login/?success_url=telegram%3A%2F%2F&failure_url=https%3A%2F%2Fdemo.battlemon.com%2F&contract_id=dev-1639312006189-41768496072291&public_key=ed25519%3AEzkpaH99JAxz2VAZCxcKo9Khs8b7GS4J5M2AcEShySMF",
                                  description="sign in testnetwork",
                                  color=0xFF5733)
            await message.channel.send(embed=embed)


client = MyClient()
client.run('token_here')
