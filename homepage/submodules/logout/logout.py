# logout.py
def logout(root):
    root.destroy()
    from login_page.login import show_login_page
    show_login_page()