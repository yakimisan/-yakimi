import tkinter as tk
from tkinter import filedialog
import re

# ファイルを選択して正規表現を適用する関数
def process_file():
    # パターンを定義
    pattern = r'\\nc(\d+)'

    # ファイルダイアログを表示し、テキストファイルを選択
    file_path = filedialog.askopenfilename()

    if file_path:
        # エンコーディングエラーを無視してファイルを開く
        with open(file_path, 'r', errors='ignore') as file:
            result_text.delete(1.0, tk.END)  # 結果表示エリアをクリア
            # ファイルの全体を読み込み、マッチした数字を取得
            matches = re.findall(pattern, file.read())
            # 重複を削除
            unique_matches = list(set(matches))
            # マッチした数字を指定された形式で結果表示エリアに追加
            result_text.insert(tk.END, ' '.join(['nc' + match for match in unique_matches]))

# Tkinterウィンドウの設定
window = tk.Tk()
window.title("Regex Text File Processor")

# ファイルを選択するボタン
open_button = tk.Button(window, text="Open File", command=process_file)
open_button.pack()

# 結果を表示するテキストエリア
result_text = tk.Text(window, height=10, width=40)
result_text.pack()

# アプリケーションの実行
window.mainloop()
