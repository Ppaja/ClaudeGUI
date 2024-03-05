import tkinter as tk
from tkinter import ttk  
from anthropic import Anthropic

def send_request():
    api_key = api_key_entry.get()
    message_content = message_entry.get("1.0", tk.END).strip()  
    selected_model = model_var.get()  

    client = Anthropic(api_key=api_key)

    message = client.messages.create(
        model=selected_model,
        max_tokens=1000,
        temperature=0.0,
        system="",  # Add the system guide - for example "Respond only in Yoda-speak." or "Respond in a humorous and witty manner" etc
        messages=[
            {"role": "user", "content": message_content}
        ]
    )

    response_text.delete(1.0, tk.END)
    response_text.insert(tk.END, message.content[0].text)  

# Create window
root = tk.Tk()
root.title("Claude Chat")

api_key_label = tk.Label(root, text="API Key:")
api_key_label.grid(row=0, column=0, sticky="w")
api_key_entry = tk.Entry(root, width=150)
api_key_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

# Model selection dropdown
model_label = tk.Label(root, text="Select Model:")
model_label.grid(row=1, column=0, sticky="w")

models = [("Opus (Best Model)", "claude-3-opus-20240229"), 
          ("Sonnet (Medium)", "claude-3-sonnet-20240229"), 
          ("Haiku (Currently Not Supported)", "claude-3-haiku")]

model_var = tk.StringVar(root)
model_var.set(models[0][1])  # Default model selection

dropdown_options = [model_name for display_name, model_name in models]
model_dropdown = tk.OptionMenu(root, model_var, *dropdown_options)
model_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="we")

message_label = tk.Label(root, text="Your message:")
message_label.grid(row=2, column=0, sticky="nw")
message_entry = tk.Text(root, width=150, height=10)
message_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

send_button = tk.Button(root, text="Send", command=send_request)
send_button.grid(row=3, column=1, pady=10)

response_label = tk.Label(root, text="Response:")
response_label.grid(row=4, column=0, sticky="w")
response_text = tk.Text(root, width=150, height=50)
response_text.grid(row=4, column=1, padx=10, pady=5, sticky="we")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=response_text.yview)
scrollbar.grid(row=4, column=2, sticky="ns")
response_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
