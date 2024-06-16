import time
import pip
import random

try:
    import tkinter as tk
    import customtkinter as ctk
except Exception as err:
    print(err)
    print("Módulos não encontrado... Tentativa de baixar em 3 Segundos")
    time.sleep(3)
    pip.main(["install", "customtkinter"])
    pip.main(["install", "tkinter"])
else:
    from tkinter import messagebox
    from tkinter import *

if __name__ == "__main__":
    main_w = ctk.CTk()

    class App():
        def __init__(self):
            self.tela_conf()
            self.main_frame()
            main_w.mainloop()
        
        def tela_conf(self):
            main_w.geometry("600x600")
            main_w.resizable(False,False)
            main_w.title("Py-X")
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
        
        def main_frame(self):
            
            global n1
            global n2
            n1 = random.randint(0, 10)
            n2 = random.randint(0, 10)
            global result
            result = int(n1 * n2)
            global respostas_corretas
            respostas_corretas = 0

            def confere_re():
                resposta = re_entry.get().isdigit()
                global n1
                global n2
                global result
                global respostas_corretas
                
                if resposta:
                    resposta = int(resposta)
                    if int(re_entry.get()) == result:
                        quest_label.configure(text_color="green")
                        quest_label.update()
                        time.sleep(1)
                        n1 = random.randint(0, 10)
                        n2 = random.randint(0, 10)
                        result = int(n1 * n2)
                        quest_label.configure(text=f"{n1} x {n2} = ?", text_color="white")
                        quest_label.update()
                        re_entry.delete(0, END)
                        print(n1, n2, result)
                        respostas_corretas += 1
                        quan_resposta.configure(text=f"Acertos: {respostas_corretas}")
                    else:
                        quest_label.configure(text_color="red")
                        quest_label.update()
                        time.sleep(1)
                        n1 = random.randint(0, 10)
                        n2 = random.randint(0, 10)
                        result = int(n1 * n2)
                        quest_label.configure(text=f"{n1} x {n2} = ?", text_color="white")
                        quest_label.update()
                        re_entry.delete(0, END)
                        print(n1, n2, result)
                        
                else:
                    quest_label.configure(text_color="red")
                    quest_label.update()
                    time.sleep(1)
                    n1 = random.randint(0, 10)
                    n2 = random.randint(0, 10)
                    result = int(n1 * n2)
                    quest_label.configure(text=f"{n1} x {n2} = ?", text_color="white")
                    quest_label.update()
                    re_entry.delete(0, END) 
                    print(n1, n2, result)           

            main_f = ctk.CTkFrame(master=main_w, width=500, height=600)
            main_f.pack()


            #/-/-/-/Frame da Pergunta/-/-/-/
            sub_frame1 = ctk.CTkFrame(master=main_f, width=500, height=200)
            sub_frame1.place(relx=0, rely=0.03)

            quest_label = ctk.CTkLabel(master=sub_frame1, text=f"{n1} x {n2} = ?", text_color="white", font=("Courier New", 50, "bold"))
            quest_label.place(relx=0.5, rely=0.5, anchor="center")


            #/-/-/-/Frame da Resposta/-/-/-/
            
                    
                    
                
               

            sub_frame2 = ctk.CTkFrame(master=main_f, width=500, height=340)
            sub_frame2.place(relx=0, rely=0.4)

            re_label = ctk.CTkLabel(master=sub_frame2, text="Digite sua resposta:", font=("Courier New", 30, "bold"))
            re_label.place(relx=0.5, rely=0.15, anchor="center")

            re_entry = ctk.CTkEntry(master=sub_frame2, placeholder_text="...", font=("Courie New", 40, "bold"), width=100, height=100)
            re_entry.place(relx=0.5, rely=0.4, anchor="center")

            re_buttom = ctk.CTkButton(master=sub_frame2, text="Responder", font=("Courier New", 30, "bold"), width=200, height=50, command=confere_re)
            re_buttom.place(relx=0.5, rely=0.7, anchor="center")

            quan_resposta = ctk.CTkLabel(master=sub_frame2, text=f"Acertos: {respostas_corretas}", font=("Courier New", 20, "bold"))
            quan_resposta.place(relx=0.5, rely=0.9, anchor="center")



    App()
