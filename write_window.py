import tkinter as tk
from worry_logic import create_worry

class WriteWindow:
    def __init__(self, parent, refresh_callback):
        self.top = tk.Toplevel(parent)
        self.top.title("📝 고민 작성하기")
        self.top.geometry("400x400")
        self.top.configure(bg="#FFF4DC")
        self.refresh_callback = refresh_callback

        tk.Label(self.top, text="카테고리", bg="#FFF4DC").pack(pady=5)
        self.category = tk.StringVar()
        tk.OptionMenu(self.top, self.category, "학교", "가족", "친구", "연애", "기타").pack()

        tk.Label(self.top, text="감정", bg="#FFF4DC").pack(pady=5)
        self.emotion = tk.StringVar()
        tk.OptionMenu(self.top, self.emotion, "슬픔", "분노", "불안", "외로움", "기타").pack()

        tk.Label(self.top, text="고민 내용", bg="#FFF4DC").pack(pady=5)
        self.content_text = tk.Text(self.top, width=40, height=10)
        self.content_text.pack()

        tk.Button(self.top, text="등록", command=self.save).pack(pady=10)

    def save(self):
        create_worry(self.category.get(), self.emotion.get(), self.content_text.get("1.0", tk.END))
        self.refresh_callback()
        self.top.destroy()