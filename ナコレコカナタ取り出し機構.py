import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import pyperclip

file_mapping = {
    "COEIROINK-RECO": "レコ nc257937 im10866915 nc259840 nc250184 ",
    "COEIROINK-NAKO": "ナコ nc257937 im10866912  nc259839 nc260220",
    "COEIROINK-KANATA": "カナタ nc257937 im10880049 nc261967 nc281035",
    "COEIROINK_KANATA_YOUNG": "カナタヤング nc257937 im11228632 nc259840",
    "COEIROINK_NAKO_YOUNG": "ナコヤング nc257937 im11228632 nc259839",
    "COEIROINK_RECO_YOUNG": "レコヤング nc257937 im11228632 nc261967",
    "COEIROINK-ARMA-": "アルマ nc257937 im10962933 nc266214",
    "COEIROINK-DIA-": "ディア nc257937 im10962928 nc266214",
    "COEIROINK-KANA-": "KANA nc257937 im11223735 nc281340",
    "COEIROINK-MANA-": "MANA im11223723 nc260220",
    "COEIROINK-SHIA-": "花撫シア im11364648 nc297761",
    "MATSUKA": "松嘩りすく im11062780 nc282245",
    "Tsukuyomichan_NONOnext_": "つくよみちゃん im10977012 nc250184"
}

def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                output_text.delete(1.0, tk.END)
                for file_name, label in file_mapping.items():
                    if file_name in content:
                        output_text.insert(tk.END, f" {label} \n")
        except FileNotFoundError:
            output_text.insert(tk.END, f"ファイル '{file_path}' が見つかりませんでした。\n")
        except Exception as e:
            output_text.insert(tk.END, f"エラーが発生しました: {e}\n")

def copy_to_clipboard():
    text_to_copy = output_text.get(1.0, tk.END)
    pyperclip.copy(text_to_copy)
    messagebox.showinfo("コピー完了", "テキストをクリップボードにコピーしました。")

# GUIの作成
root = tk.Tk()
root.title("ファイル読み込み")

# ファイル読み込みボタン
load_button = tk.Button(root, text="ファイルを選択", command=load_file)
load_button.pack(pady=5)

# 出力テキストエリア
output_text = tk.Text(root, height=10, width=50)
output_text.pack(padx=10, pady=5)

# コピーボタン
copy_button = tk.Button(root, text="コピー", command=copy_to_clipboard)
copy_button.pack(pady=5)

root.mainloop()
