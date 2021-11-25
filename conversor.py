import PySimpleGUI as sg
from moviepy.video.io.VideoFileClip import VideoFileClip

sg.theme('DarkAmber')
layout = [
    [sg.Text('Conversor de Mp4 para Mp3', font=('bold', 16))],
    [sg.Text('_______________________________________________')],
    [sg.Text(' Selecione aqui seu arquivo Mp4 >>>', font=13), sg.FileBrowse(key='videomp4')],
    [sg.Text('Escolha onde Salvar >>>', font=13), sg.FolderBrowse(key='destino')],
    [sg.Text('_______________________________________________')],
    [sg.Button('Converter'), sg.Button('Sair')],
    [sg.Text('Se gostou do programa e quiser incentivar o desenvolvedor, faça uma doação.')],
    [sg.Text('Pix: lopes.laerte@gmail.com')],
    [sg.Text('Desenvolvido por: Laerte Lopes')]

    ]
janela = sg.Window("Milerte Converter v1.0", layout=layout, element_justification='center')

while True:  # criando eventos
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Sair':
        break
    if eventos == 'Converter':
        diretorio = valores['destino']
        video = VideoFileClip(valores['videomp4'])
        video.audio.write_audiofile(f'{diretorio}/' + 'audioconvertido.mp3')
        sg.popup('Arquivo convertido com sucesso')
#desenvolvido por Laerte Lopes
