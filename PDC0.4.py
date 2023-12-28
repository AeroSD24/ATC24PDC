import tkinter as tk
from datetime import datetime
import random
import winsound

def pdc_sound():
    sound_path = 'atc_message.wav'
    winsound.PlaySound(sound_path, winsound.SND_ASYNC)

def play_opening_sound():
    sound_path = 'startup.wav'
    winsound.PlaySound(sound_path, winsound.SND_ASYNC)

play_opening_sound()

print("MADE BY AERO, PDC0.3")

def generate_pdc():
    pdc_sound()
    acft = acft_entry.get()
    dest = dest_entry.get()
    route = route_entry.get()
    atis = atis_entry.get()
    RWY = rwy_entry.get()
    qnh = qnh_entry.get()

    utc_now = datetime.utcnow()
    utc = utc_now.strftime("%H:%M")

    # Unpack the SID and ALT returned by sidfind
    SID, ALT = sidfind(RWY, dest)

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"```"
                      f"[IRFD PDC]\n"
                      f"---------------------------------------------\n"
                      f"Aircraft: {acft}\n"
                      f"Departure Airport: IRFD\n"
                      f"Destination Airport: {dest}\n"
                      f"Clearance Time: {utc}\n"
                      f"---------------------------------------------\n"
                      f"\n"
                      f"[Clearance Information]\n"
                      f"---------------------------------------------\n"
                      f"Cleared to: {dest}\n"
                      f"SID: {SID}\n"
                      f"Initial Altitude: {ALT}\n"
                      f"Route: {route}\n"
                      f"Squawk Code: {''.join(random.choice('01234567') for _ in range(4))}\n"
                      f"---------------------------------------------\n"
                      f"\n"
                      f"[Additional Information]\n"
                      f"---------------------------------------------\n"
                      f"Current ATIS: {atis}\n"
                      f"Pressure: {qnh}\n"
                      f"Special Instructions: WHEN READY FOR PUSH REPORT STAND NUMBER AND ACFT TYPE TO THE ACTIVE CONTROLLER IF UNABLE SID CONTACT CONTROLLER\n"
                      f"---------------------------------------------\n"
                      f"[END PDC]\n"
                      f"```")
    result_text.config(state=tk.DISABLED)

def copy_pdc():
    # Get the content of the Text widget
    pdc_content = result_text.get("1.0", tk.END)
    
    # Clear the clipboard and append the PDC content
    app.clipboard_clear()
    app.clipboard_append(pdc_content)
    
    # Update the clipboard
    app.update()


def sidfind(RWY, dest):
    if RWY == "18R":
        if dest == "ITKO" or dest == "IDCS":
            SID = "WELSH1R"
            ALT = "2000"
        elif dest == "IPPH" or dest == "IBTH" or dest == "ILKL" or dest == "IMLR":
            SID = "INDEX1R"
            ALT = "2000"
        elif dest == "ISCM" or dest == "IJAF" or dest == "IZOL" or dest == "ISKP":
            SID = "SETHR1R"
            ALT = "2000"
        elif dest == "ILAR" or dest == "IPAP" or dest == "IBAR" or dest == "IHEN":
            SID = "LAZER1R"
            ALT = "3000"
        elif dest == "ISAU" or dest == "IGRV":
            SID = "GUESS1R"
            ALT = "2000"
        else:
            print("ERROR204")
            
    elif RWY == "18L":
        if dest == "ITKO" or dest == "IDCS":
            SID = "WELSH1Y"
            ALT = "2000"

        elif dest == "IPPH" or dest == "IBTH" or dest == "ILKL" or dest == "IMLR":
            SID = "INDEX1Y"
            ALT = "2000"

        elif dest == "ISCM" or dest == "IJAF" or dest == "IZOL" or dest == "ISKP":
            SID = "SETHR1Y"
            ALT = "2000"

        elif dest == "ILAR" or dest == "IPAP" or dest == "IBAR" or dest == "IHEN":
            SID = "LAZER1Y"
            ALT = "3000"

        elif dest == "ISAU" or dest == "IGRV":
            SID = "GUESS1Y"
            ALT = "2000"

        else:
            print("ERROR204")



    elif RWY == "36L":
        if dest == "ITKO" or dest == "IDCS":
            SID = "WELSH1S"
            ALT = "2000"

        elif dest == "IPPH" or dest == "IBTH" or dest == "ILKL" or dest == "IMLR":
            SID = "INDEX1S"
            ALT = "2000"

        elif dest == "ISCM" or dest == "IJAF" or dest == "IZOL" or dest == "ISKP":
            SID = "SETHR1S"
            ALT = "2000"

        elif dest == "ILAR" or dest == "IPAP" or dest == "IBAR" or dest == "IHEN":
            SID = "LAZER1S"
            ALT = "3000"

        elif dest == "ISAU" or dest == "IGRV":
            SID = "GUESS1S"
            ALT = "2000"

        else:
            print("ERROR204")

    elif RWY == "36R":
        if dest == "ITKO" or dest == "IDCS":
                SID = "WELSH1Z"
                ALT = "2000"

        elif dest == "IPPH" or dest == "IBTH" or dest == "ILKL" or dest == "IMLR":
                SID = "INDEX1Z"
                ALT = "2000"

        elif dest == "ISCM" or dest == "IJAF" or dest == "IZOL" or dest == "ISKP":
                SID = "SETHR1Z"
                ALT = "2000"

        elif dest == "ILAR" or dest == "IPAP" or dest == "IBAR" or dest == "IHEN":
                SID = "LAZER1Z"
                ALT = "3000"

        elif dest == "ISAU" or dest == "IGRV":
                SID = "GUESS1Z"
                ALT = "2000"

        else:
            print("ERROR204")

    return SID, ALT



# Create the main application window
app = tk.Tk()
app.title("PDC Generator")

# Widgets (as before)
acft_label = tk.Label(app, text="Aircraft Type:")
acft_entry = tk.Entry(app)

dest_label = tk.Label(app, text="Destination:")
dest_entry = tk.Entry(app)

route_label = tk.Label(app, text="Route:")
route_entry = tk.Entry(app)

atis_label = tk.Label(app, text="Current ATIS:")
atis_entry = tk.Entry(app)

rwy_label = tk.Label(app, text="Departure RWY:")
rwy_entry = tk.Entry(app)

qnh_label = tk.Label(app, text="Current QNH:")
qnh_entry = tk.Entry(app)

generate_button = tk.Button(app, text="Generate PDC", command=generate_pdc)

result_text = tk.Text(app, height=40, width=100)
result_text.config(state=tk.DISABLED)

notes_text = tk.Text(app, height=10, width=100)
notes_text.insert(tk.END, "Notes: ")  # Insert the initial text




# Grid layout (as before)
acft_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
acft_entry.grid(row=0, column=1, padx=10, pady=5)

dest_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
dest_entry.grid(row=1, column=1, padx=10, pady=5)

route_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
route_entry.grid(row=2, column=1, padx=10, pady=5)

atis_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
atis_entry.grid(row=3, column=1, padx=10, pady=5)

rwy_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
rwy_entry.grid(row=4, column=1, padx=10, pady=5)

qnh_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
qnh_entry.grid(row=5, column=1, padx=10, pady=5)

notes_text.grid(row=8, column=0,columnspan=2, padx=10, pady=10)


generate_button.grid(row=6, column=1, pady=10)

result_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)


copy_button = tk.Button(app, text="Copy PDC", command=copy_pdc)
copy_button.grid(row=6, column=0, pady=10)
# Start the main loop
app.mainloop()
