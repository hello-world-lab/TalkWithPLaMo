import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    base_url=f"{os.environ['API_HOST']}/api/completion/v1",
    api_key=os.environ["API_KEY"],
    # other params...,
)

sysmess = {"role": "system", "content": "あなたの名前は山田太郎です。"}
sendmess = [sysmess]

print("let's start")

while True:

    print("User:")
    usertext = input()
    usermess = {"role": "user", "content": usertext}

    sendmess.append(usermess)

    if len(sendmess) > 20:
        sendmess.pop(1)

    print("PLaMo:")

    completion = client.chat.completions.create(
        model="plamo-beta",
        messages=sendmess,
        stream=False,
    )

    answer = completion.choices[0].message
    if answer.content is not None:
        print(answer.content)
        answerrole = answer.role
        answercont = answer.content
        answermess = {"role": answerrole, "content": answercont}
        sendmess.append(answermess)

     



