class Translation(object):
    START_TEXT = """¡Hola, mi principal función es renombrar archivos!
    	    
<b>Por favor envíeme cualquier archivo de Telegram y responda a ese archivo con /rename Nuevo nombre.extensión.</b>

Pero también puedes utilizarme para hacer otras cosas...
Escriba /help para más información."""

    RENAME_403_ERR = "Perdón, tú no tienes permitido renombrar este archivo"
    ABS_TEXT = "¿Qué estás tratando de hacer, compañero?"
    UPGRADE_TEXT = """Plan de pago  de@RenameArchive_bot
    
    #Plan: GRATIS
    #Límite de tamaño de archivo: 2Gb
    #Límite diario: ILIMITADO
    #Precio USD: $ 0/Mes
    #CARACTERISTICAS:
    #👉 <a href="#">Renombrar archivos ilimitadamente.</a>
    #👉 <a href="#">Colocar una miniatura personalizada.</a>
    #-------
    
    #Plan: Premium
    #Límite de tamaño de archivo: 2Gb
    #Límite diario: ILIMITADO
    #Precio USD: $ 5/Mes
    #CARACTERISTICAS:
    #👉 <a href="#">Renombrar archivos ilimitadamente.</a>
    #👉 <a href="#">Colocar una miniatura personalizada.</a>
    #👉 <a href="#">Obtenga un sticker de Telegram como archivo descargable de Telegram.</a>
    #👉 <a href="#">Convertir un archivo a video reproducible.</a>
    #👉 <a href="#">Convertir un archivo a audio reproducible.</a>
    #👉 <a href="#">Obtenga un enlace de descarga directa de su archivo.</a>
    #👉 <a href="#">Obtenga capturas de pantalla de cualquier archivo o video. (9 en total).</a>
    #👉 <a href="#">Recorta videos (desde un archivo o un video).</a>
    #👉 <a href="#">Genere una miniatura personalizada de dos imágenes.</a>
    #👉 <a href="#">Próximos beneficios agregados al bot :D</a>
    #-------
    
    <b>Paypal:</b> skueletor+ventas@gmail.com
    
    #NOTA: Después del pago, debe tomar una captura de pantalla del recibo y enviarla al administrador: @DKzippO."""
    FORMAT_SELECTION = "Seleccione el formato deseado: <a href='{}'>el tamaño del archivo puede ser aproximado</a> \nSi desea configurar una miniatura personalizada, envíe la foto antes o rápidamente después de tocar cualquiera de los botones a continuación.\nPuede usar / deletethumbnail para eliminar la miniatura generada automáticamente."
    SET_CUSTOM_USERNAME_PASSWORD = """Si desea descargar videos premium, proporcione en el siguiente formato:
ENLACE | NOMBRE DEL ARCHIVO | NOMBRE DE USUARIO | CONTRASEÑA"""
    NOYES_URL = "¡Esto es un enlace muy lento! No perderé mi tiempo en esto. Debo trabajar con otros usuarios, por favor no desacelere mi trabajo y consígueme un enlace rápido."
    DOWNLOAD_START = "😌 Intentando descargar a mi base de datos, espere por favor..."
    UPLOAD_START = "<b>😀 La descarga ha terminado, estoy intentando subir el archivo a Telegram...</b>"
    RCHD_BOT_API_LIMIT = "El tamaño del archivo es muy grande 😔. Sin embargo, intentando subirlo..."
    RCHD_TG_API_LIMIT = "Descargado en {} segundos.\nTamaño de archivo detectado: {}\nLo siento. Pero no puedo subir archivos de más de 2 GB debido a las limitaciones de la API de Telegram."
    AFTER_SUCCESSFUL_UPLOAD_MSG =  "<b>Gracias por usarme 🤓</b>\n Por favor, califícame si me encuentras útil: https://t.me/tlgrmcbot?start=renamearchive_bot-review ❤️"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Descargado en {} segundos.\nSubido en {} segundos."
    NOT_AUTH_USER_TEXT = "Por favor, escribe /upgrade mejorar tu tu suscripción y para posteriormente hacer eso."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Tamaño de archivo detectado: {}.Los usuarios gratuitos sólo pueden subir: {}\nPor favor, escribe /upgrade para mejorar tu suscripción.\nSi crees que esto se trata de un error, por favor contacta a <a href='https://telegram.dog/DKzippO'>Skueletor</a>"
    SAVED_CUSTOM_THUMB_NAIL = "<b>Miniatura personalizada guardada ✅ Esto es permanente hasta que escribas</b> /delthumb ❤"
    DEL_ETED_CUSTOM_THUMB_NAIL = "Miniatura borrada con éxito🤦"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ La miniatura personalizada fue eliminada correctamente."
    SAVED_RECVD_DOC_FILE = "<b>Archivo descargado correctamente 😎</b>"
    CUSTOM_CAPTION_UL_FILE = "Renombrado con: @RenameArchive_bot ❤️"
    NO_CUSTOM_THUMB_NAIL_FOUND = "No se encontró ninguna miniatura personalizada.🤒"
    NO_VOID_FORMAT_FOUND = "Error...\n<b>YouTubeDL</b> dice: {}"
    USER_ADDED_TO_DB = "Usuario <a href='tg://user?id={}'>{}</a> añadido a {} hasta {}."
    ABOUT_ME = """<b>Realmente no hay mucho que decir...\n Un bot que puede cambiar el nombre de los archivos de Telegram. \n Puedo establecer una miniatura permanente para el archivo para no tener que enviar miniaturas personalizadas todo el tiempo.\n\n Puedo convertir archivos en videos o audios. \n\n También puedo generar un link de descarga directa bastante rápido 🙈. \n\n Si quieres información detallada de mi, utiliza el comando /help \n\n Por favor, califícame si me encuentras útil: https://t.me/tlgrmcbot?start=renamearchive_bot-review ❤️</b>"""
    CURENT_PLAN_DETAILS = """<b>Detalles del plan actual</b>
--------
Telegram ID: <code>{}</code>
Nombre del plan: GRATIS
Expira: 10/8/2099

<b>Puedes mejorar tu suscripción con el comando /upgrade</b>"""
    HELP_USER = """<b>El modo de uso del bot es el siguiente 🤓:</b>
    (tenga en cuenta que los usuarios gratuitos solamente pueden renombrar archivos, revise /me para ver su suscripción).
    
<b>➡ Renombrar archivos:</b>
🔹1. Envíame cualquier archivo de Telegram.
🔹2. Envíe una foto para usarla como miniatura personalizada.
🔹3. Responder al archivo con "/rename (NUEVO NOMBRE.EXTENSION)".

<b>➡ Convertir de Archivo a Video</b>
🔹1. Envíame cualquier archivo de video.
🔹2. Responda al archivo con "/converttovideo".

<b>➡ Convertir de Archivo a Audio:</b>
🔹1. Envíame un archivo de audio.
🔹2. Responder al archivo con "/converttoaudio".

<b>➡ Recortar videos:</b>
🔹1. Envíame cualquier archivo de Telegram.
🔹2. Responde al archivo con el comando /downloadmedia para descargarlo en la base de datos del bot.
🔹3. Responder al archivo con "/trim HH:MM:SS [HH:MM:SS]".
🔹Ejemplo: /trim 00:01:36 00:01:49 (donde 00:01:36 es el tiempo de inicio y 00:01:49 el tiempo final).

<b>➡ Generar capturas de pantalla:</b>
🔹1. Envíame un video o un archivo de video de Telegram.
🔹2. Responda al archivo con "/generatescss" y el bot le dará 9 capturas de pantalla del archivo.

<b>➡ Genere un link de descarga directa de cualquier archivo:</b>
🔹1. Envíame cualquier archivo de Telegram.
🔹2. Responde al archivo con el comando "/getlink"
🔹<b>El enlace será válido sólo por 5 días.</b>

<b>➡ Genere miniaturas personalizadas:</b>
🔹1. Envíame 2 imágenes en un álbum multimedia.
🔹2. Responde al álbum con el coamando "/generatecustomthumbnail"
🔹<b>Sólo funciona con 2 imágenes y en modo álbum multimedia.</b>

<b>➡ Obtenga un sticker como archivo descargable:</b>
🔹1. Envíame un sticker sin animación y listo, solo queda esperar.

➡ Para más bots, únete a @BotsDeAyuda
Hecho con amor por:</b> 👉 <a href="https://t.me/DKzippO">Skueletor</a> ❤️"""
    REPLY_TO_DOC_GET_LINK = "<b>Responda a un archivo de Telegram para obtener un enlace de descarga directa de alta velocidad</b>"
    REPLY_TO_DOC_FOR_C2V = "<b> Responda a un archivo con /converttovideo para convertirlo en un archivo de video que se puede transmitir.</b>"
    REPLY_TO_DOC_FOR_C2A = "<b> Responda a un archivo con /converttoaudio para convertirlo en un archivo de audio que se puede reproducir.</b>"
    REPLY_TO_DOC_FOR_SCSS = "<b>Responde a un archivo de Telegram para obtener capturas de pantalla</b>"
    REPLY_TO_DOC_FOR_RENAME_FILE = "<b>Responda el nuevo nombre con /rename Nombre_del_archivo.EXTENSIÓN.</b>"
    AFTER_GET_DL_LINK = "Enlace directo <a href='{}'>generado</a>, este enlace es válido por {} días."
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Escribe: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Primero envía /downloadmedia a cualquier archivo para que pueda descargarse a mi base de datos. \nEnvía /storageinfo para saber los archivos que tengo descargados actualmente en mi base de datos."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Duración del video: {} \nEnvia /clearffmpegmedia para eliminar este archivo de mi almacenamiento.\nEnvía /trim HH:MM:SS [HH:MM:SS] para recortar una pequeña foto/video, de los archivos anteriores."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Ya existe un archivo descargado con ese nombre. Por favor envíe /storageinfo para conocer los detalles de los archivos descargados actualmente en mi base de datos."
    USER_DELETED_FROM_DB = "Usuario <a href='tg://user?id={}'>{}</a> Eliminado de la base de datos."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Responder a un enlace HTTP, para extraer subtítulos incrustados"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Responde /generatecustomthumbnail a un álbum multimedia, para generar miniaturas personalizadas"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "El álbum multimedia debe contener solo dos fotos. Vuelva a enviar el álbum multimedia y vuelva a intentarlo o envíe solo dos fotos en un álbum."
    INVALID_UPLOAD_BOT_URL_FORMAT = "El formato de la URL es incorrecto. asegúrese de que su URL comience con http:// o https://. Puede establecer un nombre de archivo personalizado usando el enlace de formato | Nombre_Archivo.extensión"
    ABUSIVE_USERS = "No está autorizado a utilizar este bot. Si cree que esto es un error, comuníquese con @DKzippO para eliminar esta restricción."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Mi enlace es: https://telegram.dog/RenameArchive_bot, puedes compartirlo donde tú quieras :D"
    EXTRACT_ZIP_INTRO_ONE = "Primero envíe un archivo comprimido, luego responda /unzip para descomprimir el archivo."
    EXTRACT_ZIP_INTRO_THREE = "Analizando archivo recibido. ⚠️ Esto puede llevar algún tiempo. Por favor sea paciente... "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Lo siento. Se produjeron errores al procesar el archivo comprimido. Vuelva a comprobar todo dos veces y, si el problema persiste, infórmelo a @DKzippO"
    EXTRACT_ZIP_STEP_TWO = """Seleccione Nombre_Archivo para cargar de las siguientes opciones.
Puede usar el comando /rename después de recibir el archivo para renombrarlo con soporte de miniaturas personalizadas."""
    CANCEL_STR = "Proceso cancelado."
    ZIP_UPLOADED_STR = "Subí {} archivos en {} segundos"
    FREE_USER_LIMIT_Q_SZE = """No se puede procesar.
Usuarios gratuitos solo 1 solicitud por hora.
Escribe /upgrade o Intente 3600 segundos más tarde."""
    SLOW_URL_DECED = "Dios, parece ser una URL muy lenta. Como estabas jodiendo el bot, no estoy de humor para descargar este archivo. Mientras tanto, ¿Por qué no intentas esto: ==> https://shrtz.me/PtsVnf6 y me consigues una URL rápida para que pueda subir a Telegram, sin que me desacelere para otros usuarios?"
    IFLONG_FILE_NAME = """El límite de nombre de archivo permitido por Telegram es de {alimit} caracteres.
El nombre de archivo proporcionado tiene {num} caracteres.
<b>¡Ensayos no permitidos en el nombre de archivo de Telegram!</b>
Por favor, acorta el nombre de tu archivo y vuelve a intentarlo.
    ------------------------
    
    ➡ Para más bots, únete a @BotsDeAyuda
    👉 El creador del bot es :</b> 👉 <a href="https://t.me/DKzippO">Skueletor</a>"""
    YTDL_ERROR_MESSAGE = (
        "informa este problema en https://yt-dl.org/bug . "
        "Asegúrese de estar utilizando la última versión; ver"
        "https://yt-dl.org/update sobre cómo actualizar."
        "Asegúrese de llamar a youtube-dl con la bandera --verbose "
        "e incluir su salida completa."
    )
    ISOAYD_PREMIUM_VIDEOS = "el video solo está disponible para usuarios registrados"
