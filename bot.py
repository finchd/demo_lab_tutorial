from machine.bin.run import main
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to, respond_to
import re

"""
To use this demo:

1) Register with the ChatBotAllTheThings Slack workspace with the following link
http://bit.ly/chat-lfnw-2019

2) Get a Legacy Token for the ChatBotAllTheThings workspace here:
https://api.slack.com/custom-integrations/legacy-tokens
or google for `slack legacy tokens` and be already signed in
to the ChatBotAllTheThings Slack.

3) Copy your "Token" in the value in local_settings.py file
in this workspace

4) Hit F5 or go to Debug->Start Debugging
The code should start running in a Terminal window
in VSCode.   Hit Ctrl-C to stop it.

"""

class ThunderBotPlugin(MachineBasePlugin):

    # The bot framework (Slack Machine)
    # Can Listen or Respond, based on the decorators
    
    # A reploy_to decorator will only react when
    # something is sent directly to the bot (your account)

    # A match is done by Regex - we will see 
    # some more complex examples further down

    @respond_to(r'Winner Winner')
    def winner_winner(self, msg):
        """
        Reply with 'Chicken Dinner' every time
        someone sends `@yourslackname winner winner`
        """

        # You send a message back to the 
        # channel by using methods on the 
        # msg object.
        # We will use the `reply` method here
        # that will respond in channel to
        # the original sender.
        msg.reply("Chicken Dinner")

    # `listen_to` is another decorator that will
    # passivly listen to a chanel for any matching
    # expression, and then take action.
    @listen_to(r'^What do we want$')
    def what_do_we_want(self, msg):
        """
        Say a phrase into the channel based on
        the trigger phrase (in the decorator)
        """

        # We will use the 'say' method here.
        # It will just push a message to the channel
        # not to any specific attention.
        msg.say("BOTS !!")

    # The Regex in the decorator can capture variables
    # Test Regex at https://regex101.com/

    @respond_to(r'^parrot(?:\s+)(?P<phrase>.*)$')
    def parrot(self, msg, phrase):
        """
        Reploy to sender with whatever was in
        the <phrase> regex capture group
        """

        msg.reply(f"BAWK!! {phrase}")


if __name__ == "__main__":
    main()
