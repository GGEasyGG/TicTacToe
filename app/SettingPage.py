import tkinter as tk
import StartPage as StP
import GamePage as GaP
import TicTacToe as Ttt


class BaseStartPage(tk.Frame):
    def __init__(self, master: Ttt.App) -> None:
        super().__init__(master)

        self.master: Ttt.App

        self.configure(height=280, width=800)
        self.pack_propagate(False)

        self._create_widgets()

    def _sound(self) -> None:
        self.master.click_music.play(0)

    def _choose_move_widget(self, frame: tk.Frame) -> None:
        step_choice = tk.LabelFrame(frame, font=self.master.font, text=" Choosing a move ", labelanchor="n")
        step_choice.pack(side="left", padx=(0, 12), anchor="nw")
        if self.master.move.get() == -1:
            self.master.move.set(0)
        else:
            self.master.move.set(self.master.move.get())
        tk.Radiobutton(step_choice, font=self.master.btn_font, bg="white", text="Randomly", variable=self.master.move,
                       value=0, width=15, command=lambda: self._sound()).pack(side="top", pady=(8, 4), padx=5)
        tk.Radiobutton(step_choice, font=self.master.btn_font, bg="white", text="First", variable=self.master.move,
                       value=1, width=15, command=lambda: self._sound()).pack(side="top", padx=5)
        tk.Radiobutton(step_choice, font=self.master.btn_font, bg="white", text="Second", variable=self.master.move,
                       value=2, width=15, command=lambda: self._sound()).pack(side="top", pady=(4, 14), padx=5)

    def _sign_selection(self, frame: tk.Frame) -> None:
        sign_selection = tk.LabelFrame(frame, font=self.master.font, text=" Sign selection ", labelanchor="n")
        sign_selection.pack(side="left", padx=(0, 12), anchor="nw")
        if self.master.sign.get() == "_":
            self.master.sign.set("R")
        else:
            self.master.sign.set(self.master.sign.get())
        rbtn1 = tk.Radiobutton(sign_selection, font=self.master.btn_font, bg="white", text="Randomly",
                               variable=self.master.sign, value="R", width=15, command=lambda: self._sound())
        rbtn1.pack(side="top", pady=(8, 4), padx=5)
        rbtn2 = tk.Radiobutton(sign_selection, font=self.master.btn_font, bg="white", text='Your sign - "X"',
                               variable=self.master.sign, value="X", width=15, command=lambda: self._sound())
        rbtn2.pack(side="top", padx=5)
        rbtn3 = tk.Radiobutton(sign_selection, font=self.master.btn_font, bg="white", text='Your sign - "O"',
                               variable=self.master.sign, value="O", width=15, command=lambda: self._sound())
        rbtn3.pack(side="top", pady=(4, 14), padx=5)

    def _game_type(self) -> None:
        pass

    def _start_and_return_btn(self, frame: tk.Frame) -> None:
        pass

    def _statistic_widget(self, frame: tk.Frame) -> None:
        pass

    def _create_widgets(self) -> None:
        self._game_type()

        frame1 = tk.Frame(self)
        frame1.pack(side="top", pady=15)

        self._statistic_widget(frame1)
        self._choose_move_widget(frame1)
        self._sign_selection(frame1)

        frame2 = tk.Frame(self)
        frame2.pack(side="top")

        self._start_and_return_btn(frame2)


class FriendStartPage(BaseStartPage):
    def __init__(self, master: Ttt.App) -> None:
        super().__init__(master)

    def _game_type(self) -> None:
        tk.Label(self, font=self.master.font, text="Game with friend").pack(side="top", pady=(10, 0))

    def _statistic_widget(self, frame: tk.Frame) -> None:
        statistics = tk.LabelFrame(frame, font=self.master.font, text=" Game statistic ", labelanchor="n")
        statistics.pack(side="left", padx=12, anchor="nw")
        tk.Label(statistics, font=self.master.btn_font, bg="white",
                 text="Number of played games - %s" % (self.master.friend_stat["Player1_win"]
                                                       + self.master.friend_stat["Player2_win"]
                                                       + self.master.friend_stat["drawn_game"]),
                 width=30).pack(side="top", pady=(5, 0), padx=5)
        tk.Label(statistics, font=self.master.btn_font, bg="white",
                 text="Number of Player1 wins - %s" % self.master.friend_stat["Player1_win"],
                 width=30).pack(side="top", padx=5)
        tk.Label(statistics, font=self.master.btn_font, bg="white",
                 text="Number of Player2 wins - %s" % self.master.friend_stat["Player2_win"],
                 width=30).pack(side="top", padx=5)
        tk.Label(statistics, font=self.master.btn_font, bg="white",
                 text="Number of draws - %s" % self.master.friend_stat["drawn_game"],
                 width=30).pack(side="top", pady=(0, 8), padx=5)

    def _start_and_return_btn(self, frame: tk.Frame) -> None:
        tk.Button(frame, bg="white", font=self.master.btn_font, text="Start the game",
                  command=lambda: self.master.switch_frame(GaP.FriendGame), width=30).pack(side="top", pady=(0, 5))
        tk.Button(frame, bg="white", font=self.master.btn_font, text="Return to start page",
                  command=lambda: self.master.switch_frame(StP.StartPage), width=30).pack(side="top")


class PcStartPage(BaseStartPage):
    def __init__(self, master: Ttt.App) -> None:
        super().__init__(master)

    def _game_type(self) -> None:
        tk.Label(self, font=self.master.font, text="Game with computer").pack(side="top", pady=(10, 0))

    def _statistic_widget(self, frame: tk.Frame) -> None:
        statistics = tk.LabelFrame(frame, font=self.master.font, text=" Game statistic ", labelanchor="n")
        statistics.pack(side="left", padx=12, anchor="nw")
        tk.Label(statistics, font=self.master.btn_font, bg="white",
                 text="Number of played games - %s" % (self.master.pc_stat["Player_win"]
                                                       + self.master.pc_stat["Computer_win"]
                                                       + self.master.pc_stat["drawn_game"]),
                 width=30).pack(side="top", pady=(5, 0), padx=5)
        tk.Label(statistics, font=self.master.btn_font, bg="white",
                 text="Number of user wins - %s" % self.master.pc_stat["Player_win"], width=30).pack(side="top", padx=5)
        tk.Label(statistics, font=self.master.btn_font, bg="white",
                 text="Number of user defeats - %s" % self.master.pc_stat["Computer_win"], width=30).pack(side="top",
                                                                                                          padx=5)
        tk.Label(statistics, font=self.master.btn_font, bg="white",
                 text="Number of draws - %s" % self.master.pc_stat["drawn_game"],
                 width=30).pack(side="top", pady=(0, 8), padx=5)

    def _start_and_return_btn(self, frame: tk.Frame) -> None:
        tk.Button(frame, bg="white", font=self.master.btn_font, text="Start the game",
                  command=lambda: self.master.switch_frame(GaP.PcGame), width=30).pack(side="top", pady=(0, 5))
        tk.Button(frame, bg="white", font=self.master.btn_font, text="Return to start page",
                  command=lambda: self.master.switch_frame(StP.StartPage), width=30).pack(side="top")
