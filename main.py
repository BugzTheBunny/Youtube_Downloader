from pytube import YouTube
from tkinter import *
from moviepy.editor import *


def download_as_mp4(url):
    YouTube(url).streams.first().download()


def download_as_mp3(url):
    download_requst = YouTube(url).streams.first()
    downloaded_file = download_requst.download()
    mp4_file = VideoFileClip(os.path.join(downloaded_file.title()))
    mp4_file.audio.write_audiofile(download_requst.title + '.mp3')
    mp4_file.close()
    downloaded_file_path = downloaded_file.title()
    os.remove(os.path.join(downloaded_file_path))


def main():
    # Main Frame
    app = Tk()
    app.title("Bugz's Youtube Downloader")
    app['bg'] = 'gray10'


    # Elements
    title = Label(app, width=50, pady=5, text="Input the url, and download in the format you want.", bg='black',
                  fg='white', borderwidth=3, font=('Helvetica', '13','bold'))
    title.grid(row=0, columnspan=9)
    query = Entry(app, width=50, borderwidth=3)
    query.grid(row=1, columnspan=5)
    # Buttons
    Button(app, text='💻 Download as MP4 💻', padx=5, fg='black', bg='orange2', relief="solid",
           command=lambda: download_as_mp4(query.get())).grid(
        row=1, column=6)
    Button(app, text='🔊 Download as MP3 🔊', fg='black', bg='orange2', relief="solid",
           command=lambda: download_as_mp3(query.get())).grid(
        row=1, column=7)

    app.mainloop()


if __name__ == '__main__':
    main()
