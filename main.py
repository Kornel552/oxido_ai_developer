from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("API_KEY")

with open("text_file.txt", "r", encoding="utf-8") as file:
    file_content = file.read()

prompt = (
    "Przekształć poniższy artykuł na kod HTML, używając odpowiednich tagów do strukturyzacji treści. "
    "Nie dodawaj znaczników formatowania. Wskaż miejsca, w których warto dodać grafiki, wstawiając tag <img> z "
    "atrybutem src=\"image_placeholder.jpg\" oraz dodaj atrybut alt z odpowiednim opisem obrazka. "
    "Umieść podpisy pod grafikami. Zwrócony kod powinien zawierać wyłącznie zawartość do wstawienia "
    "pomiędzy tagami <body> i </body>. Oto treść artykułu: " + file_content
)

response = openai.ChatCompletion.create(
    model="gpt-4o",
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

print("article completed")

template_html = '''
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Podgląd Artykułu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }
        figure {
            text-align: center;
            margin: 20px 0;
        }
        figcaption {
            font-style: italic;
            color: #666;
        }
    </style>
</head>
<body>
    <!-- article content -->
</body>
</html>
'''

with open("szablon.html", "w", encoding="utf-8") as template_file:
    template_file.write(template_html)

full_preview_html = template_html.replace("<!-- article content -->", html_content)

with open("podglad.html", "w", encoding="utf-8") as preview_file:
    preview_file.write(full_preview_html)

print("template and view completed")
