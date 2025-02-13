import tkinter as tk
import os
import subprocess

def run_command(command):
    try:
        output = subprocess.run(command, shell=True, text=True, capture_output=True)
        terminal_output.config(state=tk.NORMAL)
        terminal_output.delete(1.0, tk.END)
        terminal_output.insert(tk.END, output.stdout + output.stderr)
        terminal_output.config(state=tk.DISABLED)
    except Exception as e:
        terminal_output.config(state=tk.NORMAL)
        terminal_output.insert(tk.END, f'Error: {str(e)}\n')
        terminal_output.config(state=tk.DISABLED)

def require_root():
    if os.geteuid() != 0:
        root_warning = tk.Toplevel(r)
        root_warning.title("Permission Error")
        tk.Label(root_warning, text="This program requires root access!", fg="red").pack(pady=10)
        tk.Button(root_warning, text="OK", command=root_warning.destroy).pack(pady=5)
        return False
    return True

r = tk.Tk()
r.title('Apache Website Manager')

# Buttons for Apache management
button_install_apt = tk.Button(r, text="Install Apache (APT)", width=25, command=lambda: run_command("sudo apt install apache2 -y"))
button_install_dpkg = tk.Button(r, text="Install Apache (DPKG)", width=25, command=lambda: run_command("sudo dpkg -i apache2"))
button_install_dnf = tk.Button(r, text="Install Apache (DNF)", width=25, command=lambda: run_command("sudo dnf install httpd -y"))
button_install_pacman = tk.Button(r, text="Install Apache (PACMAN)", width=25, command=lambda: run_command("sudo pacman -S apache --noconfirm"))
button_start_apache = tk.Button(r, text="Start Apache", width=25, command=lambda: run_command("sudo systemctl start apache2"))
button_stop_apache = tk.Button(r, text="Stop Apache", width=25, command=lambda: run_command("sudo systemctl stop apache2"))
button_status_apache = tk.Button(r, text="Check Apache Status", width=25, command=lambda: run_command("sudo systemctl status apache2"))
button_uninstall_apache = tk.Button(r, text="Uninstall Apache", width=25, command=lambda: run_command("sudo apt remove apache2 -y"))

# Terminal output display
terminal_output = tk.Text(r, height=10, width=60, state=tk.DISABLED, bg="black", fg="white")

# Pack buttons
button_install_apt.pack()
button_install_dpkg.pack()
button_install_dnf.pack()
button_install_pacman.pack()
button_start_apache.pack()
button_stop_apache.pack()
button_status_apache.pack()
button_uninstall_apache.pack()
terminal_output.pack(pady=10)

if not require_root():
    r.withdraw()

r.mainloop()
