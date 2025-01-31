import tkinter as tk
from tkinter import messagebox
import random

class NonLosingLottery:
    def __init__(self, ticket_price, prize_cost, draws):
        self.ticket_price = ticket_price
        self.initial_prize_cost = prize_cost
        self.prize_cost = prize_cost
        self.draws = draws
        self.tickets_sold = 0
        self.total_revenue = 0
        self.total_prizes_paid = 0
        self.total_prizes_count = 0
        self.participants = {}
        self.draw_results = []
        self.first_additional_prize_draw = None

    def sell_tickets(self, num_tickets):
        for i in range(1, num_tickets + 1):
            ticket_id = f"Билет_{i}"
            self.participants[ticket_id] = 0
        self.tickets_sold += num_tickets
        self.total_revenue += num_tickets * self.ticket_price

    def conduct_draw(self, draw_number):
        if not self.participants:
            raise ValueError("No tickets sold. Cannot conduct draw.")

        additional_prizes = 0
        for ticket in list(self.participants.keys()):
            while self.participants[ticket] >= self.prize_cost * 1.2:
                self.total_prizes_paid += self.prize_cost
                self.total_prizes_count += 1
                additional_prizes += 1
                self.participants[ticket] -= self.prize_cost * 1.2
                if self.first_additional_prize_draw is None:
                    self.first_additional_prize_draw = draw_number

        eligible_tickets = [ticket for ticket, accumulation in self.participants.items() if accumulation < self.prize_cost * 1.2]
        if not eligible_tickets:
            eligible_tickets = list(self.participants.keys())

        winner = random.choice(eligible_tickets)

        self.total_prizes_paid += self.prize_cost
        self.total_prizes_count += 1
        self.participants[winner] = 0

        for ticket in self.participants.keys():
            if ticket != winner:
                self.participants[ticket] += self.ticket_price

        draw_result = {
            "draw_number": draw_number,
            "winner": winner,
            "additional_prizes": additional_prizes,
            "ticket_accumulations": dict(self.participants),
            "prizes_paid": self.total_prizes_paid,
            "prizes_count": self.total_prizes_count
        }
        self.draw_results.append(draw_result)

    def calculate_total_accumulations(self):
        return sum(self.participants.values())

    def calculate_profit_or_loss(self):
        return (self.total_revenue * self.draws) - self.total_prizes_paid

    def run_lottery(self):
        for draw_number in range(1, self.draws + 1):
            self.conduct_draw(draw_number)

    def get_status(self):
        total_accumulations = self.calculate_total_accumulations()
        status_lines = [
            f"Общий доход от билетов: {self.total_revenue * self.draws}",
            f"Общая сумма выплаченных призов: {self.total_prizes_paid}",
            f"Чистая прибыль/убыток: {self.calculate_profit_or_loss()}",
            f"Количество выданных призов: {self.total_prizes_count}",
            f"Общая сумма накоплений по невыигравшим билетам: {total_accumulations}",
            "Результаты по каждому розыгрышу:",
        ]
        for result in self.draw_results:
            status_lines.append(f"  Розыгрыш {result['draw_number']}:")
            status_lines.append(f"    Победитель: {result['winner']}")
            status_lines.append(f"    Дополнительных призов выдано: {result['additional_prizes']}")
            status_lines.append(f"    Суммарно выплачено призов на данный момент: {result['prizes_paid']}")
            status_lines.append(f"    Количество призов на данный момент: {result['prizes_count']}")
            for ticket, accumulation in result["ticket_accumulations"].items():
                status_lines.append(f"      {ticket}: {accumulation}")
        if self.first_additional_prize_draw:
            status_lines.append(f"Первый дополнительный приз был выплачен в розыгрыше: {self.first_additional_prize_draw}")
        else:
            status_lines.append("Дополнительные призы не были выплачены.")
        return "\n".join(status_lines)

    def get_draw_info(self, draw_number):
        if draw_number < 1 or draw_number > len(self.draw_results):
            return None
        return self.draw_results[draw_number - 1]

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лотерея")

        tk.Label(root, text="Стоимость одного билета:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(root, text="Количество проданных билетов:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(root, text="Начальная стоимость приза:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(root, text="Количество розыгрышей:").grid(row=3, column=0, sticky=tk.W)

        self.ticket_price_entry = tk.Entry(root)
        self.num_tickets_entry = tk.Entry(root)
        self.prize_cost_entry = tk.Entry(root)
        self.draws_entry = tk.Entry(root)

        self.ticket_price_entry.grid(row=0, column=1)
        self.num_tickets_entry.grid(row=1, column=1)
        self.prize_cost_entry.grid(row=2, column=1)
        self.draws_entry.grid(row=3, column=1)

        self.run_button = tk.Button(root, text="Запустить лотерею", command=self.run_lottery)
        self.run_button.grid(row=4, column=0, columnspan=2)

        tk.Label(root, text="Введите номер розыгрыша:").grid(row=5, column=0, sticky=tk.W)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=5, column=1, sticky="ew")

        self.search_button = tk.Button(root, text="Поиск розыгрыша", command=self.search_draw)
        self.search_button.grid(row=6, column=0, columnspan=2)

        self.result_frame = tk.Frame(root)
        self.result_frame.grid(row=7, column=0, columnspan=2, sticky="nsew")

        self.result_text = tk.Text(self.result_frame, height=20, width=60, wrap=tk.WORD)
        self.scrollbar = tk.Scrollbar(self.result_frame, orient="vertical", command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=self.scrollbar.set)

        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        root.grid_rowconfigure(7, weight=1)
        root.grid_columnconfigure(1, weight=1)
        self.result_frame.grid_rowconfigure(0, weight=1)
        self.result_frame.grid_columnconfigure(0, weight=1)

        self.root.bind('<Return>', self.handle_enter)

    def handle_enter(self, event):
        self.run_lottery()

    def run_lottery(self):
        try:
            ticket_price = float(self.ticket_price_entry.get())
            num_tickets = int(self.num_tickets_entry.get())
            prize_cost = float(self.prize_cost_entry.get())
            draws = int(self.draws_entry.get())

            self.lottery = NonLosingLottery(ticket_price, prize_cost, draws)
            self.lottery.sell_tickets(num_tickets)
            self.lottery.run_lottery()

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, self.lottery.get_status())

            if self.lottery.first_additional_prize_draw:
                messagebox.showinfo("Информация", f"Первый дополнительный приз был выплачен в розыгрыше: {self.lottery.first_additional_prize_draw}")
            else:
                messagebox.showinfo("Информация", "Дополнительные призы не были выплачены.")

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные значения.")

    def search_draw(self):
        try:
            draw_number = int(self.search_entry.get())
            if not hasattr(self, 'lottery') or not self.lottery:
                messagebox.showerror("Ошибка", "Сначала запустите лотерею.")
                return

            draw_info = self.lottery.get_draw_info(draw_number)
            if draw_info:
                info = [
                    f"Розыгрыш {draw_info['draw_number']}:",
                    f"Победитель: {draw_info['winner']}",
                    f"Дополнительных призов выдано: {draw_info['additional_prizes']}",
                    f"Суммарно выплачено призов на данный момент: {draw_info['prizes_paid']}",
                    f"Количество призов на данный момент: {draw_info['prizes_count']}",
                ]
                for ticket, accumulation in draw_info["ticket_accumulations"].items():
                    info.append(f"  {ticket}: {accumulation}")
                messagebox.showinfo("Информация о розыгрыше", "\n".join(info))
            else:
                messagebox.showerror("Ошибка", "Розыгрыш с указанным номером не найден.")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректный номер розыгрыша.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()
