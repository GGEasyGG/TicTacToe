import tkinter as tk
import SettingPage as SetP
import TicTacToe as Ttt


class StartPage(tk.Frame):
    def __init__(self, master: Ttt.App) -> None:
        super().__init__(master)

        self.master: Ttt.App

        self.configure(height=600, width=500)
        self.pack_propagate(False)

        self._create_widgets()

    def _create_widgets(self) -> None:
        tk.Label(self, font=self.master.font, text='Welcome to the "Tic-Tac-Toe" game!').pack(side="top", pady=(15, 25))
        self._create_image()
        tk.Button(self, bg="white", font=self.master.btn_font, text="Play with a friend", width=30,
                  command=lambda: self.master.switch_frame(SetP.FriendStartPage)).pack(side="top", pady=(40, 5))
        tk.Button(self, bg="white", font=self.master.btn_font, text="Play with the computer", width=30,
                  command=lambda: self.master.switch_frame(SetP.PcStartPage)).pack(side="top")

    def _create_image(self) -> None:
        canvas = tk.Canvas(self, bg="white", height=400, width=400)
        canvas.create_image(25, 25, anchor="nw", image=self.master.tictactoe_image)
        canvas.pack(side="top")
