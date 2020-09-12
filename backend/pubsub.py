import pubnub
import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

subscribe_key = 'sub-c-d1371628-f52c-11ea-8db0-569464a6854f'
publish_key = 'pub-c-91813e76-0231-4ca0-93c6-81dcd7b4be3a'

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'sub-c-d1371628-f52c-11ea-8db0-569464a6854f'
pnconfig.publish_key = 'pub-c-91813e76-0231-4ca0-93c6-81dcd7b4be3a'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object:{message_object}')


pubnub.add_listener(Listener())


def main():
    time.sleep(1)
    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()


if __name__ == '__main__':
    main()
