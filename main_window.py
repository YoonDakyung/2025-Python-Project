import tkinter as tk
from tkinter import ttk
from worry_logic import get_all_worries
from write_window import WriteWindow
from detail_window import DetailWindow
from database import initialize_database

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("🌼 익명 고민 상담소")
        self.root.geometry("700x600")
        self.root.configure(bg="#FFF8E7")

        initialize_database()

        title = tk.Label(root, text="쉿! 비밀이야🤫", font=("맑은 고딕", 18, "bold"), bg="#FFF8E7")
        title.pack(pady=20)

        self.sort_var = tk.StringVar(value="최신순")
        sort_frame = tk.Frame(root, bg="#FFF8E7")
        sort_frame.pack(pady=5)
        tk.Label(sort_frame, text="정렬: ", bg="#FFF8E7").pack(side="left")
        ttk.Combobox(sort_frame, textvariable=self.sort_var, values=["최신순", "공감순"], width=10).pack(side="left")
        tk.Button(sort_frame, text="🔄 갱신", command=self.load_worries).pack(side="left", padx=5)

        self.listbox = tk.Listbox(root, width=80, height=20, font=("맑은 고딕", 11))
        self.listbox.pack(pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.open_detail)

        btn_frame = tk.Frame(root, bg="#FFF8E7")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="📝 고민 작성", command=self.open_write_window).pack()

        self.load_worries()

    def load_worries(self):
        self.listbox.delete(0, tk.END)
        sort_key = "created_at DESC" if self.sort_var.get() == "최신순" else "empathy DESC"
        self.worries = get_all_worries(order_by=sort_key)
        for w in self.worries:
            display = f"[{w[1]}/{w[2]}] {w[3][:30]}... (공감 {w[4]})"
            self.listbox.insert(tk.END, display)

    def open_write_window(self):
        WriteWindow(self.root, refresh_callback=self.load_worries)

    def open_detail(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        worry_id = self.worries[index][0]
        DetailWindow(self.root, worry_id, refresh_callback=self.load_worries)