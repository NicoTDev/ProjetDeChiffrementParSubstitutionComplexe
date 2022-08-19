import tkinter as tk
import ChiffrementProgram
import DchiffrementProgram
import MakePaternProgram

class Application:
    #mettre toutes les variables ici
    window = None
    frame = None
    size_window = None
    #interface de base
    buttonCreateNewPatern = None
    buttonChiffrement = None
    buttonDechiffrement = None
    buttonQuit = None
    #interface du premier bouton (buttonCreateNewPatern)
    entryPatern = None
    entryFile = None
    labelFile = None
    labelPatern = None
    buttonCreate = None
    buttonBack = None
    #interface du deuxième bouton (chiffrer)
    entryKeyFile = None
    entryMessageFile = None
    labelfinalFile = None
    entryfinalFile = None
    buttonchiffrer = None
    #interface du troisième bouton (déchiffrer)
    buttondechiffrer = None
#créer les commandes:
 #pour les boutons de base
    #commande pour détruire les interface actuelles
            #détruire l'interface de base
    def destroy_all_default_compos(self):
        self.buttonCreateNewPatern.destroy()
        self.buttonChiffrement.destroy()
        self.buttonDechiffrement.destroy()
        self.buttonQuit.destroy()
    #commande pour chaque bouton
    def command_buttonQuit(self):
        self.window.destroy()
    def command_buttonCreateNewPatern(self):
        self.destroy_all_default_compos()
        self.entryPatern = tk.Entry(self.frame, bg="#000000",
                               fg="white", width=int(self.size_window[0] / 10))
        self.entryFile = tk.Entry(self.frame, bg="#000000",
                               fg="white", width=int(self.size_window[0] / 10))
        self.labelFile = tk.Label(self.frame,text="Entrez le nom du ficher (défaut=patern_file)", fg="green",bg="black")
        self.labelPatern = tk.Label(self.frame,text="Entrez le nombre de combinaison à créer", fg="green",bg="black")
        self.buttonCreate = tk.Button(self.frame, activebackground="#7bdb7c", bg="#00ff04",
                                 text="créer!",
                                 fg="#000000", anchor="center",
                                 height=int(self.size_window[1] / 100), width=int(self.size_window[0] / 10),
                                 command=self.command_buttonCreate)
        self.labelPatern.pack()
        self.entryPatern.pack()
        self.labelFile.pack()
        self.entryFile.pack()
        self.buttonCreate.pack()
        self.buttonBack = tk.Button(self.frame, activebackground="#fa4646", bg="#ff0000",
                                    text="Retour",
                                    fg="#000000", anchor="center",
                                    height=int(self.size_window[1] / 100), width=int(self.size_window[0] / 10),
                                    command=self.command_buttonBack)
        self.buttonBack.pack()
            #interface pour créer une nouvelle combinaison
    def command_buttonCreate(self):
        try:
            entryPaternValue = int(self.entryPatern.get())
            entryFileValue = str(self.entryFile.get())
            if len(entryFileValue) == 0:
                MakePaternProgram.Make_patern(number_of_patern=entryPaternValue)
            else:
                MakePaternProgram.Make_patern(file=entryFileValue,number_of_patern=entryPaternValue)
            self.command_buttonBack()
        except:
            pass
    def command_buttonBack(self):
        self.window.destroy()
        application.create_default_window([400, 600])
    def command_buttonChiffrerFin(self):
        try:
            ChiffrementProgram.chiffrer_un_message(self.entryMessageFile.get(),
                                                self.entryKeyFile.get(),
                                                self.entryfinalFile.get())
            self.command_buttonBack()
        except:
            pass
    def command_buttonChiffrer(self):
        self.destroy_all_default_compos()

        #création de la zone de texte 1
        self.labelFile = tk.Label(self.frame,text="Entrez le nom du ficher contenant le message à chiffrer",
                                  fg="green",bg="black")

        self.entryMessageFile = tk.Entry(self.frame, bg="#000000",
                                  fg="white", width=int(self.size_window[0] / 10))

        #création de la zone de texte 2
        self.labelKeyFile = tk.Label(self.frame, text="Entrez le nom du ficher contenant la clé (liste de combinaison)",
                                     fg="green", bg="black")
        self.entryKeyFile = tk.Entry(self.frame, bg="#000000",
                                     fg="white", width=int(self.size_window[0] / 10))
        #création de la zone de texte 2
        self.labelfinalFile = tk.Label(self.frame, text="Entrez le nom du ficher où le texte chiffré sera envoyé",
                                     fg="green", bg="black")
        self.entryfinalFile = tk.Entry(self.frame, bg="#000000",
                                     fg="white", width=int(self.size_window[0] / 10))
        #création du bouton "chiffrer le texte"
        self.buttonchiffrer = tk.Button(self.frame, activebackground="#7bdb7c", bg="#00ff04",
                                 text="chiffrer le message",
                                 fg="#000000", anchor="center",
                                 height=int(self.size_window[1] / 100), width=int(self.size_window[0] / 10),
                                 command=self.command_buttonChiffrerFin)
        #création du bouton "retour"
        self.buttonBack = tk.Button(self.frame, activebackground="#fa4646", bg="#ff0000",
                                    text="Retour",
                                    fg="#000000", anchor="center",
                                    height=int(self.size_window[1] / 100), width=int(self.size_window[0] / 10),
                                    command=self.command_buttonBack)

        self.labelFile.pack()
        self.entryMessageFile.pack()
        self.labelKeyFile.pack()
        self.entryKeyFile.pack()
        self.labelfinalFile.pack()
        self.entryfinalFile.pack()
        self.buttonchiffrer.pack()
        self.buttonBack.pack()
    def command_buttonDechiffrerFin(self):
        try:
            DchiffrementProgram.dechiffre_message(self.entryMessageFile.get(),self.entryKeyFile.get(), self.entryfinalFile.get())
            self.command_buttonBack()
        except:
            pass
    def command_buttonDechiffrer(self):
        self.destroy_all_default_compos()
        #créer la zone de texte 1
        self.labelFile = tk.Label(self.frame,text="Entrez le nom du ficher contenant le message à déchiffrer",
                                  fg="green",bg="black")
        self.entryMessageFile = tk.Entry(self.frame, bg="#000000",
                               fg="white", width=int(self.size_window[0] / 10))
        #création de la zone de texte 2
        self.labelKeyFile = tk.Label(self.frame, text="Entrez le nom du ficher contenant la clé (liste de combinaison)",
                                     fg="green", bg="black")
        self.entryKeyFile = tk.Entry(self.frame, bg="#000000",
                                     fg="white", width=int(self.size_window[0] / 10))
        #création de la zone de texte 2
        self.labelfinalFile = tk.Label(self.frame, text="Entrez le nom du ficher où le message déchiffré sera envoyé",
                                     fg="green", bg="black")
        self.entryfinalFile = tk.Entry(self.frame, bg="#000000",
                                     fg="white", width=int(self.size_window[0] / 10))

        #création du bouton "chiffrer le texte"
        self.buttondechiffrer = tk.Button(self.frame, activebackground="#7bdb7c", bg="#00ff04",
                                 text="Déchiffrer le message",
                                 fg="#000000", anchor="center",
                                 height=int(self.size_window[1] / 100), width=int(self.size_window[0] / 10),
                                 command=self.command_buttonDechiffrerFin)
        #création du bouton "retour"
        self.buttonBack = tk.Button(self.frame, activebackground="#fa4646", bg="#ff0000",
                                    text="Retour",
                                    fg="#000000", anchor="center",
                                    height=int(self.size_window[1] / 100), width=int(self.size_window[0] / 10),
                                    command=self.command_buttonBack)

        self.labelFile.pack()
        self.entryMessageFile.pack()
        self.labelKeyFile.pack()
        self.entryKeyFile.pack()
        self.labelfinalFile.pack()
        self.entryfinalFile.pack()
        self.buttondechiffrer.pack()
        self.buttonBack.pack()
    #créer la fenêtre principal
    def create_default_window(self, size_window: list, title: str = "interface"):
        #créer la fenêtre principale
        self.size_window = size_window
        window = tk.Tk()
        window.title(title)
        window.minsize(size_window[0], size_window[1])
        window.maxsize(size_window[0], size_window[1])
        window.configure(bg="black")
        self.frame = tk.Frame(window, bg="black", relief="raised", height=size_window[1], width=size_window[0])
        self.frame.pack()
        titre_label = tk.Label(self.frame,text="Console de Chiffrement NI", fg="green",bg="black", font=64, pady=64)
        titre_label.pack()
        self.window = window
        #créer les trois boutons par défaut
                #créer le bouton de combinaison
        self.buttonCreateNewPatern = tk.Button(self.frame, activebackground="#4fcaf0", bg="#03c2fc",
                                 text="créer une nouvelle combinaison",
                                 fg="#000000", anchor="center",
                                 height=int(size_window[1] / 100), width=int(size_window[0] / 10),
                                 command=self.command_buttonCreateNewPatern)
        self.buttonCreateNewPatern.pack()
                #créer le bouton pour chiffrer un message
        self.buttonChiffrement = tk.Button(self.frame, activebackground="#04c904", bg="#00ff00",
                                          text="Chiffrer un message",
                                          fg="#000000", anchor="center",
                                          height=int(size_window[1] / 100), width=int(size_window[0] / 10),
                                          command=self.command_buttonChiffrer)
        self.buttonChiffrement.pack()
                #créer le bouton pour déchiffrer un message
        self.buttonDechiffrement = tk.Button(self.frame, activebackground="#000000", bg="#2b2b2b",
                                          text="déchiffrer un message",
                                          fg="#ffffff", anchor="center",
                                          height=int(size_window[1] / 100), width=int(size_window[0] / 10),
                                          command=self.command_buttonDechiffrer)
        self.buttonDechiffrement.pack()
                #créer le bouton pour quitter
        self.buttonQuit = tk.Button(self.frame, activebackground="#fa4646", bg="#ff0000",
                                          text="Quitter",
                                          fg="#000000", anchor="center",
                                          height=int(size_window[1] / 100), width=int(size_window[0] / 10),
                                          command=self.command_buttonQuit)
        self.buttonQuit.pack()




#lancer le programme
application = Application()
application.create_default_window([400, 600], title="Interface de chiffrement NI")
application.window.mainloop()