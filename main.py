from dotenv import load_dotenv
import openai
import os


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found. Please set it in your .env file.")
    openai.api_key = api_key

    file_content = read_file("text_file.txt")

    prompt = (
        "Przekształć poniższy artykuł na kod HTML, używając odpowiednich tagów do strukturyzacji treści. "
        "Nie dodawaj znaczników formatowania. Wskaż miejsca, w których warto dodać grafiki, wstawiając tag <img> z "
        "atrybutem src=\"image_placeholder.jpg\" oraz dodaj atrybut alt z odpowiednim opisem obrazka. "
        "Umieść podpisy pod grafikami. Zwrócony kod powinien zawierać wyłącznie zawartość do wstawienia "
        "pomiędzy tagami <body> i </body>. Oto treść artykułu: " + file_content
    )

    html_content = get_html_from_openai(prompt)

    write_file("artykul.html", html_content)

    template_html = generate_template_html()
    write_file("szablon.html", template_html)

    full_preview_html = template_html.replace("<!-- article content -->", html_content)
    write_file("podglad.html", full_preview_html)

    print("Article, template, and preview generation completed.")


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")


def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def get_html_from_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates raw HTML code without markdown or other formatting markers."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500,
    )
    return response.choices[0].message["content"]


def generate_template_html():
    return '''
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


if __name__ == "__main__":
    main()
