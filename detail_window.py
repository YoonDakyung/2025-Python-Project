import tkinter as tk
from tkinter import scrolledtext
from worry_logic import get_worry_by_id, get_comments, add_comment, increase_empathy

class DetailWindow:
    def __init__(self, parent, worry_id, refresh_callback):
        self.top = tk.Toplevel(parent)
        self.top.title("고민 상세 보기")
        self.top.geometry("500x600")
        self.top.configure(bg="#FFF5E5")

        self.worry_id = worry_id
        self.refresh_callback = refresh_callback

        self.title_label = tk.Label(self.top, text="", font=("맑은 고딕", 13, "bold"), bg="#FFF5E5")
        self.title_label.pack(pady=10)

        self.content_label = tk.Label(self.top, text="", wraplength=450, justify="left", bg="#FFF5E5")
        self.content_label.pack(pady=10)

        self.empathy_btn = tk.Button(self.top, text="❤️ 공감하기", command=self.empathize)
        self.empathy_btn.pack(pady=5)

        tk.Label(self.top, text="💬 댓글", bg="#FFF5E5", font=("맑은 고딕", 11, "bold")).pack(pady=5)

        self.comments_box = scrolledtext.ScrolledText(self.top, width=60, height=10)
        self.comments_box.pack()
        self.comments_box.config(state="disabled")

        self.comment_entry = tk.Text(self.top, height=3, width=40)
        self.comment_entry.pack(pady=5)

        tk.Button(self.top, text="등록", command=self.add_comment).pack()

        self.load_worry()

    def load_worry(self):
        worry = get_worry_by_id(self.worry_id)
        self.title_label.config(text=f"[{worry[1]} / {worry[2]}] 고민")
        self.content_label.config(text=worry[3])

        self.comments_box.config(state="normal")
        self.comments_box.delete("1.0", tk.END)
        for c in get_comments(self.worry_id):
            self.comments_box.insert(tk.END, f"🗨 {c[0]}\n")
        self.comments_box.config(state="disabled")

    def add_comment(self):
        content = self.comment_entry.get("1.0", tk.END).strip()
        if content:
            add_comment(self.worry_id, content)
            self.comment_entry.delete("1.0", tk.END)
            self.load_worry()

    def empathize(self):
        increase_empathy(self.worry_id)
        self.refresh_callback()
        self.load_worry()