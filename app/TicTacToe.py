from PIL import Image, ImageTk  # type: ignore
import tkinter as tk
import tkinter.font as tkfont
from pathlib import Path
import pygame as pg
import sys
import os
import StartPage as StP
import SettingPage as SetP
import GamePage as GaP
from typing import Union, Dict


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Tic-Tac-Toe")
        self.resizable(False, False)

        self._frame: Union[None, StP.StartPage, SetP.FriendStartPage,
                           SetP.PcStartPage, GaP.FriendGame, GaP.PcGame] = None

        self.font: tkfont.Font = tkfont.Font(size=14, weight="bold", slant="italic")
        self.btn_font: tkfont.Font = tkfont.Font(size=12, weight="normal", slant="italic")

        path1 = self.resource_path("images")
        path2 = self.resource_path("music")

        self.tictactoe_image: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open(Path(path1,
                                                                                      "TicTacToe.png")).resize((350,
                                                                                                                350)))
        self._mute_image: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open(Path(path1,
                                                                                  "mute.png")).resize((30, 30)))
        self._unmute_image: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open(Path(path1,
                                                                                    "unmute.png")).resize((30, 30)))

        self.friend_stat: Dict[str, int] = {"drawn_game": 0, "Player1_win": 0, "Player2_win": 0}
        self.pc_stat: Dict[str, int] = {"drawn_game": 0, "Player_win": 0, "Computer_win": 0}

        self.sign: tk.StringVar = tk.StringVar()
        self.move: tk.IntVar = tk.IntVar()
        self.sign.set("_")
        self.move.set(-1)

        pg.init()
        pg.mixer.init(44100, -16, 1, 512)

        self._background_music: pg.mixer.Sound = pg.mixer.Sound(Path(path2, "music.mp3"))
        self.click_music: pg.mixer.Sound = pg.mixer.Sound(Path(path2, "click.mp3"))
        self._background_music.set_volume(0.2)
        self.click_music.set_volume(1)

        self.win_music: pg.mixer.Sound = pg.mixer.Sound(Path(path2, "win.mp3"))
        self.win_music.set_volume(0.6)
        self.defeat_music: pg.mixer.Sound = pg.mixer.Sound(Path(path2, "defeat.mp3"))
        self.defeat_music.set_volume(0.2)
        self.draw_music: pg.mixer.Sound = pg.mixer.Sound(Path(path2, "draw.wav"))
        self.draw_music.set_volume(0.3)

        self._background_music.play(-1)

        self.switch_frame(StP.StartPage)

        self._mute_unmute_btn: tk.Button = tk.Button()
        self._mute_unmute_btn_func()

    @staticmethod
    def resource_path(relative_path: str) -> str:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def _mute_unmute_btn_func(self) -> None:
        self._mute_unmute_btn = tk.Button(self, background="white", image=self._unmute_image,
                                          command=lambda: self._background_music_mute_unmute())
        self._mute_unmute_btn.pack(side="bottom", anchor="sw", padx=10, pady=10)

    def switch_frame(self, frame_class: type) -> None:
        if self._frame is not None:
            self.click_music.play()

        if isinstance(self._frame, StP.StartPage):
            self.sign.set("_")
            self.move.set(-1)

        new_frame: Union[StP.StartPage, SetP.FriendStartPage,
                         SetP.PcStartPage, GaP.FriendGame, GaP.PcGame] = frame_class(self)

        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def _background_music_mute_unmute(self) -> None:
        self.click_music.play()
        if self._background_music.get_volume() != 0:
            self._background_music.set_volume(0)
            self._mute_unmute_btn["image"] = self._mute_image
        else:
            self._background_music.set_volume(0.3)
            self._mute_unmute_btn["image"] = self._unmute_image


if __name__ == "__main__":
    app = App()
    app.mainloop()
