import openai

openai.api_key = "sk-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"

chat_history = []

while True:
    prompt = input("Habla conmigo: ")
    if prompt == "exit":
        break
    else:
        chat_history.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            stream=True,
            # max_tokens=100,
        )

        collected_messages = []

        for chunk in response:
            chunk_message = chunk["choices"][0]["delta"]  # mensaje
            collected_messages.append(chunk_message)
            full_reply_content = "".join(
                [m.get("content", "") for m in collected_messages]
            )
            print("\033[H\033[J", end="")
            print(full_reply_content)

        chat_history.append({"role": "assistant", "content": full_reply_content})
        print(full_reply_content)
