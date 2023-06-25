def get_html(div):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.min.css">
        <title>hogarcam - live</title>
        <style>
        .swiper-container {{
                width: 100%;
                height: 100%;
                overflow: hidden;
            }}
            .swiper-wrapper {{
                display: flex; /* Permite que las diapositivas se ajusten horizontalmente */
            }}

            .swiper-slide {{
                flex: 0 0 100%; /* Establece el ancho de las diapositivas al 100% del contenedor */
                text-align: center;
                font-size: 18px;
                background-repeat: no-repeat;
                background-size: cover;
                background-position: center;
            }}
            input[type="text"],
            textarea {{
                resize: none;
            }}
        </style>
    </head>
    <body class="bg-cover bg-center bg-no-repeat" style="background-image: url('../../12.jpg');">
        <article class="mt-10 mx-auto space-y-12 dark:bg-gray-800 dark:text-gray-50">
            <div class="w-full mx-auto space-y-4 text-center">
                <h1 class="text-4xl font-bold leading-tight md:text-5xl text-white">¡Captura momentos importantes en</h1>
                <h1 class="text-4xl font-bold leading-tight md:text-5xl text-white">Vivo!</h1>
            </div>
        </article>

        <div class="swiper-container mt-5">
            <div class="swiper-wrapper">
                {}
                <!-- Agrega más slides según sea necesario -->
            </div>

            <div class="swiper-pagination"></div>
            <div class="swiper-button-next mr-10 "><span class="text-white text-2xl font-bold">Siguiente <br> camara</span></div>
            <div class="swiper-button-prev ml-10 "><span class="text-white text-2xl font-bold">Camara <br> Anterior</span></div>
        </div>

        <footer>
            <div class="flex justify-center items-center mt-8 text-gray-300 py-20">
                <p class="ml-3 text-xl font-medium animate-pulse">
                    Hogarcam.com
                    <a href="https://hogarcam.com" title="hogarcam" target="_blank" class="ml-3 text-blue-500 hover:text-blue-700">
                        ¡Tu aliado en seguridad y vigilancia!
                    </a>
                </p>
            </div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.min.js"></script>
        <script>
            var swiper = new Swiper('.swiper-container', {{
                slidesPerView: 1,
                spaceBetween: 10,
                navigation: {{
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                }},
                pagination: {{
                    el: '.swiper-pagination',
                    clickable: true,
                }},
            }});
        </script>

    <script type="module">
        import Swiper from 'https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.esm.browser.min.js'
    
        
    </script>
    </body>
    </html>
    """.format(div)
    return html

def add_div(url_video, name_camara):
    return f"""<div class="swiper-slide">
                <div class="flex flex-col items-center justify-center">
                    <h2 class="text-3xl font-bold leading-tight md:text-3xl text-white">{name_camara}</h2>
                    <button type="button" class="mt-5 text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"> ¡Capturar foto!</button>
                    <div class="mt-8">
                        <div class="flex justify-center">
                          
                                <center>
                                    <iframe class="w-96 h-96" src="{url_video}" frameborder="0" allowfullscreen></iframe>
                                </center>
                           
                        </div>
                    </div>
                </div>
            </div>""" 