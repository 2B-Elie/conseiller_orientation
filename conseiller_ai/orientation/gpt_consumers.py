from channels.generic.websocket import AsyncWebsocketConsumer
import json
from openai import OpenAI

client = OpenAI(api_key="sk-svcacct-6OzqaTXT9sy5a66D-0wJ6rMBIY6JIsoYFFaD-LJSyYfFKZeaoA4gWjhehbYp8T3BlbkFJEu0v2hcPhauUc_rHpbTcWBYyQeDEQCbNobH1wRmmdZu2VRYw3vH2gG06GufAA")




class ChatGPTConsumer(AsyncWebsocketConsumer):
    message_history = [
        {
            "role": "user",
            "content": "Reponds uniquement aux questions liées à des préoccupations éducatives ou professionnelles concernant tout ce qui est orientation de parcours éducatifs et de carrière professionnlle quelque soit la langue utiliséé pour échanger avec toi. J'insite encore, ne repons pas à une question qui ne concerne pas le domaine éducative ou professionnel quelque soit la langue utiliséé pour échanger avec toi",
        },
        {
            "role": "user",
            "content": "Si on te pose des questions concernant ton nom, dit que tu t'appelles Mme Ruth. Et cela peu importe la langue utilisée pour échanger avec toi",
        },
        {
            "role": "assistant",
            "content": "Je suis Mme Ruth, votre conseillère d'orientation virtuelle, je suis disponible pour échanger avec vous et vous aider à répondre à toutes vos préoccupations éducatives ou professionnelles",
        },
    ]
    response = None

    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        # self.disconnect()
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)

        self.message_history.append({"role": "user", "content": data["message"]})

        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=self.message_history)
        self.response = response.choices[0].message.content
        self.message_history.append(
            {"role": "assistant", "content": self.response.strip("\n").strip()}
        )

        await self.send(
            text_data=json.dumps(
                {
                    "message": self.response.strip("\n").strip(),
                }
            )
        )
