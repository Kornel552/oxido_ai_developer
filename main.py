from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("API_KEY")

with open("text_file.txt", "r", encoding="utf-8") as file:
    file_content = file.read()

prompt = (
    "Przekształć poniższy artykuł na kod HTML, używając odpowiednich tagów do strukturyzacji treści. "
    "Wskaż miejsca, w których warto dodać grafiki, wstawiając tag <img> z atrybutem src=\"image_placeholder.jpg\" "
    "oraz dodaj atrybut alt z odpowiednim opisem obrazka. Umieść podpisy pod grafikami. "
    "Zwrócony kod powinien zawierać wyłącznie zawartość do wstawienia pomiędzy tagami <body> i </body>."
    "Oto treść artykułu: " + file_content
)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates raw HTML code without markdown or "
                                      "other formatting markers."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=1500,
)

html_content = response.choices[0].message["content"]

with open("artykul.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("finished")
