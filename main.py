from pytube import YouTube
import os

yt = YouTube(str(input("Ingresa la URL del video de youtube: \n ")))
video = yt.streams.filter(only_audio=True).first()

print("Ingresa la carpeta de destino o deja en blanco si deseas guardar el audio en la carpeta actual")
destino = str(input(" ")) or '.'
archivo_salida = video.download(output_path=destino)
base, ext = os.path.splitext(archivo_salida)
nuevo_archivo = base + '.mp3'
os.rename(archivo_salida, nuevo_archivo)
print(yt.title + " se ha descargado correctamente.")