import tkinter as tk
import time

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    selected_coins = [[] for _ in range(amount + 1)]

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                selected_coins[i] = selected_coins[i - coin] + [coin]

    return dp, selected_coins

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp

class DynamicProgrammingApp:
    def __init__(self, master):
        self.master = master
        master.title("Dynamic Programming Showcase")

        master.configure(bg="deepskyblue")

        self.fibonacci_label = tk.Label(master, text="Enter the number of terms for Fibonacci:", bg="deepskyblue")
        self.fibonacci_label.pack()
        self.fibonacci_entry = tk.Entry(master)
        self.fibonacci_entry.pack()
        self.calculate_fibonacci_button = tk.Button(master, text="Calculate Fibonacci", command=self.calculate_fibonacci, bg="#4CAF50", fg="white")
        self.calculate_fibonacci_button.pack()
        self.fibonacci_result_label = tk.Label(master, text="", bg="deepskyblue")
        self.fibonacci_result_label.pack()

        # Coin Change Section
        self.coin_label = tk.Label(master, text="Enter coins (comma-separated) and amount for Coin Change:", bg="deepskyblue")
        self.coin_label.pack()
        self.coin_coins_entry = tk.Entry(master)
        self.coin_coins_entry.pack()
        self.coin_amount_entry = tk.Entry(master)
        self.coin_amount_entry.pack()
        self.calculate_coin_button = tk.Button(master, text="Calculate Coin Change", command=self.calculate_coin, bg="#4CAF50", fg="white")
        self.calculate_coin_button.pack()
        self.coin_result_label = tk.Label(master, text="", bg="deepskyblue")
        self.coin_result_label.pack()

        # Knapsack Section
        self.knapsack_label = tk.Label(master, text="Enter weights (comma-separated), values (comma-separated), and capacity for Knapsack:", bg="deepskyblue")
        self.knapsack_label.pack()
        self.knapsack_weights_entry = tk.Entry(master)
        self.knapsack_weights_entry.pack()
        self.knapsack_values_entry = tk.Entry(master)
        self.knapsack_values_entry.pack()
        self.knapsack_capacity_entry = tk.Entry(master)
        self.knapsack_capacity_entry.pack()
        self.calculate_knapsack_button = tk.Button(master, text="Calculate Knapsack", command=self.calculate_knapsack, bg="#4CAF50", fg="white")
        self.calculate_knapsack_button.pack()
        self.knapsack_result_label = tk.Label(master, text="", bg="deepskyblue")
        self.knapsack_result_label.pack()
        self.knapsack_table_label = tk.Label(master, text="", bg="deepskyblue")
        self.knapsack_table_label.pack()

        
        self.trace_text = tk.Text(master, height=10, width=50, state=tk.DISABLED, bg="#FFFFFF")
        self.trace_text.pack(pady=10)

        
        self.result_labels = [
            self.fibonacci_result_label,
            self.coin_result_label,
            self.knapsack_result_label,
        ]

    def calculate_fibonacci(self):
        try:
            
            self.clear_results()

            n = int(self.fibonacci_entry.get())
            fib_sequence = fibonacci(n)
            self.fibonacci_result_label.config(text=f"Fibonacci Sequence: {fib_sequence}")
            self.show_tracefib(n)

        except ValueError:
            self.fibonacci_result_label.config(text="Please enter a valid number.")

    def calculate_coin(self):
        try:
            
            self.clear_results()

            coins = list(map(int, self.coin_coins_entry.get().split(',')))
            amount = int(self.coin_amount_entry.get())
            min_coins, selected_coins = coin_change(coins, amount)
            self.coin_result_label.config(text=f"Minimum number of coins needed: {min_coins[amount]}")
            self.show_tracecoin(selected_coins)

        except ValueError:
            self.coin_result_label.config(text="Please enter valid input.")

    def calculate_knapsack(self):
        try:
            
            self.clear_results()

            weights = list(map(int, self.knapsack_weights_entry.get().split(',')))
            values = list(map(int, self.knapsack_values_entry.get().split(',')))
            capacity = int(self.knapsack_capacity_entry.get())
            dp = knapsack(weights, values, capacity)
            self.knapsack_result_label.config(text=f"Maximum Value: {dp[-1][-1]}")
            self.show_knapsack_table(dp)
            self.show_trace(weights, values, dp, capacity)

        except ValueError:
            self.knapsack_result_label.config(text="Please enter valid input.")

    def clear_results(self):
        # Clear all result labels and trace text
        for label in self.result_labels:
            label.config(text="")

        self.clear_trace_text()

    def clear_trace_text(self):
        # Clear the trace text widget
        self.trace_text.config(state=tk.NORMAL)
        self.trace_text.delete("1.0", tk.END)
        self.trace_text.config(state=tk.DISABLED)

    def show_tracefib(self, n):
        trace_text = "Fibonacci Trace:\n"
        a = 0
        b = 1
        f = 0
        trace_text += f" term 1 :{a}\n"
        trace_text += f" term 2 : {a}+{b}={a+b}\n"

        self.trace_text.config(state=tk.NORMAL)
        self.trace_text.delete("1.0", tk.END)
        self.trace_text.insert(tk.END, trace_text)
        self.master.update_idletasks()
        time.sleep(1.5)

        for i in range(n - 1):
            trace_text += f" term {i + 3} : {a}+{b}={a + b}\n"
            d = a + b
            a, b = b, d

            self.trace_text.config(state=tk.NORMAL)
            self.trace_text.delete("1.0", tk.END)
            self.trace_text.insert(tk.END, trace_text)
            self.master.update_idletasks()
            time.sleep(1.5)

        self.trace_text.config(state=tk.DISABLED)

    def show_trace(self, weights, values, dp, capacity):
        n = len(dp) - 1
        w = capacity
        trace = []

        while n > 0 and w > 0:
            if dp[n][w] != dp[n - 1][w]:
                item_weight = weights[n - 1]
                item_value = values[n - 1]

                trace.append("Updated Knapsack Table:")
                for row in dp:
                    trace.append(str(row))
                trace.append("\n")

                trace.append(f"Include item {n - 1} (weight={item_weight}, value={item_value})")
                n -= 1
                w -= item_weight
            else:
                trace.append("Unchanged Knapsack Table:")
                for row in dp:
                    trace.append(str(row))
                trace.append("\n")

                trace.append(f"Exclude item {n - 1}")
                n -= 1

        trace.append("Initial Knapsack Table:")
        for row in dp:
            trace.append(str(row))
        trace.append("\n")

        trace.reverse()

        self.trace_text.config(state=tk.NORMAL)
        self.trace_text.delete("1.0", tk.END)

        remaining_capacity = capacity
        for step in trace:
            self.trace_text.insert(tk.END, f"{step}\n")
            if "Include" in step:
                remaining_capacity -= item_weight
                self.trace_text.insert(tk.END, f"Current remaining capacity: {remaining_capacity}\n")
            self.master.update_idletasks()
            time.sleep(0.5)

        self.trace_text.config(state=tk.DISABLED)


    def show_tracecoin(self, selected_coins):
        trace_text = "Coin Change Trace:\n"

        def show_step(step_index):
            nonlocal trace_text

            if step_index < len(selected_coins):
                coins = selected_coins[step_index]
                if coins:
                    trace_text += f"Amount {step_index}: Selected coins: {coins}\n"
                else:
                    trace_text += f"Amount {step_index}: No selected coins\n"

            
            self.trace_text.config(state=tk.NORMAL)
            self.trace_text.delete("1.0", tk.END)
            self.trace_text.insert(tk.END, trace_text)
            self.trace_text.config(state=tk.DISABLED)

            self.master.after(1500, show_step, step_index + 1)

        show_step(0)

    def show_knapsack_table(self, dp):
        table_text = "Optimal Solution Table:\n"
        for i, row in enumerate(dp):
            table_text += f"Stage {i}: " + " | ".join(map(str, row)) + "\n"
        self.knapsack_table_label.config(text=table_text)


root = tk.Tk()
app = DynamicProgrammingApp(root)
root.mainloop()

