from pytube import YouTube
from pytube import Playlist
import os

##yt = YouTube('https://www.youtube.com/watch?v=rEcolrfwD3Y')
##bestRes = yt.streams.filter(adaptive=True).all()[0]
##bestRes.download()



link = ''
link = input('Copy the link:')
dir_main = os.path.dirname(os.path.abspath(__file__))


try:
    shutil.rmtree('./data/')
except:
    pass


try:
    os.mkdir('data')
except:
    pass


try:
    playlist = Playlist(link)
    playlist.download_all('./data')
except Exception as e:
    print(str(e))
