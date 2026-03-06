import tkinter as tk
from tkinter import messagebox, ttk

TOURIST_SPOTS = [
    {"name": "Pashupatinath", "fee": 100, "time": 1.5, "interest": 9},
    {"name": "Swayambhunath", "fee": 200, "time": 2.0, "interest": 8},
    {"name": "Garden of Dreams", "fee": 150, "time": 1.0, "interest": 6},
    {"name": "Chandragiri Hills", "fee": 700, "time": 4.0, "interest": 10},
    {"name": "Patan Durbar Sq", "fee": 250, "time": 2.5, "interest": 8},
    {"name": "Boudhanath", "fee": 150, "time": 1.5, "interest": 7}
]

class TouristOptimizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Kathmandu Tourist Route Optimizer")
        self.root.geometry("500x500")

        tk.Label(root, text="Tourist Route Optimizer", font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Label(root, text="Total Budget (NPR):").pack()
        self.budget_entry = tk.Entry(root)
        self.budget_entry.pack()

        tk.Label(root, text="Total Time Available (Hours):").pack()
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        self.btn_optimize = tk.Button(root, text="Generate Optimal Route", command=self.optimize, bg="#4CAF50", fg="white")
        self.btn_optimize.pack(pady=20)

        # Output Display
        self.result_area = tk.Text(root, height=12, width=50)
        self.result_area.pack(pady=10)

    def optimize(self):
        try:
            budget = float(self.budget_entry.get())
            time_limit = float(self.time_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for budget and time.")
            return


        sorted_spots = sorted(
            TOURIST_SPOTS, 
            key=lambda x: x["interest"] / (x["fee"] + (x["time"] * 100)), 
            reverse=True
        )

        selected_route = []
        total_cost = 0
        total_time = 0
        total_interest = 0

        for spot in sorted_spots:
            if (total_cost + spot["fee"] <= budget) and (total_time + spot["time"] <= time_limit):
                selected_route.append(spot)
                total_cost += spot["fee"]
                total_time += spot["time"]
                total_interest += spot["interest"]

        self.result_area.delete('1.0', tk.END)
        if not selected_route:
            self.result_area.insert(tk.END, "No spots fit within your budget/time.")
        else:
            self.result_area.insert(tk.END, f"Suggested Itinerary:\n" + "-"*30 + "\n")
            for i, spot in enumerate(selected_route, 1):
                self.result_area.insert(tk.END, f"{i}. {spot['name']} ({spot['time']} hrs, {spot['fee']} NPR)\n")
            
            self.result_area.insert(tk.END, f"\n" + "-"*30 + "\n")
            self.result_area.insert(tk.END, f"Total Interest Score: {total_interest}\n")
            self.result_area.insert(tk.END, f"Total Cost: {total_cost} NPR\n")
            self.result_area.insert(tk.END, f"Total Time: {total_time} Hours")

if __name__ == "__main__":
    window = tk.Tk()
    app = TouristOptimizer(window)
    window.mainloop()