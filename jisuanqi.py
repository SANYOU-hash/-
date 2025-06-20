import tkinter as tk
from tkinter import ttk

# 多語言字典
LANGUAGES = {
    "English": {
        "title": "Life Utility Tool",
        "bmi": "BMI Calculator",
        "distance": "Distance (km)",
        "fuel_price": "Fuel Price (per liter)",
        "fuel_calc": "Fuel Cost Calculator",
        "unit_conv": "Unit Converter",
        "km": "Kilometers",
        "mi": "Miles",
        "height": "Height (cm)",
        "weight": "Weight (kg)",
        "calculate": "Calculate",
        "result": "Result",
        "language": "Language"
    },
    "繁體中文": {
        "title": "生活工具箱",
        "bmi": "BMI 計算機",
        "distance": "距離（公里）",
        "fuel_price": "油價（每公升）",
        "fuel_calc": "油費計算器",
        "unit_conv": "單位轉換器",
        "km": "公里",
        "mi": "英里",
        "height": "身高（公分）",
        "weight": "體重（公斤）",
        "calculate": "計算",
        "result": "結果",
        "language": "語言"
    },
    "简体中文": {
        "title": "生活工具箱",
        "bmi": "BMI 计算器",
        "distance": "距离（公里）",
        "fuel_price": "油价（每升）",
        "fuel_calc": "油费计算器",
        "unit_conv": "单位转换器",
        "km": "公里",
        "mi": "英里",
        "height": "身高（厘米）",
        "weight": "体重（公斤）",
        "calculate": "计算",
        "result": "结果",
        "language": "语言"
    }
}

class LifeToolApp:
    def __init__(self, root):
        self.root = root
        self.language = "English"
        self.strings = LANGUAGES[self.language]

        self.root.title(self.strings["title"])
        self.root.geometry("400x500")

        self.create_widgets()

    def create_widgets(self):
        self.language_menu = ttk.Combobox(self.root, values=list(LANGUAGES.keys()))
        self.language_menu.set(self.language)
        self.language_menu.pack()
        self.language_menu.bind("<<ComboboxSelected>>", self.change_language)

        # BMI 計算
        ttk.Label(self.root, text=self.strings["bmi"]).pack(pady=5)
        self.height_entry = ttk.Entry(self.root)
        self.height_entry.pack()
        self.weight_entry = ttk.Entry(self.root)
        self.weight_entry.pack()
        self.bmi_button = ttk.Button(self.root, text=self.strings["calculate"], command=self.calc_bmi)
        self.bmi_button.pack()
        self.bmi_result = ttk.Label(self.root, text="")
        self.bmi_result.pack()

        # 油費計算
        ttk.Label(self.root, text=self.strings["fuel_calc"]).pack(pady=5)
        self.distance_entry = ttk.Entry(self.root)
        self.distance_entry.pack()
        self.fuel_price_entry = ttk.Entry(self.root)
        self.fuel_price_entry.pack()
        self.fuel_button = ttk.Button(self.root, text=self.strings["calculate"], command=self.calc_fuel)
        self.fuel_button.pack()
        self.fuel_result = ttk.Label(self.root, text="")
        self.fuel_result.pack()

        # 單位轉換
        ttk.Label(self.root, text=self.strings["unit_conv"]).pack(pady=5)
        self.km_entry = ttk.Entry(self.root)
        self.km_entry.pack()
        self.km_to_mi_button = ttk.Button(self.root, text=f"{self.strings['km']} → {self.strings['mi']}", command=self.km_to_mi)
        self.km_to_mi_button.pack()
        self.mi_result = ttk.Label(self.root, text="")
        self.mi_result.pack()

    def change_language(self, event):
        self.language = self.language_menu.get()
        self.strings = LANGUAGES[self.language]
        self.update_labels()

    def update_labels(self):
        self.root.title(self.strings["title"])
        self.bmi_button.config(text=self.strings["calculate"])
        self.fuel_button.config(text=self.strings["calculate"])
        self.km_to_mi_button.config(text=f"{self.strings['km']} → {self.strings['mi']}")

    def calc_bmi(self):
        try:
            h = float(self.height_entry.get()) / 100
            w = float(self.weight_entry.get())
            bmi = round(w / (h ** 2), 2)
            self.bmi_result.config(text=f"{self.strings['result']}: {bmi}")
        except:
            self.bmi_result.config(text="Invalid input.")

    def calc_fuel(self):
        try:
            d = float(self.distance_entry.get())
            p = float(self.fuel_price_entry.get())
            fuel_used = d / 12  # 假設12 km/l
            cost = round(fuel_used * p, 2)
            self.fuel_result.config(text=f"{self.strings['result']}: {cost}")
        except:
            self.fuel_result.config(text="Invalid input.")

    def km_to_mi(self):
        try:
            km = float(self.km_entry.get())
            miles = round(km * 0.621371, 2)
            self.mi_result.config(text=f"{self.strings['result']}: {miles} mi")
        except:
            self.mi_result.config(text="Invalid input.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LifeToolApp(root)
    root.mainloop()
