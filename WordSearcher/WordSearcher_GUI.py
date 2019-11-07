from tkinter import *


class Application(Frame):
    """ GUI application which can reveal the secret of longevity. """

    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create character list label
        self.char_list_lbl = Label(self, text="Enter characters to search")
        self.char_list_lbl.grid(row=0, column=0, columnspan=1, sticky=W)

        # create character number label
        self.nb_char_lbl = Label(self, text="Number of characters in word")
        self.nb_char_lbl.grid(row=1, column=0, columnspan=1, sticky=W)

        # create entry widget to accept character list
        self.char_list_ent = Entry(self)
        self.char_list_ent.grid(row=0, column=1, sticky=W)

        # create entry widget to accept number of characters
        self.number_char_list_ent = Entry(self)
        self.number_char_list_ent.grid(row=1, column=1, sticky=W)

        # create submit button
        self.submit_bttn = Button(self, text="Submit", command=self.return_results)
        self.submit_bttn.grid(row=2, column=0, sticky=W)

        # create text widget to display message
        self.secret_txt = Text(self, width=35, height=25, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def return_results(self):
        """ Display message based on password. """
        characters_to_search_string = self.char_list_ent.get()
        characters_to_search_string = characters_to_search_string.lower()
        characters_to_search_tuple = tuple(characters_to_search_string)

        line_length = int(self.number_char_list_ent.get())
        words_found = []
        result_output_file = open("results.txt", "w")
        word_list_to_read = open("words_alpha.txt", "r")
        counter = 0

        for line in word_list_to_read.readlines():
            line = line.strip('\n')
            characters_to_search = list(characters_to_search_tuple)
            if any(x in line for x in characters_to_search) and len(line) == line_length:

                for line_character in line:
                    continue_flag = 0
                    try:
                        characters_to_search_index = characters_to_search.index(line_character)
                        characters_to_search.pop(characters_to_search_index)
                    except:
                        continue_flag = 1
                        break

                if continue_flag == 0:
                    #print(line, "\t", len(line), file=result_output_file)
                    result_output_file.close()
                    words_found.append(line)
                    # print(line, "\t", len(line))
                    counter = counter + 1

        message = words_found
        message.append(f'Number of matching words is: {counter}')
        print(f'Number of matching words is: {counter}')

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)
        word_list_to_read.close()
        result_output_file.close()


# main
root = Tk()
root.title("Lazy Word Generator")
root.geometry("300x485")
app = Application(root)
root.mainloop()
