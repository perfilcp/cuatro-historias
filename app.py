from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Generamos las rutas de las imágenes locales mediante url_for
    logo_url = url_for('static', filename='images/logo.png')
    hero_url = url_for('static', filename='images/cabecera.jpg')
    foto1_url = url_for('static', filename='images/foto1.jpg')
    foto2_url = url_for('static', filename='images/foto2.jpg')
    foto3_url = url_for('static', filename='images/foto3.jpg')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cuatro Historias - Banda</title>
        <style>
            * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Helvetica Neue', Arial, sans-serif; }}
            body {{ background-color: #121212; color: #f4f4f4; line-height: 1.6; overflow-x: hidden; }}
            
            /* Cabecera con imagen local de fondo */
            header {{ 
                height: 80vh; 
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.9)), url('{hero_url}') center/cover no-repeat; 
                display: flex; 
                flex-direction: column; 
                justify-content: center; 
                align-items: center; 
                text-align: center; 
                padding: 20px; 
            }}
            
            .logo {{
                width: 400px;
                height: auto;
                margin-bottom: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            }}

            header h1 {{ font-size: 4rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 10px; }}
            header p {{ font-size: 1.4rem; color: #e0e0e0; }}

            .container {{ width: 100%; padding: 60px 5%; }}
            section {{ margin-bottom: 60px; max-width: 1400px; margin-left: auto; margin-right: auto; }}
            h2 {{ font-size: 2.2rem; border-bottom: 2px solid #ff0000; display: inline-block; padding-bottom: 5px; margin-bottom: 30px; }}

            .video-container {{ position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 10px; margin-top: 15px; }}
            .video-container iframe {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; }}

            /* Galería de fotos locales */
            .gallery-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 20px; }}
            .gallery-item {{ width: 100%; height: 250px; object-fit: cover; border-radius: 8px; cursor: pointer; transition: transform 0.3s ease; }}
            .gallery-item:hover {{ transform: scale(1.02); }}

            .modal {{ display: none; position: fixed; z-index: 1000; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.9); justify-content: center; align-items: center; }}
            .modal img {{ max-width: 95%; max-height: 90%; border-radius: 8px; }}
            .close-modal {{ position: absolute; top: 20px; right: 30px; color: #fff; font-size: 50px; cursor: pointer; }}

            .tour-date {{ display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid #333; font-size: 1.1rem; }}
            .venue {{ color: #b3b3b3; }}
            .social-links {{ display: flex; gap: 15px; margin-top: 20px; flex-wrap: wrap; }}
            .social-links a {{ color: #f4f4f4; text-decoration: none; border: 1px solid #f4f4f4; padding: 12px 25px; border-radius: 30px; transition: 0.3s; }}
            .social-links a:hover {{ background-color: #ff0000; border-color: #ff0000; }}
            
            footer {{ text-align: center; padding: 30px; font-size: 1rem; color: #666; border-top: 1px solid #222; }}
        </style>
    </head>
    <body>

        <header>
            <img src="{logo_url}" alt="Logo" class="logo">
            <h1></h1>
            <p>BANDA DE ROCK - URUGUAY</p>
        </header>

        <div class="container">
            <section>
                <h2>Biografía</h2>
                <p>La historia de Cu4tro Historias tiene un poder emocional enorme. No es solo una banda que volvió después de 30 años, es un testimonio de cómo la música trasciende el tiempo y cómo los sueños pueden retomarse cuando uno está listo. Es una historia de pasión, reencuentro y resiliencia, y eso conecta con la gente a un nivel profundo.</p>
            </section>

            <section>
                <h2>Video Destacado</h2>
                <div class="video-container">
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/mSnY4KXLRWQ?si=qqPEv9wx6g9wOo2B" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                </div>
            </section>

            <section>
                <h2>Galería</h2>
                <div class="gallery-grid">
                    <img src="{foto1_url}" class="gallery-item" onclick="openModal(this.src)" alt="Foto 1">
                    <img src="{foto2_url}" class="gallery-item" onclick="openModal(this.src)" alt="Foto 2">
                    <img src="{foto3_url}" class="gallery-item" onclick="openModal(this.src)" alt="Foto 3">
                </div>
            </section>

            <section>
                <h2>Próximas Fechas</h2>
                <div class="tour-date">
                    <span>15 de Octubre</span>
                    <span class="venue">Sala Principal - Ciudad</span>
                </div>
                <div class="tour-date">
                    <span>22 de Noviembre</span>
                    <span class="venue">Teatro Local - Ciudad</span>
                </div>
            </section>

            <section>
                <h2>Contacto & Redes</h2>
                <div class="social-links">
                    <a href="https://www.youtube.com/@Cuatro-Historias" target="_blank">YouTube</a>
                    <a href="https://www.instagram.com/cu4trohistorias" target="_blank">Instagram</a>
                </div>
            </section>
        </div>

        <div id="imageModal" class="modal" onclick="closeModal()">
            <span class="close-modal">&times;</span>
            <img id="modalImg" src="">
        </div>

        <footer>
            &copy; 2026 CUATRO HISTORIAS. Todos los derechos reservados.
        </footer>

        <script>
            function openModal(src) {{ document.getElementById('modalImg').src = src; document.getElementById('imageModal').style.display = 'flex'; }}
            function closeModal() {{ document.getElementById('imageModal').style.display = 'none'; }}
        </script>

    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)