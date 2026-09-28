from google import genai


API_KEY = ""

with open("texts/prompt.txt", "w") as f:
    f.write("Tell me a short story about cow in Bangla")
content = ""
with open("texts/prompt.txt", "r") as f:
    content = f.read()


client = genai.Client(api_key=API_KEY)

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input= content
)
print(interaction.output_text)

with open("texts/output.txt", "w", encoding="utf-8") as f:
    f.write(interaction.output_text)