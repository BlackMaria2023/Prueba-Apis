import requests
import json
from string import Template

def request_get(url):
    return json.loads(requests.get(url).text)

response = request_get('https://aves.ninjas.cl/api/birds')[:5]

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Aves de Chile</title>
                            </head>
                            <body>

                            <h1>Aves de Chile</h1>

                            $body

                            </body>
                            </html>
                        ''')

body_content = ''
for bird in response:
    name_es = bird.get("name", {}).get("spanish", "Nombre no disponible")
    name_en = bird.get("name", {}).get("english", "Name not available")
    images = bird.get("images", {}).get("main")  # Tomar solo la URL de la imagen principal

    if images:
        bird_html = f'''
            <div>
                <h2>{name_es} ({name_en})</h2>
                <img src="{images}" alt="{name_es}">
            </div>
        '''
        body_content += bird_html

final_html = html_template.substitute(body=body_content)

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Sitio web creado y guardado en output.html")