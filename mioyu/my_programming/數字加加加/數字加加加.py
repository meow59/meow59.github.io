class game():
    import tkinter as tk
    from tkinter import messagebox as msg
    btns = {}
    total_sum = 0
    done = False
    def rand4(self, goal=10):
        _n24_ = r.randint(2, 4)
        numbers = [r.randint(goal//4, int(goal * (0.6-((goal-10)/112))))]
        numbers.append(int((goal-numbers[0])/_n24_-1))
        if _n24_ == 3:
            numbers.append(goal-numbers[0]-numbers[1])
            numbers.append(r.randint(2, 9))
        elif _n24_ == 4:
            numbers.append(r.randint(1, numbers[0]+numbers[1]-1))
            numbers.append(goal-sum(numbers))
        else:
            numbers.append(r.randint(1, 8))
            numbers.append(r.randint(2, 9))
        if 0 in numbers or sum([numbers[i] for i in range(_n24_)]) != goal:
            numbers = self.rand4(goal)
        r.shuffle(numbers)
        return numbers
    
    def update(self, root, x, y, goal):
        def minus1():
            self.remaining -= 1
            self.r_label.config(text='剩下' + str(self.remaining) + '題')
            if self.remaining == 0:
                self.game_over()
        if self.total_sum != goal:
            if self.btns[x, y]['fg'] != '#000000':
                self.btns[x, y]['bg'] = self.btns[x, y]['fg']
                self.btns[x, y]['fg'] = '#000000'
                self.total_sum += int(self.btns[x, y]['text'])
            else:
                self.btns[x, y]['fg'] = self.btns[x, y]['bg']
                self.btns[x, y]['bg'] = '#eeeeee'
                self.total_sum -= int(self.btns[x, y]['text'])
            self.goal_label.config(text=str(self.total_sum)+'/'+str(goal))
            if self.total_sum == goal:
                self.goal_label.config(fg='#00ff00')
                self.btns[x, y].after(300, lambda goal=goal: self.goal_label.config(text='0'+'/'+str(goal)))
                self.btns[x, y].after(300, lambda goal=goal: self.goal_label.config(fg='#000000'))
                self.goal_label.after(300, lambda root=root, goal=goal: self.next_1(root, goal))
                self.goal_label.after(300, minus1)
    def next_1(self, root, goal=10):
        numbers = self.rand4(goal)
        colors = ['#28c8ff', '#ff2828', '#00ff00', '#ffc90e']
        r.shuffle(colors)
        c = 0
        self.total_sum = 0
        for bx in range(2):
            for by in range(2):
                btn = tk.Button(root, text=str(numbers[c]), fg=colors.pop(), width=3, height=2, \
                                font=('微軟正黑體', 16), command=lambda x=bx, y=by: self.update(root, x, y, goal))
                btn.grid(column=bx, row=by, padx=5, pady=5)
                self.btns[bx, by] = btn
                c += 1

    def updatetime(self, start, time):
        def roundplus(x, y=0):
            for a in list(range(y)):
                x *= 10
            ret = divmod(x, 1)
            if ret[1] != 0:
                x = ret[0] + 1
            for a in list(range(y)):
                x /= 10
            if x == int(x):
                x = int(x)
            return x
        if self.remaining != 0:
            now_time = t.perf_counter()
            self.tr_label.config(text='⏰%3.1f' % (roundplus(time-(now_time-start), 1)))
            if roundplus(time-(now_time-start), 1) <= 0:
                self.game_over()
            else: self.tr_label.after(1, lambda start=start, time=time: self.updatetime(start, time))
        
    def game_start(self, difficulty=1):
        self.remaining = 20
        self.time = 55 + 5 * difficulty
        self.root = tk.Tk()
        self.root.title('數字加加加')
        
        goal = 5 + int(difficulty) * 5
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=0, column=0, rowspan=5)
        self.goal_label = tk.Label(self.root, text='0/' + str(goal), font=('微軟正黑體', 12))
        self.r_label = tk.Label(self.root, text='剩下' + str(self.remaining) + '題', font=('微軟正黑體', 12))
        self.tr_label = tk.Label(self.root, text='⏰%3.1f' % (self.time), font=('微軟正黑體', 12))
        self.goal_label.grid(row=0, column=1)
        self.r_label.grid(row=3, column=1)
        self.tr_label.grid(row=4, column=1)
        tk.Label(self.root, text='#By 喵小羽32', fg = '#82e2ff', font=('微軟正黑體', 12)).grid(row=4, column=2)
        t.sleep(1)
        self.start = t.perf_counter()
        self.next_1(btn_frame, goal)
        self.updatetime(self.start, self.time)
        self.root.mainloop()

    def game_restart(self, difficulty=1):
        self.remaining = 20
        self.time = 55 + 5 * difficulty
        
        goal = 5 + int(difficulty) * 5
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=0, column=0, rowspan=5)
        self.goal_label = tk.Label(self.root, text='0/' + str(goal), font=('微軟正黑體', 12))
        self.r_label = tk.Label(self.root, text='剩下' + str(self.remaining) + '題', font=('微軟正黑體', 12))
        self.tr_label = tk.Label(self.root, text='⏰%3.1f' % (self.time), font=('微軟正黑體', 12))
        self.goal_label.grid(row=0, column=1)
        self.r_label.grid(row=3, column=1)
        self.tr_label.grid(row=4, column=1)
        tk.Label(self.root, text='#By 喵小羽32', fg = '#82e2ff', font=('微軟正黑體', 12)).grid(row=4, column=2)
        t.sleep(1)
        self.start = t.perf_counter()
        self.next_1(btn_frame, goal)
        self.updatetime(self.start, self.time)
        self.root.mainloop()

    def game_over(self):
        if self.remaining <= 0:
            msg.showinfo('數字加加加', '分數： %4.2f秒' % (t.perf_counter()-self.start))
        else:
            msg.showinfo('數字加加加', '分數： %d題' % (20 - self.remaining))
        again = msg.askyesno('數字加加加', '再玩一次？')
        if again: self.game_restart()
        else:
            self.root.withdraw()
            quit()
            print('請關掉此視窗')

import tkinter as tk
from tkinter import messagebox as msg
import random as r
import time as t

g=game()
g.game_start()
