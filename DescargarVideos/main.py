from pytube import YouTube

# URL del video de YouTube
video_url = 'https://www.youtube.com/watch?v=uE6iYUME6As'

# Crear un objeto YouTube
yt = YouTube(video_url)

# Seleccionar la mejor calidad de video disponible
stream = yt.streams.get_highest_resolution()

# Descargar el video
stream.download()

print("Video descargado con éxito")
