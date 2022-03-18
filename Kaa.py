
#considers the calculations are based on 24FPS
##from tkinter import *
##using Python 3.7.6
##
##root = Tk()
##
###creating a label widget
##myLabel1 = Label(root, text ="Hello Cesar!")
##myLabel2 = Label(root, text ="Welcome to Kaa!")
##myButton = Button(root,text="run_Program")
##
##myLabel1.grid(row=0,column=0)
##myLabel2.grid(row=1,column=1)
##myButton.grid(row=0,column=1)
##
##
###Here we are sending it to go.
###myLabel1.pack()
###myLabel2.pack()
##
##root.mainloop()


def run_Program():

    tList = []  ###List that will check if current clip has been encountered before
    my_dict = {} ###will store name and length of all clips

    f = open("test_file.edl","r")   ### opens our edl file
    fList = f.readlines()           ### stores contents of file line by line
    f.close()                       ### close file


    #The next line creates a csv file that will store the name and length of music used.

    n = open(fList[0][7:-1] + ".csv","w")

    n.write("ID, Music Title,clip start,clip end, duration, duration(frames)\n")

    # the for loop below will navigate the file line by line until it hits
    # a numerical mark where we can parse the
    # header info and then move in to the clip title.

    for i in fList:
        if i[0].isdigit():              # Checks if we are at a line that starts with a digit
            id = i[0:3]                 # log the clips id
            num1 = i[29:40]             # log the starting timecode
            f1 = int(num1[-2:])         # isolate the frames
            s1 = int(num1[6:8])*24      # isolate the seconds and calculating to frames
            m1 = int(num1[3:5])*1440    # isolate the minutes and calculating to frames
            h1 = int(num1[:2])*86400    # isolate the hours and calculating to frames
            num2 = i[41:52]             # log the ending timecode
            f2 = int(num2[-2:])         # frames
            s2 = int(num2[6:8])*24      # seconds and calculating to frames
            m2 = int(num2[3:5])*1440    # minutes and calculating to frames
            h2 = int(num2[:2])*86400    # hours and calculating to frames
            frame_duration = (f2+s2+m2+h2) - (f1+s1+m1+h1)  # subtracting beginning from end to get duration
            h3 = int(frame_duration /  86400)  # rebuilding total hours
            m3 = int(frame_duration /  1440)   # # rebuilding total minutes
            s3 = int(frame_duration / 24)      # rebuilding total seconds
            f3 = frame_duration % 24           # rebuilding total frames
            nh3 = str(h3) if h3 > 9 else "0" + str(h3)  # condition to add a zero for proper timecode layout
            nm3 = str(m3) if m3 > 9 else "0" + str(m3)  # ""
            ns3 = str(s3) if s3 > 9 else "0" + str(s3)  # ""
            nf3 = str(f3) if f3 > 9 else "0" + str(f3)  # ""

            duration = f"{nh3}:{nm3}:{ns3}:{nf3}"   # New String to hold our duration for this clip


        if i[0] is '*':         # lines that begin with * denote the title of the clip data from above.
            clip = i[18:-1]     # log the clip title then write to the csv file
            n.write(id +"," + clip + "," + num1 + "," + num2 + "," + duration + "," + str(frame_duration) + "\n")

            if clip not in tList: # check if we have come accross a clip from the same audio file

                tList.append(clip)             # if not we add it to our list
                my_dict[clip] = frame_duration # store the new clip and duration in list
            else:
                my_dict[clip] = my_dict[clip] + frame_duration # else we add the current clip length to the total



    for i in range(4):
        n.write(".\n")                  # Make space for total count
    n.write(",~~~~~~Totals~~~~~~\n")
    for l in tList:

        h4 = int(my_dict[l] /  86400)   #Rebuild the totals again in hh:mm:ss:ff
        m4 = int(my_dict[l] /  1440)
        s4 = int(my_dict[l] / 24)
        f4 = my_dict[l] % 24
        nh4 = str(h4) if h4 > 9 else "0" + str(h4)  # condition to add a zero for proper timecode layout
        nm4 = str(m4) if m4 > 9 else "0" + str(m4)  # ""
        ns4 = str(s4) if s4 > 9 else "0" + str(s4)  # ""
        nf4 = str(f4) if f4 > 9 else "0" + str(f4)  # ""
        duration2 = f"{nh4}:{nm4}:{ns4}:{nf4}"      # # New String to hold our combined duration for this clip
        n.write("," + l + "," + str(my_dict[l]) + "," + duration2 + "\n") #write to file

    n.close()

run_Program()
