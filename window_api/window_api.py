from Tkinter import *
import tkFileDialog
from ttk import Button, Label
import tkMessageBox
from neu_net import neu_net
import matplotlib.pyplot as plt


class window_if(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_variables()
        self.initUI()

    def initUI(self):
        self.parent.title("Neural network 1-3-1")
        self.grid_configure(ipadx=30)
        self.columnconfigure(0, pad=20)
        self.columnconfigure(1, pad=20)
        self.columnconfigure(2, pad=20)
        self.columnconfigure(3, pad=20)

        self.rowconfigure(0, pad=20)
        self.rowconfigure(1, pad=20)
        self.rowconfigure(2, pad=20)
        self.rowconfigure(3, pad=20)
        self.rowconfigure(4, pad=20)
        self.rowconfigure(5, pad=20)
        self.rowconfigure(6, pad=20)
        self.rowconfigure(7, pad=20)
        self.rowconfigure(8, pad=20)
        self.rowconfigure(8, pad=20)
        self.rowconfigure(9, pad=20)
        self.rowconfigure(10, pad=20)

        self.rowconfigure(11, pad=20)
        self.rowconfigure(12, pad=20)
        self.rowconfigure(13, pad=20)
        self.rowconfigure(14, pad=20)
        self.rowconfigure(15, pad=20)
        self.rowconfigure(16, pad=20)
        self.rowconfigure(17, pad=20)
        self.rowconfigure(18, pad=20)
        self.rowconfigure(19, pad=20)
        self.rowconfigure(20, pad=20)

        self.organize_labels()
        self.menu = self.create_manu_bar()
        self.plot_button = self.create_button("START", self.make_plots, 20).grid(row=18, column=1, sticky=W)



    def organize_labels(self):
        print 'organize_labels'
        self.L0LBL0 = Label(text="L0", width=10)
        self.L0LBL0.grid(row=0, column=0, sticky=W)
        self.L0LBL1 = Label(text="waga N1", width=10)
        self.L0LBL1.grid(row=1, column=0, sticky=W)
        self.L0wage = Entry()
        self.L0wage.insert(0,"0.893")
        self.L0wage.grid(row=1, column=1, sticky=W)
        self.L0LBL2 = Label(text="bias N1", width=10)
        self.L0LBL2.grid(row=2, column=0, sticky=W)
        self.L0BIAS = Entry()
        self.L0BIAS.insert(0, "0.738")
        self.L0BIAS.grid(row=2, column=1, sticky=W)

        self.L1LBL0 = Label(text="L1", width=10)
        self.L1LBL0.grid(row=3, column=0, sticky=W)
        self.L1LBL1 = Label(text="waga N2", width=10)
        self.L1LBL1.grid(row=4, column=0, sticky=W)
        self.L1wage1 = Entry()
        self.L1wage1.insert(0, "0.057")
        self.L1wage1.grid(row=4, column=1, sticky=W)
        self.L1LBL2 = Label(text="bias N2", width=10)
        self.L1LBL2.grid(row=5, column=0, sticky=W)
        self.L1BIAS1 = Entry()
        self.L1BIAS1.insert(0, "0.176")
        self.L1BIAS1.grid(row=5, column=1, sticky=W)

        self.L1LBL3 = Label(text="waga N3", width=10)
        self.L1LBL3.grid(row=6, column=0, sticky=W)
        self.L1wage2 = Entry()
        self.L1wage2.insert(0, "0.352")
        self.L1wage2.grid(row=6, column=1, sticky=W)
        self.L1LBL4 = Label(text="bias N3", width=10)
        self.L1LBL4.grid(row=7, column=0, sticky=W)
        self.L1BIAS2 = Entry()
        self.L1BIAS2.insert(0, "0.405")
        self.L1BIAS2.grid(row=7, column=1, sticky=W)

        self.L1LBL5 = Label(text="waga N4", width=10)
        self.L1LBL5.grid(row=8, column=0, sticky=W)
        self.L1wage3 = Entry()
        self.L1wage3.insert(0, "0.813")
        self.L1wage3.grid(row=8, column=1, sticky=W)
        self.L1LBL6 = Label(text="bias N4", width=10)
        self.L1LBL6.grid(row=9, column=0, sticky=W)
        self.L1BIAS3 = Entry()
        self.L1BIAS3.insert(0, "0.935")
        self.L1BIAS3.grid(row=9, column=1, sticky=W)

        self.L2LBL7 = Label(text="L3", width=10)
        self.L2LBL7.grid(row=10, column=0, sticky=W)
        self.L2LBL8 = Label(text="waga[1] N5", width=10)
        self.L2LBL8.grid(row=11, column=0, sticky=W)
        self.L2wage1 = Entry()
        self.L2wage1.insert(0, "0.009")
        self.L2wage1.grid(row=11, column=1, sticky=W)
        self.L2LBL9 = Label(text="waga[2] N5", width=10)
        self.L2LBL9.grid(row=12, column=0, sticky=W)
        self.L2wage2 = Entry()
        self.L2wage2.insert(0, "0.138")
        self.L2wage2.grid(row=12, column=1, sticky=W)
        self.L2LBL10 = Label(text="waga[3] N5", width=10)
        self.L2LBL10.grid(row=13, column=0, sticky=W)
        self.L2wage3 = Entry()
        self.L2wage3.insert(0, "0.202")
        self.L2wage3.grid(row=13, column=1, sticky=W)
        self.L2LBL11 = Label(text="bias N5", width=10)
        self.L2LBL11.grid(row=14, column=0, sticky=W)
        self.L2BIAS = Entry()
        self.L2BIAS.insert(0, "0.410")
        self.L2BIAS.grid(row=14, column=1, sticky=W)

        self.EpochLbl = Label(text="EPOCH NR", width=10)
        self.EpochLbl.grid(row=15, column=0, sticky=W)
        self.Epoch = Entry()
        self.Epoch.insert(0, "600")
        self.Epoch.grid(row=15, column=1, sticky=W)
        self.LearnLbl = Label(text="COEFF", width=10)
        self.LearnLbl.grid(row=16, column=0, sticky=W)
        self.Learn = Entry()
        self.Learn.insert(0, "0.9")
        self.Learn.grid(row=16, column=1, sticky=W)

        self.LBL = Label(text="                 ", width=20)
        self.LBL.grid(row=17, column=0, sticky=W)
        self.LBL = Label(text="WAITING FOR INPUT", width=20)
        self.LBL.grid(row=18, column=0, sticky=W)

    def organize_learned_labels(self):
        self.ldesc = Label(text="", width=20)
        self.ldesc.grid(row=0, column=2, sticky=W)

        self.lL0w0 = Label(text="", width=20)
        self.lL0w0.grid(row=1, column=2, sticky=W)
        self.lL0b = Label(text="", width=20)
        self.lL0b.grid(row=2, column=2, sticky=W)

        self.lL1w1 = Label(text="", width=20)
        self.lL1w1.grid(row=4, column=2, sticky=W)
        self.lL1b1 = Label(text="", width=20)
        self.lL1b1.grid(row=5, column=2, sticky=W)

        self.lL1w2 = Label(text="", width=20)
        self.lL1w2.grid(row=6, column=2, sticky=W)
        self.lL1b2 = Label(text="", width=20)
        self.lL1b2.grid(row=7, column=2, sticky=W)

        self.lL1w3 = Label(text="", width=20)
        self.lL1w3.grid(row=8, column=2, sticky=W)
        self.lL1b3 = Label(text="", width=20)
        self.lL1b3.grid(row=9, column=2, sticky=W)

        self.lL2w1 = Label(text="", width=20)
        self.lL2w1.grid(row=11, column=2, sticky=W)
        self.lL2w2 = Label(text="", width=20)
        self.lL2w2.grid(row=12, column=2, sticky=W)
        self.lL2w3 = Label(text="", width=20)
        self.lL2w3.grid(row=13, column=2, sticky=W)
        self.lL2b = Label(text="", width=20)
        self.lL2b.grid(row=14, column=2, sticky=W)

    def create_manu_bar(self):
        menubar = Menu(self.parent)
        file_menu = Menu(menubar)
        file_menu.add_command(label='Teaching data', command=self.choose_data_path)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.onExit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.parent.config(menu=menubar)

    def create_button(self, name, function, wdt):
        button = Button(text=name, command=function, width=wdt)
        return button

    def init_variables(self):
        print 'init_variables'
        self.teaching_vector_path = ""
        self.teaching_vector = list()
        self.teaching_vector.append(list())
        self.teaching_vector.append(list())
        self.figure = 1

    def choose_data_path(self):
        self.teaching_vector_path = tkFileDialog.askopenfilename()
        print self.teaching_vector_path
        self.read_teaching_vector()

    def check_input(self):
        try:
            self.L0w = float(self.L0wage.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L1 N1 wage is not a float")
            return 1

        try:
            self.L0b = float(self.L0BIAS.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L1 N1 BIAS is not a float")
            return 1
        #
        try:
            self.L1w1 = float(self.L1wage1.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L2 N2 wage is not a float")
            return 1

        try:
            self.L1b1 = float(self.L1BIAS1.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L2 N2 BIAS is not a float")
            return 1

        try:
            self.L1w2 = float(self.L1wage2.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L2 N2 wage is not a float")
            return 1

        try:
            self.L1b2 = float(self.L1BIAS2.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L2 N3 BIAS is not a float")
            return 1

        try:
            self.L1w3 = float(self.L1wage3.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L2 N4 wage is not a float")
            return 1

        try:
            self.L1b3 = float(self.L1BIAS3.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L2 N4 BIAS is not a float")
            return 1

        ##
        try:
            self.L2w1 = float(self.L2wage1.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L3 N5 wage1 is not a float")
            return 1
        try:
            self.L2w2 = float(self.L2wage2.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L3 N5 wage2 is not a float")
            return 1
        try:
            self.L2w3 = float(self.L2wage3.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L3 N5 wage3 is not a float")
            return 1
        try:
            self.L2b = float(self.L2BIAS.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "L3 N5 BIAS is not a float")
            return 1
        try:
            self.coeff = float(self.Learn.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "COEFF is not a float")
            return 1

        try:
            self.epo = float(self.Epoch.get())
        except ValueError:
            tkMessageBox.showinfo("Wrong Input", "EPOCH is not a float")
            return 1

        return 0

    def read_teaching_vector(self):
        self.teaching_vector[1] = []
        self.teaching_vector[0] = []
        print "read_teaching_vector"
        f = open(self.teaching_vector_path)
        teaching_vec = f.readlines()
        for i in range(len(teaching_vec)):
            [samp, val] = teaching_vec[i].split()
            self.teaching_vector[0].append(float(samp))
            self.teaching_vector[1].append(float(val))
        f.close()
        print self.teaching_vector[0]
        print self.teaching_vector[1]


    def create_network(self):
        if(len(self.teaching_vector[0]) != len(self.teaching_vector[1])):
            print "len(self.teaching_vector[0]): " + str(len(self.teaching_vector[0]))
            print "len(self.teaching_vector[1]): " + str(len(self.teaching_vector[1]))
            tkMessageBox.showinfo("Wrong Input", "Teaching vector has wrong size")
            return -1

        if (len(self.teaching_vector[0]) == 0 or  len(self.teaching_vector[1]) == 0):
            tkMessageBox.showinfo("Wrong Input", "Please provide teaching vector")
            return -1

        siec = neu_net.neu_net(3, self.teaching_vector[0], self.teaching_vector[1], self.coeff, self.epo)
        siec.initialize_layer(0, 1, 1, 3)
        siec.initialize_perceptron(0, 0, [self.L0w], self.L0b)
        siec.print_info(0)
        siec.initialize_layer(1, 3, 1, 1)
        siec.initialize_perceptron(1, 0, [self.L1w1], self.L1b1)
        siec.initialize_perceptron(1, 1, [self.L1w2], self.L1b2)
        siec.initialize_perceptron(1, 2, [self.L1w3], self.L1b3)
        siec.print_info(1)
        siec.initialize_layer(2, 1, 3, 1)
        siec.initialize_perceptron(2, 0, [self.L2w1, self.L2w2, self.L2w3], self.L2b)
        siec.print_info(2)
        return siec



    def make_plots(self):
        self.organize_learned_labels()
        print "make_plots"
        ret = self.check_input()
        if ret:
            print "Wrong input please correct it"
            return -1
        else:
            print "Next step: creating neural network"

        siec = self.create_network()
        if siec == 1:
            print "Network was not created"
            return -1
        else:
            print "Next step: learning and plotting"

        self.LBL.config(text="TEACHING")
        self.LBL.update_idletasks()
        siec.teach_network()

        self.LBL.config(text="RUNNING NET")
        self.LBL.update_idletasks()
        siec.start_net(self.teaching_vector[0])
        plt.figure(self.figure)
        plt.plot(self.teaching_vector[0], siec.out_teached, 'r', label='siec neuronowa')
        plt.plot(self.teaching_vector[0], self.teaching_vector[1], 'b', label='wektor uczacy')
        plt.ylabel("Wartosc funkcji")
        plt.xlabel("Argument")
        plt.legend()
        plt.grid()
        self.figure+=1
        plt.figure(self.figure)
        plt.plot(siec.epoch_n, siec.err_ep, 'r')
        plt.ylabel("Wartosc bledu")
        plt.xlabel("Epoka uczaca")
        plt.grid()
        self.figure += 1
        self.LBL.config(text="DONE")
        self.LBL.update_idletasks()
        self.read_learned_values(siec)
        plt.show()

    def read_learned_values(self, lsiec):
        self.ldesc.config(text="Learned")
        self.ldesc.update_idletasks()

        self.lL0w0.config(text=str(lsiec.layers[0][0].wages[0]))
        self.lL0w0.update_idletasks()
        self.lL0b.config(text=str(lsiec.layers[0][0].bias))
        self.lL0b.update_idletasks()

        self.lL1w1.config(text=str(lsiec.layers[1][0].wages[0]))
        self.lL1w1.update_idletasks()
        self.lL1b1.config(text=str(lsiec.layers[1][0].bias))
        self.lL1b1.update_idletasks()

        self.lL1w2.config(text=str(lsiec.layers[1][1].wages[0]))
        self.lL1w2.update_idletasks()
        self.lL1b2.config(text=str(lsiec.layers[1][1].bias))
        self.lL1b2.update_idletasks()

        self.lL1w3.config(text=str(lsiec.layers[1][2].wages[0]))
        self.lL1w3.update_idletasks()
        self.lL1b3.config(text=str(lsiec.layers[1][2].bias))
        self.lL1b3.update_idletasks()

        self.lL2w1.config(text=str(lsiec.layers[2][0].wages[0]))
        self.lL2w1.update_idletasks()
        self.lL2w2.config(text=str(lsiec.layers[2][0].wages[1]))
        self.lL2w2.update_idletasks()
        self.lL2w3.config(text=str(lsiec.layers[2][0].wages[2]))
        self.lL2w3.update_idletasks()
        self.lL2b.config(text=str(lsiec.layers[2][0].bias))
        self.lL2b.update_idletasks()







    def onExit(self):
        self.quit()

    def onClick(self):
        if self.phase_plot.get() == True:
            self.parent.title("Phase plot will be made")
        elif self.phase_plot.get() == False:
            self.parent.title("Ni ma")

def start_analyzer():
    root = Tk()
    root.geometry("370x370+250+250")
    app = window_if(root)
    root.mainloop()
