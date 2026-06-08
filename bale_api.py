import requests
import config


class BaleClient:
    def __init__(self):
        self.token = config.BotToken
        self.channel_id = config.ChannelID
        self.base_url = f"https://tapi.bale.ai/bot{self.token}"

    def send_message(self, text: str):
        try:
            response = requests.post(
                f"{self.base_url}/sendMessage",
                json={"chat_id": self.channel_id, "text": text},
                timeout=10,
            )

            if response.ok:
                return True, response.json()

            return False, response.text

        except Exception as ex:
            return False, str(ex)

    def get_me(self):
        response = requests.get(f"{self.base_url}/getMe")
        return response.json()
